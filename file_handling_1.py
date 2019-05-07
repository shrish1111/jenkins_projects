myfile=open("shrishchamoli.txt","w")
myfile.write("""This file is being created by,
using python scripts""")
myfile.close()
myfile=open("shrishchamoli.txt","a")
myfile.write("""This is new text""")
myfile.close()
myfile=open("shrishchamoli.txt","r")
print(myfile.read())
myfile.close()

