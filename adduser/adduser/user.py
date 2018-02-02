import os
import crypt
def createUser(name, username, password):
    encPass = crypt.crypt(password, "22")
    try:
        os.system("useradd -p " + encPass + " -s " + "/bin/bash " + "-d " + "/home/" + username + " -m " + " -c \"" + name + "\" " + username)
        d = ['adm','audio','floppy','log','network','rfkill','scanner','storage','optical','power','wheel']
        for i in d:
            os.system('useradd -m -p "" -g dojo_ctf -G "adm,audio,floppy,log,network,rfkill,scanner,storage,optical,power,wheel" -s /usr/bin/zsh  %s'% username)
    except Exception:
        print("falta de permisao")