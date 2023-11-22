import urllib.request
import hashlib

def check_minecraft_version():
    print('''
       github.com/nestyk.
       This Python code checks if a Minecraft Version is certified.
    ''')

    sha256_versions = urllib.request.urlopen("https://textbin.net/raw/g57tt6thai").read().decode("utf-8").strip()
    lines = sha256_versions.split("\n")

    filename = input("Enter the file path: ")

    if '"' in filename:
        filename = filename[1:-1]

    sha256_hash = hashlib.sha256()
    sha256_version = ""
    for line in lines:
        file_info = line.split("§")
        if file_info[0] in filename:
            sha256_version = file_info[1]
            break

    # Calcola l'hash del file locale
    with open(filename, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)

    # Confronta gli hash e fornisci l'esito della verifica
    if sha256_version.strip() == sha256_hash.hexdigest():
        print("Legit: Certified Minecraft Version.")
    else:
        print("Java Edit Found.")
        print(f"Current Version hash: {sha256_hash.hexdigest()}")
        print(f"Certified Version hash: {sha256_version.strip()}")


check_minecraft_version()

print("This code is public on https://github.com/nestyk/")
input("Press enter to exit.")
