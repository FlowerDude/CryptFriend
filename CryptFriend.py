import base64
import os
#from cryptography.fernet import InvalidToken
#from cryptography.fernet import Fernet
#from cryptography.hazmat.primitives import hashes
#from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import easygui
#from tabulate import tabulate
import string
import random

wrkdir = os.path.dirname(os.path.realpath(__file__))

class FiendishEntry:
    target = ''
    usr = ''
    pwd = ''

    def __init__(self, target, usr, pwd):
        self.target = target
        self.usr = usr
        self.pwd = pwd


def generatePW(length=32, specials=True):
    chrs = string.ascii_uppercase + string.ascii_lowercase + string.digits
    if specials:
        chrs += string.punctuation

    return ''.join(random.choice(chrs) for i in range(length))

if __name__ == '__main__':
    sel = easygui.buttonbox('Password Management', 'Start', ['Add', 'Show'])

    if sel == None:
        exit(0)

    if sel == 'Add':
        genOrAdd = easygui.buttonbox('Generate a Password or enter an existing?', 'Generate?', ['Generate', 'Add Existing'])
        if genOrAdd == 'Generate':
            length = easygui.integerbox('Password length','Length',upperbound=4096, lowerbound=1)
            if length == None:
                exit(0)
            specials = easygui.ynbox('Special characters?', 'Special')
            passw = generatePW(length, specials)
            print(passw)
            if not easygui.ynbox('Add to existing storage?', 'Store?'):
                exit(0)
            
            fields = ['Name', 'User']
            identification = easygui.multenterbox('Data', 'Data', fields,)
            mapping = dict(zip(fields, identification))
            name = mapping['Name']
            usr = mapping['User']
            newestEntry = FiendishEntry(name, usr, passw)



    if sel == 'Show':
        easygui.msgbox('''
              ';.
    .---.,       \ 
   {}-.__,>=======;==================
    `----'      ,/
fld           .;'
              ''')



















# def encryptBase(password, salt):    
#     saltFile = open(wrkdir+'\salt', 'wb')
#     saltFile.write(salt)
#     saltFile.close()

#     kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length = 32, salt = salt, iterations=480000)
#     key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
#     f = Fernet(key)
#     inpt = open(wrkdir+ '\\base.txt', 'rb')
#     token = f.encrypt(inpt.read())
#     inpt.close()
    
#     output = open(wrkdir+'\crypt', 'wb')
#     output.write(token)
#     output.close()

#     os.remove(wrkdir+ '\\base.txt')

# def decryptBase(password):
#     saltFile = open(wrkdir+'\salt', 'rb')
#     salt = saltFile.read()
#     saltFile.close()

#     inpt = open(wrkdir + '\crypt', 'rb')
#     kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length = 32, salt = salt, iterations=480000)
#     key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
#     f = Fernet(key)
#     try:
#         return f.decrypt(inpt.read())
#     except InvalidToken:
#         print('Wrong Password !')

# def gatherPwd():
#     pwd = easygui.passwordbox('Encryption password', 'Encryption', 'droggelbecher')
#     if pwd == None or pwd == '':
#         return None
#     pwd2 = easygui.passwordbox('Re-enter password', 'Encryption', 'droggelbecher')
#     if pwd == pwd2:
#         return pwd
#     easygui.msgbox('Password missmatch ! Retry', 'Missmatch !')
#     return gatherPwd()

# def decrypt():
#     pwd = easygui.passwordbox('Decryption password', 'Decryption', 'droggelbecher')
#     print('Decrypt Document')
#     return decryptBase(pwd)

# #def decryptedToCli(decrypted):
# #    txtOutput = decrypted.decode()
# #    fineLines = []
# #    for line in txtOutput.splitlines():
# #        fineLines.append(line.split(';'))
# #    header = fineLines.pop(0)
# #    print(tabulate(fineLines, headers=header, tablefmt="pretty"))


# def decryptedToFile(decrypted):
#     basefile = open(wrkdir+ '\\base.txt', 'w')
#     basefile.write(decrypted.decode())
#     basefile.close()        

# def addNewPassToStore(newPass):
#     easygui.textbox('Key for Pass', 'Key')

# if __name__ == '__main__':
#     sel = easygui.choicebox('De-/Encrypt', 'Start', ['Encrypt', 'DecryptToFile', 'Add Password', 'Show Passwords'])

#     if sel == 'Encrypt':
#         salt = os.urandom(16)
#         pwd = gatherPwd()
#         if pwd == None:
#             exit(0)
#         print('Encrypt new Document')
#         encryptBase(pwd, salt)
#         print('Done !')


#     if sel == 'DecryptToFile':
#         decrypted = decrypt()
#         if decrypted == None:
#             exit(0)
#         else:
#             decryptedToFile(decrypted)

#     if sel == 'Add Password':
#         easygui.choicebox('Generate a Password or enter an existing?', 'Generate?', ['Generate', 'Add'])
#         length = easygui.integerbox('Password length','Length',upperbound=4096, lowerbound=1)
#         if length == None:
#             exit(0)
#         specials = easygui.ynbox('Special characters?', 'Special')
#         passw = generatePW(length, specials)
#         print(passw)
#         if not easygui.ynbox('Add to existing storage?', 'Store?'):
#             exit(0)
#         identification = easygui.multenterbox('Data', 'Data', ['Name', 'User'],)
#         print(identification)



#         newestEntry = FiendishEntry(name, user, passw)
#         #addNewPassToStore()
#         #decryptedToFile(decrypt())

#     #toDo: add functionality to replace passwords