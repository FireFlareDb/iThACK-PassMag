from Password_Manager.User._user_db import create_database
from Password_Manager.User._master_encryption import passwordHasher
import os
import json
import subprocess

if __name__ == '__main__':
    configFolder = "Password_Manager/Config"
    if not os.path.exists(configFolder):
        os.mkdir(configFolder)

    configFile = "Password_Manager/config.json"
    if not os.path.exists(configFile):
        create_database()
        passwordHasher("don't use weak master password")

        data = {
            'Installation': True,
            'Automatic Backup': False,
            'Automatic Cloud Backup': False,
            'User Preferred Local Backup': False,
        }
        with open("Password_Manager/config.json", "w") as config_file:
            json.dump(data, config_file)
    else:
        with open("Password_Manager/config.json", "r") as config_file:
            isAutoBackupAllowed = json.load(config_file)['Installation']

        if isAutoBackupAllowed:
            print("\niThACK PassMag is already installed in your system.\n")
            exit()

    subprocess.check_call(['python', '-m', 'pip', 'install', '-r', 'requirements.txt'])

    print("\n🤞🤞🤞👌👌👌 Woo Hoo Installation Complete Successfully 🐱‍💻🐱‍🐉🐱‍🚀🎁🎏🔑\n")