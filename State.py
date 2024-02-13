from Rectangle import Rectangle


"""Class representing the state of the Mondrian's Rectangles puzzle"""
class State:
    rectangles = {}
    ratios = set()  # List of possible ratios to split a rectangle
    dim = 0

    def __init__(self, dim: int):
        r = Rectangle(0, 0, dim, dim)
        self.rectangles[r] = r.area
        self.dim = dim

        for x in range(1, dim):
            for y in range(1, dim):
                if x != y and (y, x) not in self.ratios and x + y <= self.dim:
                    self.ratios.add((x, y))

    def score(self) -> int | float:
        if len(self.rectangles) == 1:
            return float("inf")

        return max(self.rectangles, key=lambda r: r.area) - min(self.rectangles, key=lambda r: r.area)

    # Update current state with new rectangles
    def update(self, r: Rectangle, r1: Rectangle, r2: Rectangle):
        self.rectangles.pop(r)
        self.rectangles[r1] = r1.area
        self.rectangles[r2] = r2.area
        return self

    # Restore the current state
    def restore(self, r: Rectangle, r1: Rectangle, r2: Rectangle):
        self.rectangles.pop(r1)
        self.rectangles.pop(r2)
        self.rectangles[r] = r.area

        return self

    def __str__(self):
        return f"Score >> {self.score()}\n" + "".join(list(map(lambda x: x.__str__(), self.rectangles)))
