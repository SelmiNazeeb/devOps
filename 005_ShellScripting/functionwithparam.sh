#/bin/sh
#author : selmi
#purpose : learning funtion with parameter
#usage : ./functionwithparam.sh

function sum {
    local total=$(( $1 + $2 ))
    echo "$total"
}
result=$( sum 5 8 )
echo "The result returned is $result"