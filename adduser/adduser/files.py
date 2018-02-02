import os.path
def files(files):
    for i in files:
        if os.path.isdir("/home/dojo_ctf") == True:
            try:
                os.mkdir("/home/dojo_ctf/%s"%i)
                print("criando diretorio %s [+]" %i)
            except FileExistsError:
                pass
        else:
            print("saida")