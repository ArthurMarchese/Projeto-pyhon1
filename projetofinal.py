#importa os modulos 
#importa os módulos
import os
import shutil

#processamento
def criar_pasta(caminho):
    #verifica se existe uma pasta 
    if not os.path.exists(caminho):
        #cria a pasta
        os.makedirs(caminho)
        print(f"Pasta criada: {caminho}")
    else:
        print(f"A pasta já existe: {caminho}")

# Exemplo de uso
criar_pasta("documentos/planilhas")
criar_pasta("documentos/docs")


def criar_pasta(destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

def mover_arquivos(origem):
    origem = input("Digite o caminho completo da pasta de origem: ")

    # Defina os caminhos para as pastas específicas para cada tipo de arquivo
    destino_docs = "documentos/docs"  # Pasta para arquivos .doc e .docx
    destino_planilhas = "documentos/planilhas"  # Pasta para arquivos .xls e .xlsx

    # Verifica se a pasta de origem existe
    if os.path.exists(origem):
        # Cria as pastas de destino, se não existirem
        criar_pasta(destino_docs)
        criar_pasta(destino_planilhas)

        # Itera sobre os arquivos da pasta de origem
        for arquivo in os.listdir(origem):
            caminho_arquivo = os.path.join(origem, arquivo)

            # Verifica se é um arquivo e não uma subpasta
            if os.path.isfile(caminho_arquivo):
                # Se o arquivo for .doc ou .docx, move para a pasta 'documentos/docs'
                if arquivo.endswith('.doc') or arquivo.endswith('.docx'):
                    shutil.move(caminho_arquivo, destino_docs)
                    print(f"Arquivo movido para docs: {arquivo}")

                # Se o arquivo for .xls ou .xlsx, move para a pasta 'documentos/planilhas'
                elif arquivo.endswith('.xls') or arquivo.endswith('.xlsx'):
                    shutil.move(caminho_arquivo, destino_planilhas)
                    print(f"Arquivo movido para planilhas: {arquivo}")
    else:
        print(f"A pasta de origem não existe: {origem}")

# Mover arquivos da pasta 'documentos' para pastas específicas dependendo da extensão
mover_arquivos("documentos")
