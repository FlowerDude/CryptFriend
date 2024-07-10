import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import easygui
from tabulate import tabulate

wrkdir = os.path.dirname(os.path.realpath(__file__))

def encryptBase(password, salt):    
    saltFile = open(wrkdir+'\salt', 'wb')
    saltFile.write(salt)
    saltFile.close()

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length = 32, salt = salt, iterations=480000)
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    inpt = open(wrkdir+ '\\base.txt', 'rb')
    token = f.encrypt(inpt.read())
    inpt.close()
    
    output = open(wrkdir+'\crypt', 'wb')
    output.write(token)
    output.close()

    os.remove(wrkdir+ '\\base.txt')

def decryptBase(password):
    saltFile = open(wrkdir+'\salt', 'rb')
    salt = saltFile.read()
    saltFile.close()

    inpt = open(wrkdir + '\crypt', 'rb')
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length = 32, salt = salt, iterations=480000)
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    return f.decrypt(inpt.read())

sel = easygui.choicebox('De-/Encrypt', 'Start', ['Encrypt', 'Decrypt', 'DecryptToFile'])

if sel == 'Encrypt':
    salt = os.urandom(16)
    pwd = easygui.passwordbox('Encryption password', 'Encryption', 'droggelbecher')
    print('Encrypt new Document')
    encryptBase(pwd, salt)
    print('Done !')


if sel == 'Decrypt' or sel == 'DecryptToFile':
    pwd = easygui.passwordbox('Decryption password', 'Decryption', 'droggelbecher')
    print('Decrypt Document')
    output = decryptBase(pwd)
    if sel != 'DecryptToFile':
        txtOutput = output.decode()
        fineLines = []
        for line in txtOutput.splitlines():
            fineLines.append(line.split(';'))
        header = fineLines.pop(0)
        print(tabulate(fineLines, headers=header, tablefmt="pretty"))
    else:
        basefile = open(wrkdir+ '\\base.txt', 'w')
        basefile.write(output.decode())
        basefile.close()        