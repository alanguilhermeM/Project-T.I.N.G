import os
import sys


def txt_importer(path_file):
    if not os.path.exists(path_file):
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        return

    file_name, file_extension = os.path.splitext(path_file)

    if not file_extension == '.txt':
        sys.stderr.write('Formato inválido\n')
        return

    linhas_do_arquivo = []
    with open(path_file, "r") as arquivo:
        for linha in arquivo:
            linhas_do_arquivo.append(linha.strip())

    return linhas_do_arquivo
# print(txt_importer('statics/arquivo_teste.txt'))
