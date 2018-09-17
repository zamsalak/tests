import json

jspn_data = """
[
  {
    "word": "menace",
    "meaning": "something that is likely to cause harm"
  },
  {
    "word": "vicarious",
    "meaning": "experienced as a result of watching, listening to, or reading about the activities of other people, rather than by doing the activities yourself"
  }
]
"""


class Arm:
    def __init__(self, json_data):
        self.json_data = json.loads(data)
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.json_data) == self.index:
            raise StopIteration
        else:
            returned = self.json_data[self.index]
            self.index += 1
            return returned

for i in Arm(data):
    print(i)
