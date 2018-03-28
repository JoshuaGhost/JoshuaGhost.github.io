title: metaexploit安装时问题解决
date: 2011-7-23
tags: metasploit, troubleshooting

metasploit 中文系统安装失败问题

windows中文系统在安装metasploit时会报postgresql错误，这是由于postgresql对中文支持问题导致。

解决方法：控制面板-区域和语言选项-将标准与格式，改为英语（美国），在安装即可

或可以安装metasploit framework的mini版，该版本不安装postgresql自然也无上述错误了。但无法使用GUI界面和一些相关功能
 
    :::log
    On 11/29/2010 11:21 PM, Yuping Li wrote: hi, guyswhen i was installing the metasploit framework 3.5 on XP, I come across with the following error message again and again.There has been an error. Unknown error while running C:\framework/postgresql/bin/psql.exe -U postgres -p 8448 -h localhost -c "ALTER USER postgresql PASSWORD '********'" The application will exit now. We have seen this on some non-english versions of the install - the cause is the default locale in PostgreSQL is not compatible with the SQL_ASCII statements. We need to override the installation locale of PostgreSQL to resolve this and have an open ticket to resolve it.-HD

[问题解答原文出处](http://seclists.org/metasploit/2010/q4/27)

转载自[此处](http://hi.baidu.com/heyiblog/blog/item/60edb9867413462d67096e59.html/cmtid/3303d1fc0402a88db901a02e)
