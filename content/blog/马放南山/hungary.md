Title: 听ghost讲那匈牙利算法的事情
Date:  2022-12-17
Tas:   NOIP, 匈牙利算法, 算法, 二分图匹配

具体的不用解释了吧，就是匈牙利算法，做二分图匹配用的。粘在这里只是为了防止自己电脑数据异常丢失……。

这是百度百科上匈牙利算法的pascal原版程序，只是改了改格式而已。百度上的是用邻接矩阵写的，过两天我写一个python-based邻接表版本的。矩阵版的时间复杂度为$O(n^3)$，邻接表则变成了$O(EN)$，在边的个数小的时候明显占优势。

```
#!pascal
program matching;
const
    max = 1000;
var
    map : array [1..max, 1..max] of boolean;
    match: array [1..max] of integer;
    chk : array [1..max] of boolean;
    m, n, i, t1, t2, ans,k: integer;

function dfs(p: integer): boolean;
var
    i, t: integer;
begin
    for i:=1 to k do
        if map[p, i] and not chk[ i ] then begin 
            chk[ i ] := true;
            //p是左边（源），i是右边（汇）
            //重点是这里，在每次主循环中，如果我保持当前的p-i对应（暨让i的chk被p占用），并且
            //递归深搜地能给i的原matching找到一个新的对应，并在最终一次递归的时候让最后的i
            //找到一个之前从来没有matching过的i，并把最后的p分配给这个之前没有遇到过的i
            //
            //想像一个新人坐到一个椅子上，他把这个椅子上原来坐着的人赶走了，于是这个原来坐这儿
            //的人又找到他喜欢的另一把椅子，如果另一把椅子上有人，就把那个人再赶走，以此类推。
            //如果最后一个人还是能找到一把空椅子(matching[i] = 0)的话，那就说明这堆椅子又
            //能多坐一个人了
            if (match[ i ] = 0) or dfs(match[ i ]) then begin
                match[ i ] := p;
                exit(true)
            end
        end;
    exit(false)
end;

begin
    readln(n, m);
    fillchar(map, sizeof(map), 0);
    k:=0;
    for i:=1 to m do begin
        readln(t1, t2);
        
        map[t1, t2] := true;
        if k<t2 then k:=t2
    end;

    fillchar(match, sizeof(match), 0);
    ans := 0;
    for i:=1 to n do begin
        fillchar(chk, sizeof(chk), 0);
        if dfs(i) then inc(ans)
    end;
    
    writeln(ans);
    for i:=1 to 1000 do
        if match[ i ] <> 0 then
            writeln(match[ i ], '-->', i)
end.
```

然后以下是时隔13年的邻接表：

```
#!python
# 邻接表样式

n, m = read()

pre = [None] * m
last = [] * n
other = [] * m
n_edge = 0
n_matching = 0

matching = [None] * n
visited = [False] * n

def is_extentable(p: int) -> bool:
    p_edge = last[p]
    while pre[p_edge] is not None:
        other_node = other[pre[p_edge]]
        if not visited[other_node]:
            visited[other_node] = True
            if matching[other_node] is not None or is_estentable(matching[other_node]):
                matching[other_node] = p
                return True
    return False

def add_edge(u: int, v: int) -> None:
    pre[n_edge] = last[u]
    last[u] = n_edge
    other[n_edge] = v

for _ in range(m):
    u, v = read()
    add_edge(u, v)

for i in range(n):
    if is_extentable(i):
        visited = [False] * n
        n_matching += 1

print(f'#matching: {n_matching}')
for v, u in sorted(zip(range(n), matching), key = lambda x: x[1], reverse=True):
    print(f'{u} -> {v}')
```

这篇最初是2009年9月3日写的，当时是正在准备高三最后一次竞赛，打算把关于竞赛所有学到的东西都写下来但是没有时间了。今年（2022）年年底又翻了出来，完善了一些注释，新写了邻接表的实现，修正了时间复杂度的表达方式（当然Pascal实现里面的一些小错误为了保持原汁原味我还是没有修改的:P）。回首往事如云卷云舒，感慨万千不知所言。