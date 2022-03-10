import hashlib
import secrets
from getpass import getpass


def checkTrust():
    try:
        masterPasswordAttempt = 0
        while masterPasswordAttempt <= 2:
            masterPassword = getpass("\nVerify Yourself To Continue (Master Password)📌 : ")
            if verifyMasterPassword(masterPassword) == True:
                break
            else:
                print("\n❌ Nope, Try Again ❌")
                masterPasswordAttempt += 1
        else:
            print("\n 👋👋👋👋👋👋👋👋👋 To Many Invalid Attempts!! Get Out 👉 👋👋👋👋👋👋👋👋👋\n")
            quit()
        return masterPassword
    except Exception as e:
        print("\n❌❌❌ ErRoR OcCuRrEd 👉 Can't Verify The Trust Level ❌❌❌")
        print("\n 👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋\n")
        exit()


def verifyMasterPassword(masterPassword):
    with open("Password_Manager/User/masterlevel/00003.1.SALT.bin", "rb") as saltFile:
        salt = saltFile.read()
    with open("Password_Manager/User/masterlevel/00003.1.KEY.bin", "rb") as keyFile:
        key = keyFile.read()

    new_key = hashlib.pbkdf2_hmac('sha256', masterPassword.encode('utf-8'), salt, 150000, dklen=128)
    trust = secrets.compare_digest(key, new_key)
    return trust