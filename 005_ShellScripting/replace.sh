#/bin/sh
#author : selmi
#purpose : replace a word with another
#usage : ./replace.sh

echo "Enter the file to changed "
read -r myfile
echo "Enter the word to changed "
read -r old
echo "Enter the new word "
read -r new
sed -i "s/$old/$new/g" $myfile
