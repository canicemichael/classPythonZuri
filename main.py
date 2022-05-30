class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, value):
        self.name = value

    def change_age(self, value):
        self.age = value

    def get_score(self):
        return self.score

    def add_track(self, newItem):
        self.tracks.append(newItem)

    # @score.setter
    def score(self, value):
        try:
            self._score = float(value)
            print("Validated")
        except ValueError:
            raise ValueError('"score" must be a number') from None



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.name)