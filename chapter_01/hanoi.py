from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int, printt: bool = False, msg: str = None) -> None:

    if printt:
        print("tower_a = {}, tower_b = {}, tower_c = {}, n = {}, msg = {}".format(tower_a, tower_b, tower_c, n, msg))

    if n == 1:
        msg += " (base case) "
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1, printt, "begin->temp")
        hanoi(begin, end, temp, 1, printt, "begin->end")
        hanoi(temp, end, begin, n - 1, printt, "temp->end")


num_discs: int = 10
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs, True, "init.")
