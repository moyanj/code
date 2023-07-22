command = "makecert.exe -sv root.pvk -ss {} -n 'CN={},E={},C={},S={}' -r root.cer".format(name,CAname,mail,country,city)
os.system(command)