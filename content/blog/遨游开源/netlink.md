title:使用netlink与内核通信时发现的问题记录 
date: 2012-5-14
tags: 信息安全竞赛, netlink, linux, troubleshooting, 笔记
##1
kernel部分的netlink_kernel_create()函数第一个参数是net类型的一个结构体指针，这个结构指的是网络设备，一般情况下应该设为&init_net
##2
netlink使用新类型的时候要用一下MODULE_ALIAS_NET_PF_PROTO(family,protoco)宏函数来注册新类型（我用的是17号类型）
##3
内核的对skb操作部分最好用互斥锁lock一下，以防篡改
