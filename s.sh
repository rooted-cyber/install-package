chs() {
if [ -e sort ];then
sudo cp -rf ins*pa*/sort/* /bin
cp -rf ins*pa*/sort/* /bin
else
git clone https://github.com/rooted-cyber/install-package
sudo cp -rf ins*pa*/sort/* /bin
cp -rf ins*pa*/sort/* /bin
fi
}
chi() {
cd ~
if [ -e install-package ];then
sudo cp -rf ins*pa*/sort/* /bin
cp -rf ins*pa*/sort/* /bin
else
chs
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
chi
fi
}
chi
prm
prf
