def exists_word(word, instance):
    data = instance.data
    list_words = []
    list_currencyes = []

    for item_data in data:
        for index, item in enumerate(item_data["linhas_do_arquivo"]):
            if word.lower() in item.lower():
                list_words.append({"linha": index + 1})

        if len(list_words) > 0:
            list_currencyes.append(
                {
                    "palavra": word,
                    "arquivo": item_data["nome_do_arquivo"],
                    "ocorrencias": list_words,
                }
            )
    return list_currencyes


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
