class Edge:

    egdes: list = []

    def __init__(self, start: int, end: int, weight:float):
        self.start = start
        self.end = end
        self.weight = weight
        Edge.egdes.append(self)

    def __repr__(self):
        return f"Edge({self.start}, {self.end}, {self.weight})"
