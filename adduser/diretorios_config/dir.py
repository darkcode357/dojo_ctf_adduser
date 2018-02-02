from os import system as sys
from os import chdir
from os import getcwd
wallpapers="/home/dojo_ctf/wallpaper"
urls = ['https://raw.githubusercontent.com/darkcode357/dojo_ctf/master/198967.jpg']

def wallpaper_dir(wallpaper_dir):
    if getcwd() != "/home/dojo_ctf/wallpaper":
        print("==> mudando de diretorio[+]")
        chdir(wallpapers)
        print(getcwd())
        donwload(urls)
    else:
        donwload(urls)
def donwload(url):
    print("baixando wallpaper")
    for i in urls:
        sys("wget %s /home/dojo_hacking/wallpaper/ " %i)


