class Flight:

    flights: dict = {}

    def __init__(self, id: int, origen: int, destino: int):
        self.id: int = id
        self.origen: int = origen
        self.destino: int = destino
        Flight.flights[id] = self

    def __repr__(self):
        return f"Flight(id={self.id}, origen={self.origen}, destino={self.destino})"