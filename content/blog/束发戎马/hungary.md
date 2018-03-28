Title: 听ghost讲那匈牙利算法的事情
Date:  2009-9-3
Tas:   NOIP, 匈牙利算法, 算法, 二分图匹配

具体的不用解释了吧，就是匈牙利算法，粘在这里只是为了防止自己电脑数据异常丢失……

这是百度百科上匈牙利算法的pascal原版程序，只是该了改格式而已。百度上的是用邻接矩阵写的，以后有空了我会写一个邻接表版本的匈牙利算法，矩阵版的时间复杂度为点个数的三次方，邻接表则变成了边的个数乘以点的个数，也不是很难写，应该最近就能完成。

    :::pascal
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
