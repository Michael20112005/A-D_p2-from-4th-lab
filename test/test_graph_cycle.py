import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from graph_cycle import bfs


class TestBFS(unittest.TestCase):

    def test_cycle_start(self):
        graph = {1: [2], 2: [3], 3: [1]}
        visited = set()
        self.assertTrue(bfs(1, graph, visited))

    def test_start_node_with_no_outgoing_edges(self):
        graph = {1: [2], 2: [3], 3: [1]}
        visited = set()
        self.assertTrue(bfs(1, graph, visited))

    def test_start_node_with_one_outgoing_edge(self):
        graph = {1: [2], 2: [3], 3: [1]}
        visited = set()
        self.assertTrue(bfs(2, graph, visited))


if __name__ == '__main__':
    unittest.main()
