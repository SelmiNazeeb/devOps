#/bin/sh
#author : selmi
#purpose : pallindrome
#usage : ./pallindrome.sh

echo "Enter the string"
read -r String
rev_string=$(echo "$String" | rev)
if [ "$String" == "$rev_string"]; then
    echo "pallindrome"
else
    echo "Not pallindrome"
fi