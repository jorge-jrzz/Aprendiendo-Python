class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon

    def __ne__(self, other):
        return self.lat != other.lat or self.lon != other.lon

    def __lt__(self, other):
        return self.lat + self.lon < other.lat + other.lon

    def __le__(self, other):
        return self.lat + self.lon <= other.lat + other.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

# print(coords != coords2)
print(coords >= coords2)
