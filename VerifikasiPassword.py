import re

pas = input("Masukkan password : ")

def verifikasi(pas):
    char = "[`~!@#$%^&*()_+-={}|:<>?\;',.]"

    if (len(pas) < 8):
        return False
    elif not re.search("[A-Z]", pas):
        return True
    elif not re.search(char, pas):
        return True

    else:
        return True


def password():
    if (verifikasi(pas) == True):
        print("True")
    else:
        print("False")

password()
