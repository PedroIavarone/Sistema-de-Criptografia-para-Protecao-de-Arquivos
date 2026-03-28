import os, hashlib

from Crypto.Cipher import AES

from Crypto.Util.Padding import pad, unpad
 
# Parte 1: Entrada da senha

senha = input("Senha: ")

chave = hashlib.sha256(senha.encode()).digest()
 
# Menu

opcao = input("1-Criptografar  2-Descriptografar: ")

pasta = input("Pasta origem: ")

saida = input("Pasta destino: ")

os.makedirs(saida, exist_ok=True)
 
for nome in os.listdir(pasta):

    caminho = os.path.join(pasta, nome)

    if not os.path.isfile(caminho):

        continue
 
    with open(caminho, "rb") as f:

        dados = f.read()
 
    if opcao == "1":

        # Parte 2 e 3: Leitura + Criptografia AES

        iv = os.urandom(16)

        cifra = AES.new(chave, AES.MODE_CBC, iv)

        resultado = iv + cifra.encrypt(pad(dados, 16))

        destino = os.path.join(saida, nome + ".enc")

    else:

        # Parte 5: Descriptografia

        cifra = AES.new(chave, AES.MODE_CBC, dados[:16])

        resultado = unpad(cifra.decrypt(dados[16:]), 16)

        destino = os.path.join(saida, nome.replace(".enc", ""))
 
    # Parte 4: Salvamento na nova pasta

    with open(destino, "wb") as f:

        f.write(resultado)

    print(f"[OK] {nome}")
 
print("Concluído!")
 