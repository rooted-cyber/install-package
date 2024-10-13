from os import chdir as cd, getcwd as pwd, chmod as ch, listdir as ls
from shutil import copy as cp, unpack_archive as un
import git as g

def prf():
  file = ["a","ap","p3","pi3","pr3","g","w","y"]
  for b in file:
    cd("/bin")
    ch(b,755)



def chs():
  if "sort":
    un("install-package/sort/sh.zip","/bin")
    prf()
  else:
    g.Git("/root").clone("https://github.com/rooted-cyber/install-package")
    un("install-package/sort/sh.zip","/bin")
    prf()

def chi():
  if "install-package":
    un("install-package/sort/sh.zip","/bin")
    prf()
  else:
    chs()


chi()
if "p3" in ls("/bin"):
  print("Successfully added\n")
else:
  print("Not add")
