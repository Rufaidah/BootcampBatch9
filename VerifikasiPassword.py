import re

pas = input("Masukkan password : ")

def verifikasi(pas):
    char = "[`~!@#$%^&*()_+-={}|:<>?\;',.]"

    if (len(pas) < 8):
        return False
    elif re.search("[A-Z]",pas):
        return False
    elif re.search(char,pas):
        return False

    else:
        return True
    # elif re.match(r"^([\d]+)$",pas):
    #     return True

def password():
    if (verifikasi(pas) == True):
        print("True")
    else:
        print("False")

password()
