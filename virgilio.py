import os

class Virgilio:
    def __init__(self, directory):
        self.directory = directory

    def read_canto_lines(self, canto_number):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

virgilio_instance = Virgilio("canti")
print(virgilio_instance.read_canto_lines(5))