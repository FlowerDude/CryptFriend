# CryptFriend is a small "passwordmanager" like tool
 
 Executing CryptFiend.py opens a dialog in which the user can choose between
- Encrypt
- Decrypt
- Decrypt into File

----
- Encrypt:
	- Will read the base.txt file and asks for a password encrypting the file base.txt removing it in the process, creating a "crypt" and "salt" file.
- Decrypt:
	- Will read the "crypt" and "salt" file and asks for a password decrypting the file printing the content into the console
- Decrypt into File
	- Will read the "crypt" and "salt" file and asks for a password decrypting the file printing the content into a file called "base.txt"
