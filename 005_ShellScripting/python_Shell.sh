
#/bin/sh
#author : selmi
#purpose : print a message using function call
#usage : ./python_Shell.sh

print(){
    #local message=$1
    echo "message passed : $message"
}
echo "enter the message u want to print"
read -r message
print "$message"


## write a shell script to pass the directry and we have to find size of the directry ##

echo "please enter directory path"
read -r directory
du -h $directory        #print size with path
##################
du -h $directory | cut -f1      #prints only the size like cut the string and return first part only 
##################
du -h $directory | awk '{print $1}'     #same as cut

#output

please enter directory path
   C:\Users\291059\shell/shell_Questions
11K     C:\Users\291059\shell/shell_Questions
11K
11K


### write a shell script to find hardware information  ###

echo "host name : $(hostname)"
echo "cpu info : $(lscpu)" #another command cat /proc/cpuinfo
echo "hardisk info : $(lshw)" 
echo "memory info : $(free -h)" #another command cat /proc/meminfo
echo "disk info : $(df -h)"  #another commands lsblk,diskinfo
echo "network info : $(ifconfig)" #another command ip addr
echo "os version : $(cat /etc/os-release)" 
echo "kernel version : $(uname -r)" #another command cat /proc/version


