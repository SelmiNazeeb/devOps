#/bin/sh
#author : selmi
#purpose : learning 
#usage : ./task.sh


current_hour=$(date +%H)
if [ "$current_hour" -ge 9 ] && [ $current_hour -lt 12 ] ; then
    echo "Good morning"
elif [ "$current_hour" -ge 12 ] && [ "$current_hour" -lt 16 ]; then
    echo "Good afternoon"
elif [ "$current_hour" -ge 16 ] && [ "$current_hour" -lt 20 ]; then
    echo "Good evening"
else 
    echo "Good night"
fi

