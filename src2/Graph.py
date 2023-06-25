from Node import Node
from Edge import Edge


class Graph:

    graph: dict = {}

    @staticmethod
    def create_graph():
        Graph.graph = {i: {} for i in Node.nodes.keys()}
        for egde in Edge.egdes:
            Graph.graph[egde.start][egde.end] = egde.weight
            Graph.graph[egde.end][egde.start] = egde.weight

    def __repr__(self):
        return f"Graph({Graph.graph})"
