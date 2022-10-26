import pyAesCrypt
from os import stat, remove
import keyring

bufferSize = 64 * 1024
arquivo = input('Escolha o caminho do arquivo: ')
nome_rede = input('\nDigite o nome de rede: ')
usuario = input('\nDigite o usuario: ')
password = keyring.get_password(nome_rede, usuario)

encFileSize = stat(arquivo + ".enc").st_size

with open(arquivo + ".enc", "rb") as fIn:
 try:
  with open(arquivo + ".txt", "wb") as fOut:
    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
 except:
    pass
