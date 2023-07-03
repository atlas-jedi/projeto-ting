import sys
from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: AbstractQueue):
    already_exists = False
    imported_file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(imported_file),
        "linhas_do_arquivo": imported_file,
    }

    if len(instance) > 0:
        for index in range(len(instance)):
            file = instance.search(index)
            if file["nome_do_arquivo"] == path_file:
                already_exists = True

    if already_exists is False:
        instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance: AbstractQueue):
    result = None
    if len(instance) == 0:
        result = "Não há elementos"
    else:
        path_file = instance.search(0)["nome_do_arquivo"]
        result = f"Arquivo {path_file} removido com sucesso"
        instance.dequeue()
    print(result, file=sys.stdout)


def file_metadata(instance: AbstractQueue, position: int):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
