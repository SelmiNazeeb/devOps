#/bin/sh
#author : selmi
#purpose : count number of words in a string
#usage : ./count.sh

echo "Enter the string"
read -r String
counts=$(echo "$String" | wc -w) # wc -c is for count characters or "counts=$(wc -w <<< $String)"
echo "$counts"
