import pwd
wallpapers="/home/dojo_ctf/wallpaper"
dict =['Desktop','wallpaper','Downloads','Pictures','PycharmProjects','Videos', 'Documents','Music','Public','Templates','VirtualBox VMs']
print("check user[...]")
from adduser.user import createUser 
from adduser.files import files
from diretorios_config.dir import wallpaper_dir
def check(user):
    try:
        pwd.getpwnam(user)
        print(user+" ok")
    except Exception:
        print(user+" nao exite [-]")
        print("criando user "+user+" [+]")
        createUser(user,user,"dojo_hacking")
        files(dict)
        wallpaper_dir(wallpapers)


