#!/bin/bash
db=$3
table=$4
req=$(mysql -u$1 -p$2 -e "show open tables" | grep $db | grep $table | awk -F ' ' '{print $3}')
echo $req
