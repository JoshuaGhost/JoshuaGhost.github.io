Title: python并发编程
Date: 2023-08-27
Tag: 自学, python, 并发

## multithreading, threads, asyncio

Status: python

## asyncio，threading和multiprocessing之间的区别与联系

参考资料: [https://medium.com/analytics-vidhya/asyncio-threading-and-multiprocessing-in-python-4f5ff6ca75e8](https://medium.com/analytics-vidhya/asyncio-threading-and-multiprocessing-in-python-4f5ff6ca75e8)

TBD

## 整理自领英文章[How can you succeed with parallel programming？](https://www.linkedin.com/advice/0/how-can-you-succeed-parallel-programming-skills-computer-science?utm_source=share&utm_medium=member_android&utm_campaign=share_via)

并行化的不同paradigm

- shared memory
  - - 容易实现
  - - 竞态条件
- message passing
  - - 可以scalable
  - - 需要更多coordination（design and coordination overhead）
- data parallel
- task parallel
- functional parallel

不同的tools

OpenMPI， MPI， CUDA， Spark

## 为啥要用Asyncio

threading和multiprocessing都有各自的限制：

- threading受GIL限制。GIL每次只让一个线程执行。但执行 I/O（例如文件、套接字和外围设备）时，会释放此锁(https://superfastpython.com/asyncio-vs-threading/)，所以所以搞IO密集型的程序的时候用threading比较好
- multiprocessing受操作系统最大进程数限制，所以搞CPU密集型的时候用multiprocessing
- asyncio是python3.4之后的新模块，支持异步处理，单线程但是允许多处移交控制权（比如在等待IO之类的时候）。因为是单线程所以对于CPU密集型的程序并不会提升效率，但对于IO密集型的程序不受GIL限制。而且asyncio的协程本质上是函数，所以它是一个轻量级的并发模型

## 最简单的例子：coroutine + Task

asyncio协程函数是用async描述的“函数”，这里我之所以用引号引起来“函数”，是因为这个“函数”其实已经被async变成了一个coroutine对象。

这种coroutine对象在代码调用的时候前面加上await关键字来“等待式”调用，即当前位置需要等待await后的操作完成后才能往下走，而不是直接叫出控制权。async-await有传染性，即await调用了async函数的函数也是一个协程。

协程函数可以被asyncio.run()激活，还可以用多个coroutine组合起来交给asyncio.gather函数并发执行

```python
import asyncio

async def task_coro():
    print("The task is running")
    await asyncio.sleep(2)
    print("The task is done")
    return "the answer is 42"

async def main():
		import time
		tic = time.perf_counter()
    task = asyncio.create_task(task_coro())
		# 注意task在这里就已经开始执行了，因为asyncio.create_task()本身就会安排
		# 里面的协程尽快运行
    print("The main is running")
		# 这里的await和上面的task是并发执行的
    await asyncio.sleep(2)
    print(f"before await for task"）
    await task
		print(time.perf_counter() - tic)
		# 这里输出的经过时间应该在两秒左右，而不是4秒，这是因为
    print(task.__class__)
    print(f"after await for task")
    print(f"got: {task.result()}")

asyncio.run(main())
```

## Future

await可以作用在三种awaitable对象上：coroutine，Task和Future，其中coroutine就是上面定义的async def函数，Task就是asyncio.create_task()升沉的Task，Future是比较基础的类，并不需要用户手工定义，但其实下边的gather生成的是Future：

```python
import random
import asyncio

random.seed(42)

async def task_coro_1(arg):
    value = random.random()
    await asyncio.sleep(value)
    print(f"Task {arg} done after {value:.2f} seconds")
		return arg

async def main():
    coros = [task_coro_1(i) for i in range(10)]
    print(coros[0].__class__)
    # gather函数返回一个Future对象，接受多个awaitables（可变长参数，所以这里用iterable
    # comprehension）
    # await是一种阻塞式调用，所以这里的gather函数会等待所有的coroutine执行完毕
    # 如果这里不加await，并且之后没有其它耗时操作，那么gather函数就会抛出cancelledError异常
    # 因为时间不够，各个coroutine还没有执行完毕，就被main函数结束了
    # 如果这里不加await，但是之后还有其它耗时操作，那么gather函数创建的Future也是有可能完成的，
    # 也就是说如果main的流程足够长，以至于最长的coroutine都完成了，也是可以gather到全部结果的。
    # 所以这里有两种写法：
    # 1.
    # ret = await asyncio.gather(*coros)
    # 2.
    ret = asyncio.gather(*coros)
    await asyncio.sleep(LONG_ENOUGH_TIME)
		return ret

print(asyncio.run(main()))
## 结果是[0,1,2,3,4,5,6,7,8,9]，即gather的返回值是按照调用时候的参数顺序排列的
## 但task_coro_1协程中的print则是按照对应协程await asnco.sleep的时长从短到长
## 输出的
```

## asyncio.wait premitive

wait premitive可以指定一系列tasks返回的条件，我们可以先定义一个iterable的Task（s），再用asyncio.wait指定这些tasks满足什么条件的时候（比如超时、有一个协程完成、有一个协程抛出异常，所有协程都完成了）暂停各协程的执行，并把完成的协程（done）和执行到一半的协程（pending）分别返回出来。

done和pending都是set()

wait在因为超时而返回的时候，[并不会抛出TimeoutError错误](https://docs.python.org/3/library/asyncio-task.html#waiting-primitives)，而是把还没来得及完成的任务返到pending中

```python
import asyncio
import random

random.seed(42)

async def task_coro(arg):
    value = random.random()
    await asyncio.sleep(value)
    return arg * value

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # return_when表示返回条件，
    # 默认是all_completed（asyncio.ALL_COMPLETED），表示所有的coroutine都完成之后才返回
    # 这里指定为FIRST_COMPLETED，表示只要有一个coroutine完成了，就返回
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(len(done), len(pending))
    print(done.__class__, pending.__class__)
    task = done.pop()
    print(f"First finished task got: {task.result():.2f}")

		# 其它在pending的task还是可以通过await继续执行的
		task = pending.pop()
		await task
		print(f'one of the unfinished coro got: {task.result():.2f}')

asyncio.run(main())
```

## 按照完成顺序返回

asyncio.as_completed可以让一串tasks按照完成顺序返回

```python
async def task_coro(arg):
    value = random.random() * 10
    await asyncio.sleep(value)
    # 这会导致caller里面的await关键字抛出一个异常
    # if value > 5:
    #     raise ValueError(f"Boom from {arg}")
    return arg * value

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # 这里的for是让tasks按照完成的顺序返回，如果超时了就抛出TimeOutError
    for task in asyncio.as_completed(tasks):
        # 这里必须await
        result = await task
        print(f"> got result: {result:.2f}")

asyncio.run(main())
```

## 生产者-消费者-队列模型：

asyncio提供了一个与[synchronized queue](https://docs.python.org/3/library/queue.html)对应的异步queue，我们可以用它来实现异步生产者-消费者模型

```python
async def producer(queue):
    value = random.random()
    await asyncio.sleep(value)
    await queue.put(value)
    # 这里也需要写queue.task_done(),因为task_done()一般是用在consumer里面的
    # 它的功能是,对应producer put进来的所有元素,consumer get一个,就调用一次task_done()
    # 最后task_done(注意不是get的次数)和put的次数想等的时候,queue.join()才会返回

    # 用task_done和join的时候,一般是快速生产,慢速消费的场景。这样在完成之前队列里面一直有元素,
		# 即里面未完成的元素一直大于0，所以join()直到所有元素都被消耗完之前一直会block当前函数。

    # 而慢速生产快速消费的情况不能用join判断,因为生产的速度慢,所以在消费完之前,队列里面的元素
    # 就会消耗殆尽,这时候join()就会停止block当前函数。但是实际上这时生产可能还没有完成。
    # 所以这种情况可以用特殊标记标识生产完成,比如await queue.put(None)（如下一组producer-
    # consumer模型所示）
    # 参考文献:
    # [1] https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.task_done
    # [2] https://www.vuln.cn/8610
    print(f"Producer: {value:.5f}")
    return value * 10

async def consumer():
    queue = asyncio.Queue()
    tasks = [asyncio.create_task(producer(queue)) for _ in range(10)]
    # 这里其实不用await queue.join(),因为join()只是等待queue中的所有元素都被加入了,
    # 但我们这里的as_completed并不care是否*所有*的元素都被加入了,按照完成顺序返回，
		# 而coroutine每完成一个，就相当于队列里多了一个元素，就可以用下边的await queue.get()
    # 来取元素了。
    for task in asyncio.as_completed(tasks):
        ret = await task
        print(f"queue element: {await queue.get():.5f}")
        print(f"Consumer: {ret:.5f}")

asyncio.run(consumer())

async def producer(queue):
    print("Producer: running")
    for i in range(10):
        value = random.random()
        await asyncio.sleep(value)
        # queue put(get)还有对应的non-waiting方法put_nowait(get_nowait),非阻塞，直接
				# 放入（取走）元素，而不用写await等待
        await queue.put(value)
    await queue.put(None)
    print("Producer: Done")

async def consumer():
    queue = asyncio.Queue()
    asyncio.create_task(producer(queue))
    while True:
        value = await queue.get()
        if value is None:
            break
        print(f"Consumer: {value:.5f}")

asyncio.run(consumer())
```

## 实践操作，使用async.open_onnection来异步下载页面

```python
import asyncio
import random

random.seed(42)

async def main():
    host, port, path = "www.google.com", 443, "/"
    reader, writer = await asyncio.open_connection(host, port, ssl=True)
    # 上面只是阻塞性地建立了连接，下面才是真正的发送数据
    query = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(query.encode())
    await writer.drain()
    response = await reader.readline()
    status = response.decode().strip()
    print(status)
    writer.close()

asyncio.run(main())
```

## 优先队列（数据结构那个堆）、LIFO队列（栈）

参考：[https://www.cnblogs.com/traditional/p/17398542.html](https://www.cnblogs.com/traditional/p/17398542.html)

TBD
