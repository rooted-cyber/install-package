pentt() {
echo "️️"
echo "️️"
echo "️️"
echo "️️"
}
fix() {
apt install --fix-broken -y
}
app() {
apt update
apt upgrade -y
fix
for a in wget python3-pip python3 ffmpeg neofetch mediainfo;do
pentt
printf "Installing $a"
echo
#apt install  $a -y
pentt
fix
done
pip install --upgrade pip
wget -O req.txt https://github.com/TeamUltroid/Ultroid/raw/main/requirements.txt
wget -O reqq.txt https://github.com/TeamUltroid/Ultroid/raw/main/requirements.txt
#pip3 install -r req*
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
