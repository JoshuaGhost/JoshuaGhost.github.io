Title: 听ghost讲那kmp算法的事情
Date:  2009-9-3
Tags:  NOIP, 算法, KMP
传说中的kmp算法，快速模式匹配，程序源代码如下：

    :::pascal
    program match(input,output);
    var
        i,j,k,m,n:longint;
        t,s:string;
        p:array[1..255] of integer;

    procedure predeal(t:string);
    var
        i,j,q:longint;
    begin
        p[1]:=0;
        k:=0;
        for q:=2 to length(t) do begin
            while (k>0) and (t[k+1]<>t[q]) do k:=p[k];
            if t[k+1]=t[q] then inc(k);
            p[q]:=k;
        end;
    end;
    
    function kmp(t,s:string):integer;
    var
        i,j,k:longint;
    begin
        predeal(t);
        k:=0;
        for i:=1 to length(s) do begin
            while (k>0) and (t[k+1]<>s[i]) do k:=p[k];
            if t[k+1]=s[i] then begin
                inc(k);
                if k=length(t) then begin
                    exit(i-length(t)+1);
                    halt;
                end;
            end;
        end;
        exit(0);
    end;
    
    begin
        readln(t);
        readln(s);
        writeln(kmp(t,s));
    end.



普通的字符串匹配时间复杂度为目标串（以下用A串代替）长度乘以包含目标串的长串（以下用B串代替），而kmp算法则是这两个数相加，它的实现原理大致上是这样的：

##1.预处理过程

以A串为原型建立一个p数组，p［i］记录的是i这个位置的字符在它前缀串里的位置（我语言表达能力不是很好，让我们以串说话）

比如，A串为abcabcd，则p数组就应该是0001230，设两个指针q与k，q是for循环的循环变量，k则是初始值为0的一个标记。

一开始，q为1，k为零，A串中q位置上的字符为a，k＋1位置上的字符也为a，但是q等于1，所以不做任何改变；

接着，q等于2，k为0，A串q位置上的字符为b，k＋1位置上的字符为a，a<>b所以不做任何改动；

q等于3的时候同2；

然后，q等于4，这个时候k＋1位置上的字符是a，q位置上的字符也是a，两者相等，k加一等于1，p［q］赋值等于k，说明当前位置上前一个前序段是从1位置开始的。

之后，q等于5，这个时候k+1位置上的字符是b，q位置上的字符也是b，两者相等，k加一等于1，p［q］赋值等于k。

q等于6，类推。

q等于7的时候，k等于3，k＋1位置上的字符为a，q位置上的字符等于d，d<>a，所以k赋值等于q［k］，也就是0，此时k等于0，停止往前倒，k＋1位置上的字符等于a，a<>d，所以q［7］等于0

如果A串为abcabcabce，p数组就变成了0001234560，想一想这是为什么，A数组如果是abcdeabcffa呢？

建立p数组的过程就是整个预处理的最主要过程，到此预处理告一段落，开始进行正式模式匹配。

##2.模式匹配

阿，今天还有事，以后有空再写吧，语言还得组织组织，俄嫩，走了…………
