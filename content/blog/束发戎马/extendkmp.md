Title: 扩展kmp
Date:  2009-10-28
Tags:  NOIP, 算法, KMP, Extended KMP 

教程的话……我理解了以后会发上来的……
    
    :::pascal
    program extended_kmp(input,output); 
    var 
        max,now,x,i,j,k,m,n,w:longint; 
        a,b:array[1..200001] of char; 
        f,p,ans:array[0..200000] of longint; 
    begin 
        assign(input,"str.in"); 
        assign(output,"str.out"); 
        reset(input); 
        rewrite(output); 
        readln(n,m,w); 
        for i:=1 to n do read(a[i]); 
        readln; 
        for i:=1 to m do read(b[i]); 
        readln; j:=0; 
        while b[1+j]=b[j+2] do inc(j); 
        p[2]:=j; 
        k:=2; 
        for i:=3 to m do begin 
            max:=k+p[k]-1; 
            now:=p[i-k+1]; 
            if now<max-i+1 then 
                p[i]:=now else begin 
                    if max-i+1>0 then 
                        j:=max-i+1 
                    else 
                        j:=0; 
                while b[i+j]=b[j+1] do inc(j); 
                p[i]:=j; 
                k:=i 
                end 
    end;

    begin
        j:=0; 
        while b[j+1]=a[j+1] do inc(j); 
        f[1]:=j; k:=1; 
        for i:=2 to n do begin 
            max:=k+f[k]-1; 
            now:=p[i-k+1]; 
            if now<max-i+1 then 
                f[i]:=now else begin 
                    if max-i+1>0 then 
                        j:=max-i+1 
                    else 
                        j:=0; 
                    while a[i+j]=b[j+1] do inc(j); 
                    f[i]:=j; 
                    k:=i 
                end 
        end; 
        for i:=1 to n do inc(ans[f[i]]); 
        for i:=1 to w do begin 
            read(x); 
            writeln(ans[x]) 
        end; 
        close(input); close(output) 
    end.
