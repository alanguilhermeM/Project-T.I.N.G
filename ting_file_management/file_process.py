from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    dic = {}
    linhas = txt_importer(path_file)

    for item in instance.queue:
        if path_file == item["nome_do_arquivo"]:
            return None

    dic["nome_do_arquivo"] = path_file
    dic["qtd_linhas"] = len(linhas)
    dic["linhas_do_arquivo"] = linhas

    instance.enqueue(dic)
    print(dic)


# instance = Queue()
# path = 'statics/arquivo_teste.txt'
# process(path, instance)


def remove(instance):
    if len(instance.queue) <= 0:
        print("Não há elementos")
        return None

    removed = instance.dequeue()
    print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or len(instance) <= position:
        sys.stderr.write('Posição inválida')
        return None
    print(instance.search(position))
