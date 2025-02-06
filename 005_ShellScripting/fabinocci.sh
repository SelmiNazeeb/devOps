#!/bin/bash
#author : selmi
#purpose : fabinocci
#usage : ./fabinocci.sh

echo "enter the number"
read -r number
if [ $number -lt 0 ]
    then
    echo "syntax error"
    exit 1
fi
a=0
b=1
echo "Fibonacci Series is : "
echo $a
echo $b
for (( i=2; i<number; i++ )); do
    next=$((a + b))
    a=$b
    b=$next
    echo $next
done
