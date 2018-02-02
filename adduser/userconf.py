try:
    import  wget
except ImportError:
    print("instalando")
    from pip import main
    main(['install', "wget"])
from check.check import check

check("dojo_ctf")