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
    
    def count_word(self, canto_number, word):
        canto_as_string = "".join(self.read_canto_lines(canto_number))
        return canto_as_string.count(word)
    
    def get_verse_with_word(self, canto_number, word):
        canto_as_list = self.read_canto_lines(canto_number)
        for verse in canto_as_list:
            if word in verse:
                return verse
            
    def get_verses_with_word(self, canto_number, word):
        canto_as_list = self.read_canto_lines(canto_number)
        verses_with_word = []
        for verse in canto_as_list:
            if word in verse:
                verses_with_word.append(verse)
        return verses_with_word
    
    def get_longest_verse(self, canto_number):
        canto_as_list = self.read_canto_lines(canto_number)
        longest_verse = ""
        for verse in canto_as_list:
            if len(verse) > len(longest_verse):
                longest_verse = verse
        return longest_verse


virgilio_instance = Virgilio("canti")
print("longest verse",virgilio_instance.get_longest_verse(26))