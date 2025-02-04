#/bin/sh
#author : selmi
#purpose : learning regular expression
#usage : ./regular_expression.sh

numString="Aabc"
if [[ $numString =~ ^[1] ]]; then 
# =~ - operator used for regular expression matching in Bash. 
#The caret (^) means "start of the string,so ^1 matches any string that starts with the digit 1.
    echo "$numString starts with 1 present in string"
fi
#check if the string stored in $numString starts with either 1, ., or 7
if [[ $numString =~ ^[1.7] ]]; then 
    echo "$numString starts with 1 and 7 present in string"
fi
#matches if the first character is any of those.
if [[ $numString =~ ^[1.*9] ]]; then 
    echo "$numString starts with 1 and 9 present in string"
fi
#This is a character class that matches any one character,upper or lower case.
# + - This means must have "one or more" of the characters defined by the character class.
# $ - must end after these valid characters
#string must not contain any other characters like spaces,numbers,symbols
if [[ $numString =~ ^[A-Za-z]+$ ]]; then 
    echo "the letter in $numString starts with a and b present in string"
fi


