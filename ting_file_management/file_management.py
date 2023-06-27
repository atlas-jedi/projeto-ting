import sys


def txt_importer(path_file: str):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
            return None

        with open(path_file, "r", encoding="utf-8") as file:
            file_data = file.readlines()
            return [line.strip() for line in file_data]

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
