#/bin/sh
#author : selmi
#purpose : convert string from lowercase to uppercase
#usage : ./uppercase.sh

echo "Enter the string"
read -r String
upper=$(echo "$String" | tr 'a-z' 'A-Z')
echo "$upper"