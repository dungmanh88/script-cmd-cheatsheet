#!/bin/bash

if [ ! $UID -eq 0 ]; then
  echo "You must run as root or use sudo"
  exit 1
fi

read -p "Enter your username: " username
read -sp "Enter your password: " password
echo -e "\n"
read -p "Enter your public key: " key

if [ -z $username ]; then
  echo "You must enter username"
  exit 1
fi

if [ -z $password ]; then
  echo "You must enter password"
  exit 1
fi

if [ -z "$key" ]; then
  echo "You must enter key"
  exit 1
fi

if grep -Fq $username /etc/passwd
then
  echo "$username is exist"
  exit 1
fi

if ! useradd -p $(openssl passwd -1 $password) $username
then
  echo "Add $username failed"
  exit 2
fi

if ! groupadd admin
then
  echo "Add group admin failed"
fi

mkdir -p /home/$username/.ssh && \
echo $key >> /home/$username/.ssh/authorized_keys && \
chown -R $username:$username /home/$username/.ssh && \
chmod 700 /home/$username/.ssh && \
chmod 644 /home/$username/.ssh/authorized_keys

usermod -aG admin $username

if ! grep -Fq "%admin ALL=(ALL) ALL" /etc/sudoers
then
  echo "%admin ALL=(ALL) ALL" >> /etc/sudoers
fi
echo "DONE!"
