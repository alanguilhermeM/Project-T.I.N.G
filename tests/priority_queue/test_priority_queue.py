from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    project = PriorityQueue()

    mock1 = {
        "qtd_linhas": 3
    }

    mock2 = {
        "qtd_linhas": 7
    }

    project.enqueue(mock2)
    assert len(project.regular_priority) == 1

    project.enqueue(mock1)
    assert len(project.high_priority) == 1

    assert project.search(0) == mock1
    assert project.dequeue() == mock1

    project.dequeue()
    assert len(project.regular_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        project.search(2)

    
