import sys

# from ting_file_management.queue import Queue
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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# if __name__ == "__main__":
#     list_1 = Queue()
#     file = "arquivo_teste.txt"
#     caminho = (
#         f"C:/Users/andre/GitHub/trybe/sd-025-b-project-ting/statics/{file}"
#     )

#     for i in range(4):
#         process(caminho, list_1)
#         print(f"Tamanho da lista na execução[{i}]: {len(list_1)}")
