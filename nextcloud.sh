#!/bin/sh

# yum -y update
# cd /var/lib/dpkg/info
# rm -rf *
sudo apt-get -y update
sudo apt-get -y
sudo apt-get -y install nginx
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install
sudo apt-get -y install php7.0-fpm php-mysql
cd /usr/share/nginx/html
rm -rf *
wget -qO-  https://download.nextcloud.com/server/installer/setup-nextcloud.php | php
