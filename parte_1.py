import sys
from math import inf
from timeit import default_timer

class Graph():

    def __init__(self):
        self.V = set()
        self.E = set()
        self.c = dict()  # parejas laves:valor para cada arco (i,j) con su peso

    def add_vertex(self, v):
        self.V.add(v)

    def add_edge(self, v1, v2, w):
        self.E.add((v1, v2, w))
        self.c[(v1, v2)] = w

    def add_row(self, row, i):
        for j, w in enumerate(row):
            if w != '-1':
                self.add_edge(i, j, int(w))
            else:
                self.add_edge(i, j, inf)

    def dijkstra(self, source):
        A = {source}
        r = [self.c[(source, v)] if (source, v)
             in self.c else inf for v in self.V]  # Lista de distancias
        while A != self.V:
            w = source
            for u in self.V:
                if u not in A and ((w == source) or (r[u] < r[w])):
                    w = u
            A.add(w)
            for w, v, cost in self.E:
                if v not in A:
                    r[v] = min(r[v], r[w] + cost)
        return r

    def bellman_ford(self, source):
        r = [inf for _ in self.V]  # Lista de distancias
        r[source] = 0
        for _ in range(1, len(self.V) - 1):
            for w, v, cost in self.E:
                r[v] = min(r[v], r[w] + cost)
        return r

    def floyd_warshall(self):
        m = [[inf for _ in self.V] for _ in self.V]
        for i, j, cost in self.E:
            m[i][j] = cost
        i, j, k, n = int(), int(), 0, len(self.V)
        while k <= n:
            i = 0
            while i < n:
                j = 0
                while j < n:
                    if k == 0:
                        if (i, j) in self.c:
                            m[i][j] = self.c[(i, j)]
                        else:
                            m[i][j] = inf
                    else:
                        m[i][j] = min(m[i][j], m[i][k-1] + m[k-1][j])
                    j += 1
                i += 1
            k += 1
        return m

    def __str__(self):
        return f"V: {self.V}, E: {self.E}"

    def __repr__(self):
        return f"V: {self.V}, E: {self.E}"


def matrix_to_string(matrix):
    return '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix])


def main():
    graph = Graph()

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

    # Construcción de la matriz de costos mínimos para cada nodo usando Dijkstra
    min_cost_dijkstra = []
    for i in range(len(graph.V)):
        min_cost_dijkstra.append([j for j in graph.dijkstra(i)])

    t_1 = default_timer()

    # Construcción de la matriz de costos mínimos para cada nodo usando Bellman Ford
    min_cost_bellman_ford = []
    for i in range(len(graph.V)):
        min_cost_bellman_ford.append([j for j in graph.bellman_ford(i)])

    t_2 = default_timer()

    # Construcción de la matriz de costos mínimos para cada nodo usando Floyd Warshall
    min_cost_floyd_warshall = graph.floyd_warshall()
    min_cost_floyd_warshall = [[j for j in i]
                               for i in min_cost_floyd_warshall]

    t_3 = default_timer()

    print(f"Dijkstra tomó: {(t_1-t_0):.9f} s")
    print(f"Bellman Ford tomó: {(t_2-t_1):.9f} s")
    print(f"Floyd Warshall tomó: {(t_3-t_2):.9f} s")
    print(f"Tiempo total: {(t_3-t_0):.9f} s")

    s = ""
    s+='A continuación se muestra la matriz de costos mínimos para cada nodo usando cada uno de los algoritmos:' + '\n'*2
    s+='Dijkstra:' + '\n'
    s+=matrix_to_string(min_cost_dijkstra) + '\n'*2
    s+='Bellman Ford:' + '\n'
    s+=matrix_to_string(min_cost_bellman_ford) + '\n'*2
    s+='Floyd Warshall:' + '\n'
    s+=matrix_to_string(min_cost_floyd_warshall) + '\n'*2
    text_file = open("results.txt", "wt")
    text_file.write(s)
    text_file.close()

if __name__ == "__main__":
    main()
