#/bin/sh
#author : selmi
#purpose : extract email from the text file
#usage : ./mail.sh

echo "Enter the file "
read -r myfile
if [[ -f "$myfile" ]]; then
    grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}' "$myfile"
else
    echo "file not exists"
fi