pentt() {
echo "️️"
echo "️️"
echo "️️"
echo "️️"
}
centt() {
echo "️️"
echo "️️"
echo "️️"
echo "️️"
}
fix() {
apt install --fix-broken -y
}
nfc() {
neofetch --stdout
cd ~
if [ -e .config ];then
cp ~/install*e/config* ~/.config/neofetch
fi
}
chcp() {
cd ~/install*e/plu
if [ -e pwd.py ];then
centt
printf "Founding all plugins"
centt
printf "Now copying all plugins"
centt
cp *py ~/install*e/Ultroid/plug*
ls ~/install*e/Ultroid/plug*
sleep 50
fi
}
pplf() {
centt
printf "Copying file or plugins"
centt
cd ~/install*e
if [ -e a.otf ];then
centt
printf "Founding all files"
centt
printf "Now copying"
centt
nfc
echo "hrllo,"
cd ~/install*e
cp -rf * ~/install*e/Ultroid/res*/dow*
ls ~/install*e/Ultroid/res*/dow*
crntt
ls ~/inst*
sleep 50
centt
cd ~/install*e/plu
chcp
else
centt
printf "Not found"
exit
fi
}
app() {
apt update
apt upgrade -y
fix
for a in wget python3-pip python3 ffmpeg neofetch mediainfo;do
pentt
cd /bin
if [ -e $a ];then
echo "already"
else
printf "Installing $a"
echo
apt install  $a -y
pentt
fi
fix
done
pip install --upgrade pip
for bb in yt-dlp telegraph aiohttp python-decouple requests;do
pentt
printf "Installing $a"
echo
pip3 uninstall $bb -y
pip3 install $bb
pentt
done
}
app
pplf
