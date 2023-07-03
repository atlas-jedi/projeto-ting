import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()

    element1 = {"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 5}
    element2 = {"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3}
    element3 = {"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 4}
    element4 = {"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10}

    queue.enqueue(element1)
    queue.enqueue(element2)
    queue.enqueue(element3)
    queue.enqueue(element4)

    assert len(queue) == 4
    assert queue.dequeue() == element2
    assert queue.search(0) == element3
    with pytest.raises(IndexError):
        queue.search(666)
