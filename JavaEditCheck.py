import urllib.request
import hashlib
def JavaEditCheck():
    print('''
       oooo
       `888
        888  .oooo.   oooo    ooo  .oooo.
        888 `P  )88b   `88.  .8'  `P  )88b
        888  .oP"888    `88..8'    .oP"888
        888 d8(  888     `888'    d8(  888
    .o. 88P `Y888""8o     `8'     `Y888""8o
    `Y888P


    oooooooooooo       .o8   o8o      .
    `888'     `8      "888   `"'    .o8
     888          .oooo888  oooo  .o888oo
     888oooo8    d88' `888  `888    888
     888    "    888   888   888    888
     888       o 888   888   888    888 .
    o888ooooood8 `Y8bod88P" o888o   "888"\n
                                by nestyk\n\n\n\n''')



    
    sha256v = urllib.request.urlopen("https://textbin.net/raw/g57tt6thai").read().decode("utf-8").strip()

    lines = sha256v.split("\n")

    versione = "" 
    fakeversion = "0ptiFine"
    filename = input("Enter the jar(version) with his path: ")
    if '"' in filename:
        filename = filename[1:-1]
    sha256_hash = hashlib.sha256()

    for line in lines:
        f = line.split("§")
        if f[0] in filename:
            sha256versione = f[1]
            
    with open(filename,"rb") as f:
        
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)

    if sha256versione.strip()  == sha256_hash.hexdigest():
        print("Legit")
    else:
        print("Java Edit Found.")
        print(f"Version Current using has this hash: {sha256_hash.hexdigest()}")
        print(f"Legit Version has this hash: {sha256versione.strip()}")


JavaEditCheck()
print("This code is public on https://github.com/nestyk/JavaEditCheck/")
print("Press enter to exit.")
input()
