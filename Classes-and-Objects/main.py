class Student:
    # [assignment] Skeleton class. Add your code here
    pass
    def __init__(self, name, age, tracks,score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, name):
            self.name = name
    def change_age(self, age):
            self.age = age
    def add_track(self, tracks):
            self.tracks = tracks
    def get_score(self):
            return self.score
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.change_name("Peter")   
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.name,Bob.age,Bob.tracks,Bob.score)