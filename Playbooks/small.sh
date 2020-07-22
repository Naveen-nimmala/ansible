#!/bin/bash
GROUP_SER="[servers]"
LOCAL_SER="localhost"
echo $GROUP_SER
echo $LOCAL_SER
for ip in $(cat /ansible/text)
do
  echo $ip
done
