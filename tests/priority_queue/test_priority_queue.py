from ting_file_management.priority_queue import PriorityQueue
import pytest

mock = [
    {
        "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            "Estratégias em um",
            "mundo",
            "paralelo",
            "aqui",
            "e agora",
        ],
    },
    {
        "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [
            "Estratégias em um",
            "mundo",
        ],
    },
    {
        "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": [
            "Estratégias em um",
            "mundo",
            "paralelo",
            "aqui",
            "e agora",
            "aqui",
            "e agora",
            "aqui",
            "e agora",
            "aqui",
        ],
    },
    {
        "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["Estratégias em um", "mundo", "melhor"],
    },
]

mock_receives_regular_priority = [
    {
        "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [
            "Estratégias em um",
            "mundo",
            "paralelo",
            "aqui",
            "e agora",
        ],
    },
    {
        "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": [
            "Estratégias em um",
            "mundo",
            "paralelo",
            "aqui",
            "e agora",
            "aqui",
            "e agora",
            "aqui",
            "e agora",
            "aqui",
        ],
    },
]

mock_search = {
    "nome_do_arquivo": "statics/novo_paradigma_globalizado-min.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ["Estratégias em um", "mundo", "melhor"],
}


mock_receives_dequeue = [
    {
        "qtd_linhas": 5,
    },
    {
        "qtd_linhas": 10,
        "linhas_do_arquivo": [
            "Estratégias em um",
            "mundo",
            "paralelo",
            "aqui",
            "e agora",
            "aqui",
            "e agora",
            "aqui",
            "e agora",
            "aqui",
        ],
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    data = priority_queue.regular_priority.data

    assert priority_queue.__len__() == 0

    for item in mock:
        priority_queue.enqueue(item)

    assert priority_queue.__len__() == 4

    assert data == mock_receives_regular_priority

    receives = priority_queue.search(1)

    print(receives)
    assert receives == mock_search

    # receives_search = priority_queue.search(-1)

    priority_queue.dequeue()

    assert priority_queue.__len__() == 3

    # print(len(data))

    with pytest.raises(IndexError):
        priority_queue.search(-1)
