# -*- coding: utf-8 -*-


class Vertex:
    def __init__(self):
        pass


class SimpleGraph:
    def __init__(self, max_vertex):
        self.max_vertex = max_vertex
        self.m_adjency = [[0 for x in range(self.max_vertex)] for y in range(self.max_vertex)]
        self.vertex = [Vertex() for x in range(self.max_vertex)]

    def __repr__(self):
        res = ''
        for i in range(self.max_vertex):
            res += f'{self.m_adjency[i]}\n'
        return res

    def _get_index(self, vertex):
        return self.vertex.index(vertex)

    def add_rib(self, vertex_first, vertex_second):
        index_first = self._get_index(vertex_first)
        index_second = self._get_index(vertex_second)

        self.m_adjency[index_first][index_second] = 1
        self.m_adjency[index_second][index_first] = 1

    def remove_rib(self, vertex_first, vertex_second):
        index_first = self._get_index(vertex_first)
        index_second = self._get_index(vertex_second)

        self.m_adjency[index_first][index_second] = 0
        self.m_adjency[index_second][index_first] = 0

    def add_vertex(self, vertex):
        self.vertex.append(vertex)
        self.m_adjency.append([0 for i in range(self.max_vertex)])
        for i in self.m_adjency:
            i.append(0)
        self.max_vertex += 1

    def remove_vertex(self, vertex):
        index = self._get_index(vertex)
        del self.m_adjency[index]
        for i in self.m_adjency:
            del i[index]
        self.max_vertex -= 1


def test_add_rib():
    graph = SimpleGraph(3)
    graph.add_rib(graph.vertex[0], graph.vertex[0])
    graph.add_rib(graph.vertex[0], graph.vertex[1])
    graph.add_rib(graph.vertex[0], graph.vertex[2])

    test_graph = [
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]

    assert graph.m_adjency == test_graph


def test_remove_rib():
    graph = SimpleGraph(3)
    graph.add_rib(graph.vertex[0], graph.vertex[0])
    graph.add_rib(graph.vertex[0], graph.vertex[1])
    graph.add_rib(graph.vertex[0], graph.vertex[2])

    graph.remove_rib(graph.vertex[0], graph.vertex[2])

    test_graph = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]

    assert test_graph == graph.m_adjency


def test_add_vertex():
    graph = SimpleGraph(3)
    graph.add_rib(graph.vertex[0], graph.vertex[0])
    graph.add_rib(graph.vertex[0], graph.vertex[1])
    graph.add_rib(graph.vertex[0], graph.vertex[2])

    graph.add_vertex(Vertex())

    test_graph = [
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert test_graph == graph.m_adjency
    assert len(graph.m_adjency) == graph.max_vertex


def test_remove_vertex():
    graph = SimpleGraph(3)
    graph.add_rib(graph.vertex[0], graph.vertex[0])
    graph.add_rib(graph.vertex[0], graph.vertex[1])
    graph.add_rib(graph.vertex[0], graph.vertex[2])

    graph.remove_vertex(graph.vertex[0])

    test_graph = [
        [0, 0],
        [0, 0],
    ]

    assert test_graph == graph.m_adjency
    assert len(graph.m_adjency) == graph.max_vertex

    graph.remove_vertex(graph.vertex[0])

    test_graph = [
        [0],
    ]

    assert test_graph == graph.m_adjency
    assert len(graph.m_adjency) == graph.max_vertex


if __name__ == '__main__':
    test_add_rib()
    test_remove_rib()
    test_add_vertex()
    test_remove_vertex()
