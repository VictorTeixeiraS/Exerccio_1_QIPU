class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """


    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
        """
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    @property
    def head(self): 
        if self._head:  
            return self._head.value 
        return None

    @property
    def tail(self):
        if self._tail:
            return self._tail.value
        return None

    def append(self, value):
        new_node = LinkedListNode(value) 
        if not self._head: 
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._len += 1 

    def insert(self, value):
        new_node = LinkedListNode(value, self._head)
        self._head = new_node
        if not self._tail:
            self._tail = new_node
        self._len += 1

    def removeFirst(self):
        if not self._head:
            raise OutOfBoundsException("The list is empty")
        value = self._head.value
        self._head = self._head.next
        self._len -= 1
        if not self._head:
            self._tail = None
        return value

    def getValueAt(self, index):
        if index < 0 or index >= self._len:
            raise OutOfBoundsException("Index out of bounds")
        current_node = self._head
        for i in range(index):
            current_node = current_node.next
        return current_node.value

    def toList(self):
        result = []
        current_node = self._head
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next
        return result


if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    ll = LinkedList()
    assert(ll.head is None)
    assert(ll.tail is None)
    assert(ll.toList() == [])
    ll.append(1)
    assert(ll.head == 1)
    assert(ll.tail == 1)
    assert(len(ll) == 1)
    assert(ll.toList() == [1])
    ll.append(2)
    assert(ll.head == 1)
    assert(ll.tail == 2)
    assert(len(ll) == 2)
    assert(ll.toList() == [1, 2])
    ll.append(3)
    assert(ll.head == 1)
    assert(ll.tail == 3)
    assert(len(ll) == 3)
    assert(ll.toList() == [1, 2, 3])
    ll.insert(0)
    assert(ll.head == 0)
    assert(ll.tail == 3)
    assert(len(ll) == 4)
    assert(ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert(ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == -1)
    assert(ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == 0)
    assert(ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert(v == 1)
    assert(ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert(v == 2)
    assert(ll.toList() == [3])
    v = ll.removeFirst()
    assert(v == 3)
    assert(ll.toList() == [])
    assert(len(ll) == 0)
    print("100%")
