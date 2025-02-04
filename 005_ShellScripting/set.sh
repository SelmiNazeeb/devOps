#/bin/sh
#author : selmi
#purpose : learning atopopulated commands
#usage : ./set.sh

set `date`
set -x    #when you are troubleshooting(stuck),you need to know which line is to configure
echo "Today is $1"
echo "Month is $2"
echo "Date is $3"
echo "Year is $4"
echo "Time is $5"
echo "AM/PM is $6"
