import os

class Virgilio:
    def __init__(self, directory):
        self.directory = directory

    def read_canto_lines(self, canto_number):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
        
    def count_verses(self, canto_number):
        return len(self.read_canto_lines(canto_number))
    
    def count_tercets(self, canto_number):
        return int(self.count_verses(canto_number) / 3)

virgilio_instance = Virgilio("canti")

for i in range(1, 35):
    print(i, virgilio_instance.count_verses(i), virgilio_instance.count_tercets(i))