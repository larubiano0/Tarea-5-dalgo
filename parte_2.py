import sys
from timeit import default_timer


class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


class UndirectedGraph():
    def __init__(self):
        self.V = set()
        self.E = set()

    def add_vertex(self, v):
        self.V.add(v)

    def add_edge(self, v1, v2, w):
        if ((v2, v1) not in self.E):
            self.E.add((v1, v2))

    def add_row(self, row, i):
        for j, w in enumerate(row):
            if w != '-1':
                self.add_edge(i, j, int(w))

    def adjacent(self, v):
        adj = set()
        for e in self.E:
            if e[0] == v:
                adj.add(e[1])
            elif e[1] == v:
                adj.add(e[0])
        return adj

    def bfs_for_connected_components(self):
        visited = set()
        connected_components = list()
        queue = Queue()
        for i in self.V:
            if i not in visited:
                queue.enqueue(i)
                visited.add(i)
                connected_component = set()
                while not queue.is_empty():
                    v = queue.dequeue()
                    connected_component.add(v)
                    for adj in self.adjacent(v):
                        if adj not in visited:
                            queue.enqueue(adj)
                            visited.add(adj)
                connected_components.append(connected_component)
        return connected_components

    def __str__(self):
        return f"V: {self.V}, E: {self.E}"

    def __repr__(self):
        return f"V: {self.V}, E: {self.E}"


def main():
    graph = UndirectedGraph()

    i = 0
    while True:  # Crea estructua de datos de tipo grafo
        row = sys.stdin.readline()
        row_list = row.split()

        if row_list == []:
            break

        graph.add_row(row_list, i)
        graph.add_vertex(i)
        i += 1

    t_0 = default_timer()

    connected_components = graph.bfs_for_connected_components()

    t_1 = default_timer()

    print(f"BFS tomó: {(t_1-t_0):.9f} s")

    print(f"Componentes conexas: {len(connected_components)}")

    text_file = open('results_2.txt', 'wt')
    text_file.write('{' + str(connected_components)[1:-1] + '}')
    text_file.close()

    print('Se ha creado el archivo results_2.txt con los resultados')


if __name__ == "__main__":
    main()
