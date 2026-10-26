"""Exercício 08 — Remover duplicatas de uma lista encadeada.

Resolvido: percorra a lista uma vez, guarde os valores já vistos e remova
repetições sem alterar a ordem da primeira ocorrência.
Complexidade: O(n) de tempo e O(n) de espaço adicional.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_duplicates(self):
        seen = set()
        previous = None
        current = self.head

        while current is not None:
            if current.value in seen:
                previous.next = current.next
            else:
                seen.add(current.value)
                previous = current
            current = current.next

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


if __name__ == "__main__":
    linked_list = LinkedList()
    for number in [4, 2, 4, 3, 2, 1, 3]:
        linked_list.append(number)

    print("Antes: ", linked_list.to_list())
    linked_list.remove_duplicates()
    print("Depois:", linked_list.to_list())