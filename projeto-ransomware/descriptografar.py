from cryptography.fernet import Fernet
import os

# 3.1 Descriptografar um único arquivo
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    dados = f.decrypt(dados_encriptados)
    with open(arquivo, "wb") as file:
        file.write(dados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregar_chave()  # usa a chave original
    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)

    print("Arquivos restaurados com sucesso")

if _name_ == "_main_":
    main()
    