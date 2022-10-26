import getpass
import pyAesCrypt
import os
import keyring

bufferSize = 64 * 1024

arquivo = input('Escolha o caminho do arquivo: ')
nome_rede = input('\nDigite o nome de rede: ')
usuario = input('\nDigite o usuario: ')
password = getpass.getpass('\nDigite a Senha:')

with open(arquivo, "rb") as fIn:
 with open(arquivo + ".enc" , "wb") as fOut:
   pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
   
os.remove(arquivo)

keyring.set_password(nome_rede,usuario,password)