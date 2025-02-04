#/bin/sh
#author : selmi
#purpose : learning basic command
#usage : ./linuxinshell.sh

echo "I am $USERNAME. $USERNAME is a tiger"
echo "my current working directory is `pwd`"
echo "`whoami`"
echo "`date`"
ls

echo "--------------------------------"
command="ls -ltr /etc"
echo "$command"
eval $command
