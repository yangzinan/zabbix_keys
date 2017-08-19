#!/bin/bash
#create by: DaGuanRen
#参数位端口号
#-A INPUT -p tcp -m tcp --dport $1 -j ACCEPT--添加iptables规则

recv=$(iptables -L -v -n -x | grep dpt:$1 | awk -F ' ' {'print $2'})
echo $recv

send=$(iptables -L -v -n -x | grep spt:$1 | awk -F ' ' {'print $2'})
echo "$send"

