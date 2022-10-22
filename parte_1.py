import sys
from fractions import Fraction


class Graph():
    def __init__(self):
        self.V = set()
        self.E = set()

    def add_vertex(self, v):
        self.V.add(v)

    def add_edge(self, v1, v2, w):
        self.E.add((v1, v2, w))

    def add_row(self, row, i):
        for j, w in enumerate(row):
            if w != '0':
                self.add_edge(i, j, Fraction(w))

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


if __name__ == "__main__":
    main()
