#!/bin/bash
echo "Hello World"

sudo apt-get install unzip

pip3 install paramiko
pip3 install pyxhook
pip3 install plyer



echo $HOSTNAME
mkdir /home/$HOSTNAME/Desktop/lazy_pocketbook
cd /home/$HOSTNAME/Desktop/lazy_pocketbook

wget https://github.com/wloszynski/lazy-pocketbook-pc/raw/main/pb_jailbreak.zip

unzip pb_jailbreak.zip

rm -rd pb_jailbreak.zip
