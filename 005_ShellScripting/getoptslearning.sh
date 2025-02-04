#/bin/sh
#author : selmi
#purpose : learning getopts
#usage : ./lgetoptslearning.sh

while getopts :a:b: flag;do
     case $flag in 
        a) ab=$OPTARG;;
        b) bc=$OPTARG;;
        ?) echo "I dont understand this value"
     esac
done
    echo "first value $ab, second value $bc"