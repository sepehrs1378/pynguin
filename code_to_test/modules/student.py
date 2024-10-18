class Teacher:
    def __init__(self, id_, courses) -> None:
        self.id = id_
        self.courses = courses


class Student:
    def __init__(self, id_, name, age) -> None:
        self.id = id_
        self.name = name
        self.age = age

    def get_courses(self):
        return [
            "basic programming",
            "advanced programming",
            "compiler design",
        ]


# def func(s):
#     if s.age < 18:
#         return "Go play your games."
#     if len(s.name) > 10:
#         return "I'm lazy. Tell it yourself."
#     if s.id == 911:
#         return "FBI! Open up!"
#     return "What a day."


def func(s: Teacher):
    if s.age < 18:
        return "Go play your games."
    if len(s.name) > 10:
        return "I'm lazy. Tell it yourself."
    if s.id == 911:
        return "FBI! Open up!"
    return "What a day."
