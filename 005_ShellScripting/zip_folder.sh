#!/bin/bash
#author : selmi
#purpose : zip a folder
#usage : ./zip_folder.sh

echo "Enter the folder name"
read -r folder
if [ -d $folder ]; then
    echo "folder exists"
    zip -r "$folder.zip" "$folder"
    echo "folder zipped"
else
    echo "folder doesnot exists"
fi 