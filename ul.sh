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
fi
}
pplf() {
cd ~/install*e
if [ -e a.otf ];then
nfc
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
echo "already installed $a"
else
printf "package Installing $a"
echo
apt install  $a -y
pentt
fix
fi
done

}
app
pplf
