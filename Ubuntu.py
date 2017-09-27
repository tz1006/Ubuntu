# Initialize Shell For Ubuntu

sudo apt-get update

# 安装中文语言包
sudo apt-get -y install language-pack-zh-hans language-pack-zh-hans-base language-pack-gnome-zh-hans language-pack-gnome-zh-hans-base
sudo apt-get -y install `check-language-support -l zh`
sudo localectl set-locale LANG=zh_CN.UTF-8

# 安装系统组件
sudo apt-get -y install vim

# 安装python相关
sudo apt-get -y install python-pip python-pyside

pip install Ghost.py

sudo reboot

