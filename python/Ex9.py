"""Exercício 09 — Fila de prioridade com heap mínimo.

Resolvido: implemente inserção e remoção em um heap binário. A menor prioridade
numérica sai primeiro; em caso de empate, vale a ordem de chegada.
Complexidade: inserir/remover O(log n), consultar o próximo O(1).
"""

from typing import Any


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._next_order = 0

    def __len__(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0

    def enqueue(self, value: Any, priority: int):
        entry = (priority, self._next_order, value)
        self._next_order += 1
        self._heap.append(entry)
        self._sift_up(len(self._heap) - 1)

    def peek(self):
        if self.is_empty():
            raise IndexError("A fila de prioridade está vazia.")
        priority, _, value = self._heap[0]
        return priority, value

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila de prioridade está vazia.")

        first = self._heap[0]
        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            self._sift_down(0)

        priority, _, value = first
        return priority, value

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self._heap[parent] <= self._heap[index]:
                break
            self._heap[parent], self._heap[index] = (
                self._heap[index],
                self._heap[parent],
            )
            index = parent

    def _sift_down(self, index):
        size = len(self._heap)
        while True:
            left = 2 * index + 1
            right = left + 1
            smallest = index

            if left < size and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < size and self._heap[right] < self._heap[smallest]:
                smallest = right
            if smallest == index:
                break

            self._heap[index], self._heap[smallest] = (
                self._heap[smallest],
                self._heap[index],
            )
            index = smallest


if __name__ == "__main__":
    tasks = PriorityQueue()
    tasks.enqueue("Enviar trabalho", 2)
    tasks.enqueue("Atender emergência", 1)
    tasks.enqueue("Responder e-mail", 2)

    print("Próxima tarefa:", tasks.peek())
    while not tasks.is_empty():
        print("Executando:", tasks.dequeue())