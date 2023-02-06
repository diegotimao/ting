from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    notice = txt_importer(path_file)

    for item in instance.data:
        if path_file in item["nome_do_arquivo"]:
            return None

    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(notice),
        "linhas_do_arquivo": notice,
    }

    instance.enqueue(file)

    return sys.stdout.write(str(file))


def remove(instance):
    size = instance.__len__()

    if size > 0:
        data_path = instance.dequeue()["nome_do_arquivo"]
        return sys.stdout.write(f"Arquivo {data_path} removido com sucesso\n")
    else:
        return sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
