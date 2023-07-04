from ting_file_management.abstract_queue import AbstractQueue


def exists_word(word: str, instance: AbstractQueue, show_content=False):
    word = word.lower()
    results = []

    for file in instance.data:
        file_name = file["nome_do_arquivo"]
        file_lines = file["linhas_do_arquivo"]

        ocurrences = [
            {"linha": j + 1, "conteudo": line}
            if show_content
            else {"linha": j + 1}
            for j, line in enumerate(file_lines)
            if word in line.lower()
        ]

        if ocurrences:
            results.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": ocurrences,
                }
            )

    return results


def search_by_word(word: str, instance: AbstractQueue):
    return exists_word(word, instance, show_content=True)
