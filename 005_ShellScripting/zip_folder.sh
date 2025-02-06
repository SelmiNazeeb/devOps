#!/bin/bash
#author : selmi
#purpose : zip  and unzip a folder
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


### unzip ###

echo "Enter the zip file name (with .zip extension)"
read -r zipfile
if [ -f "$zipfile" ]; then
    echo "zip file exists"
    unzip "$zipfile" -d "${zipfile%.zip}"
    echo "folder unzipped"
else
    echo "zip file does not exist"
fi