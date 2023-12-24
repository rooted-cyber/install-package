chs() {
cd ~/Termux-Ubuntu/*/ins*e
if [ -e sort ];then
cp -rf ~/Termux-Ubuntu/*/ins*pa*/sort/* /bin
else
cd ~/Termux-Ubuntu/Ultroid
git clone https://github.com/rooted-cyber/install-package
cp -rf ~/Termux-Ubuntu/*/ins*pa*/sort/* /bin
fi
}
prf() {
cd /bin
for b in a ap p3 pi3 pr3 g w y;do
chmod 755 $b
sudo chmod 755 $b
done
}
prm() {
cd /bin
if [ -e a ];then
prf
else
chs
fi
}
prm
prf
