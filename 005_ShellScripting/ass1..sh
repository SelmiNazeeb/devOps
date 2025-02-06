#!/bin/bash
#author : selmi
#purpose : check even or odd number
#usage : ./ass1.sh

echo "enter the number"
read -r number
if [ $((number % 2)) -eq 0 ]
then
    echo "even number"
else
    echo "odd number"
fi