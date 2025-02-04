#/bin/sh
#author : selmi
#purpose : average mark
#usage : ./mark.sh

echo "enter mark 1"
read -r a
echo "enter mark 2"
read -r b
echo "enter mark 3"
read -r c
if [ $a -lt 35 ] || [ $b -lt 35 ] || [ $c -lt 35 ]; then
    echo "failed"
else
        total=$((a + b + c))
        average=$(($total/3))
    if [ "$average" -ge 80 ]; then   # or $(((a + b + c)/3)) for average
        echo "distinction"
    elif [ "$average" -ge 60 ] && [ "$average" -lt 80 ]; then 
        echo "first class"
    else [ "$average" -lt 60 ] 
        echo "second class"
    fi 
fi

