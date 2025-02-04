#/bin/sh
#author : selmi
#purpose : learning backup
#usage : ./backup.sh

function backup {
    echo "enter the file name"
    read -r myfile
    # if [ -f $myfile ]; then
    #     echo "file exists"
    #     cp $myfile /tmp/backupp.sh
    # else
        echo "file not exists"
    # fi
    cp $myfile /tmp/backupp.sh
    #echo $?
    if [ $? -ne 0 ]; then
        echo "backup failed "
    fi
    }
    backup 