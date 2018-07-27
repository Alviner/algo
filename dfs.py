# -*- coding: utf-8 -*-

import stack
import simple_graph


class Vertex(simple_graph.Vertex):
    def __init__(self, value):
        self.hit = False
        self.value = value

    def set_visited(self):
        self.hit = True

    def set_unvisited(self):
        self.hit = False

    def is_visited(self):
        return self.hit

    def __repr__(self):
        return f'{self.value}'


class Graph(simple_graph.SimpleGraph):
    vertex_class = Vertex

    def __init__(self, max_vertex=0):
        super(Graph, self).__init__(max_vertex)
        self.stack = stack.Stack()

    def is_adjacent(self, first_vertex: Vertex, second_vertex: Vertex):
        index_first = self._get_index(first_vertex)
        second_index = self._get_index(second_vertex)

        if self.m_adjency[index_first][second_index] == 1:
            return True
        else:
            return False

    def get_adjacent(self, vertex: Vertex):
        res = []
        for other_vertex in self.vertex:
            if other_vertex != vertex and self.is_adjacent(vertex, other_vertex):
                res.append(other_vertex)
        return res

    def gfs(self, first_vertex: Vertex, second_vertex: Vertex):
        for vertex in self.vertex:
            vertex.set_unvisited()
        self.stack.stack = []

        current_vertex = first_vertex

        while current_vertex is not None:
            if not current_vertex.is_visited():
                self.stack.push(current_vertex)
                current_vertex.set_visited()

            adjacent = self.get_adjacent(current_vertex)
            if len(adjacent) == 0:
                self.stack.__init__()
                return self.stack

            if second_vertex in adjacent:
                self.stack.push(second_vertex)
                current_vertex = None
            else:
                for i, vertex in enumerate(adjacent):
                    if not vertex.is_visited():
                        current_vertex = vertex
                        break
                    if i == len(adjacent) - 1:
                        current_vertex = self.stack.pop()
                        if self.stack.size() == 0:
                            return self.stack
                        break
        return self.stack


def test_gfs():
    graph = Graph(0)

    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')

    graph.add_vertex(A)
    graph.add_vertex(B)
    graph.add_vertex(C)
    graph.add_vertex(D)
    graph.add_vertex(E)

    graph.add_rib(A, D)
    graph.add_rib(C, B)
    graph.add_rib(C, D)
    graph.add_rib(E, B)

    test_graph = [A, D, C, B, E]

    for i, i_test in zip(graph.gfs(A, E).stack, test_graph):
        assert i == i_test

    graph.remove_rib(E, B)

    assert graph.gfs(A, E).stack == []


if __name__ == '__main__':
    test_gfs()
