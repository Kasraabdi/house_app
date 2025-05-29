from validator import house_validator


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

    def to_tuple(self):
        return (self.id, self.area, self.address, self.state, self.parking, self.elevator)

    def validate(self):
        return house_validator(self)
