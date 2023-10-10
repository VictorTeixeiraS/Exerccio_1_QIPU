## Resolução para o primeiro exercicio sobre listas ligadas para a posição de Estágio Desenvolvimento de Software

### `class LinkedListNode(object)`

Essa classe define um nó individual da lista ligada. Cada nó contém um valor e uma referência para o próximo nó.

- `__init__(self, value, next=None)`: Construtor do nó da lista ligada. Ele recebe um valor (obrigatório) e uma referência ao próximo nó (opcional).
- `value`: Propriedade que retorna o valor do nó atual.
- `next`: Propriedade que retorna o próximo nó.
- `next(self, node)`: Método que define o próximo nó.
- `hasNext(self)`: Método que retorna True se houver um próximo nó, False caso contrário.

### `class LinkedList(object)`

Essa classe representa a lista ligada, composta por vários nós.

- `__init__(self)`: Construtor da lista ligada. Inicializa uma lista vazia.
- `__len__(self)`: Método especial que retorna o número de elementos na lista.
- `head`: Propriedade que retorna o valor do primeiro nó da lista ligada.
- `tail`: Propriedade que retorna o valor do último nó da lista ligada.
- `append(self, value)`: Método que insere um novo nó no FINAL da lista ligada com o valor especificado.
- `insert(self, value)`: Método que insere um novo nó no INÍCIO da lista ligada com o valor especificado.
- `removeFirst(self)`: Método que remove o primeiro elemento da lista e retorna o seu valor.
- `getValueAt(self, index)`: Método que retorna o valor de um nó na posição especificada pelo índice. Se o índice for maior do que o tamanho da lista, uma exceção `OutOfBoundsException` é lançada.
- `toList(self)`: Método que retorna uma representação da lista ligada em forma de lista Python.

### `class OutOfBoundsException(Exception)`

Essa classe define uma exceção personalizada, chamada `OutOfBoundsException`, que é lançada quando uma operação fora dos limites da lista é detectada.



### `Referencia`

[Geeks4Geeks](https://www.geeksforgeeks.org/python-linked-list/)
