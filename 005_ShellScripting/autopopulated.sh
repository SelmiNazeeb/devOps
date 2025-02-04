#/bin/sh
#author : selmi
#purpose : learning atopopulated commands
#usage : ./autopopulated.sh

echo "all the arguments combined together: $*"
echo "number of arguments: $#"
echo "first argument: $1"
echo "expands all the command line arguments as seperate words: $@"
echo "process id of the current process: $$"

sleep 400 & #running as a backround process
echo "process id of most recently backgrouded process:  $!"
echo "file name of current program: $0"

