from queue import Queue


def exists_word(word, instance: Queue):
    matching_files = []

    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = []
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": i + 1})

        if occurrences:
            matching_files.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return matching_files


def search_by_word(word, instance):
    matching_files = []

    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = []
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": i + 1, "conteudo": line})

        if occurrences:
            matching_files.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return matching_files

