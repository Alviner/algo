# -*- coding: utf-8 -*-

import queue
from dfs import Vertex as DfsVertex, Graph as DfsGraph


class Vertex(DfsVertex):
    def __init__(self, value):
        super(Vertex, self).__init__(value)
        self.parent = None

    def set_parent(self, vertex):
        self.parent = vertex


class Graph(DfsGraph):
    vertex_class = Vertex

    def __init__(self, max_vertex=0):
        super(Graph, self).__init__(max_vertex)
        self.queue = queue.Queue()

    def bfs(self, first_vertex: Vertex, second_vertex: Vertex):
        self.queue.__init__()
        for vertex in self.vertex:
            vertex.set_unvisited()
        path = []
        first_vertex.set_visited()
        self.queue.enqueue(first_vertex)

        while self.queue.size() > 0:
            current_vertex = self.queue.dequeue()
            if current_vertex == second_vertex:
                while current_vertex is not None:
                    path.append(current_vertex)
                    if current_vertex.parent is not None:
                        current_vertex = current_vertex.parent
                    else:
                        current_vertex = None
                return True, list(reversed(path))
            for vertex in self.get_adjacent(current_vertex):
                if not vertex.is_visited():
                    self.queue.enqueue(vertex)
                    vertex.set_visited()
                    vertex.set_parent(current_vertex)
        return False, []


def test_bfs():
    graph = Graph(0)

    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')
    F = Vertex('F')

    graph.add_vertex(A)
    graph.add_vertex(B)
    graph.add_vertex(C)
    graph.add_vertex(D)
    graph.add_vertex(E)
    graph.add_vertex(F)

    graph.add_rib(A, B)
    graph.add_rib(B, D)
    graph.add_rib(D, F)
    graph.add_rib(F, C)
    graph.add_rib(E, C)

    graph.add_rib(A, E)
    graph.add_rib(E, F)

    test_bfs = [A, E, C]
    is_path, bfs = graph.bfs(A, C)

    assert is_path
    for i, i_test in zip(bfs, test_bfs):
        assert i, i_test

    test_bfs = [A, B, D]
    is_path, bfs = graph.bfs(A, D)

    assert is_path
    for i, i_test in zip(bfs, test_bfs):
        assert i, i_test

    test_bfs = [A, E, F]
    is_path, bfs = graph.bfs(A, F)

    assert is_path
    for i, i_test in zip(bfs, test_bfs):
        assert i, i_test

    graph.remove_rib(B, D)
    test_bfs = [A, E, F, D]
    is_path, bfs = graph.bfs(A, D)

    assert is_path
    for i, i_test in zip(bfs, test_bfs):
        assert i, i_test

    graph.remove_rib(F, D)
    test_bfs = []
    is_path, bfs = graph.bfs(A, D)

    assert not is_path
    for i, i_test in zip(bfs, test_bfs):
        assert i, i_test


if __name__ == '__main__':
    test_bfs()
