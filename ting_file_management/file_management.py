import os
import sys


def txt_importer(path_file):
    try:
        arquivo, extensao = os.path.splitext(path_file)
        list_notice = []
        if not extensao == ".txt":
            return sys.stderr.write("Formato inválido\n")

        with open(path_file, "r") as file:
            for linha in file:
                notice = linha.split("\n")
                list_notice.append(notice[0])
            return list_notice
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
