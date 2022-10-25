import sys
from timeit import default_timer


class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


class Graph():
    def __init__(self):
        self.V = set()
        self.E = set()

    def add_vertex(self, v):
        self.V.add(v)

    def add_edge(self, v1, v2):
        self.E.add((v1, v2))

    def add_row(self, row, i):
        for j, w in enumerate(row):
            if w != '0' and w != '-1':
                self.add_edge(i, j)

    def adjacent(self, v):
        return [u for u in self.V if (v, u) in self.E]

    def dfs(self, v, visited, stack):
        visited.add(v)
        stack.push(v)
        for v in self.adjacent(v):
            if v not in visited:
                if self.dfs(v, visited, stack):
                    return True
            elif v in stack.items:
                return True
        stack.pop()
        return False

    def cycle_detection(self):
        visited = set()
        stack = Stack()
        for v in self.V:
            if v not in visited:
                if self.dfs(v, visited, stack):
                    return True
        return False

    def __str__(self):
        return f"V: {self.V}, E: {self.E}"

    def __repr__(self):
        return f"V: {self.V}, E: {self.E}"


def main():
    graph = Graph()

    i = 0
    while True:
        row = sys.stdin.readline()
        row_list = row.split()

        if row_list == []:
            break

        graph.add_row(row_list, i)
        graph.add_vertex(i)
        i += 1

    t_0 = default_timer()

    if graph.cycle_detection():
        print('Existe por lo menos un ciclo en el grafo')
    else:
        print('No existe ningún ciclo en el grafo')

    t_1 = default_timer()

    print(f"DFS tomó: {(t_1-t_0):.9f} s")


if __name__ == "__main__":
    main()
