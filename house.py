class House:
    def __init__(self, id, area, address, state, parking, elevator):
        self.id = id
        self.area = area
        self.address = address
        self.state = state
        self.parking = parking
        self.elevator = elevator

    def save(self):
        print(f"{self.id}---{self.area} {self.area} {self.address} {self.parking} {self.elevator}")
