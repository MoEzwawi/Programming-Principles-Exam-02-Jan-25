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
    
    def get_longest_canto(self):
        longest_canto = None
        longest_canto_length = 0
        for canto in range(1, 35):
            canto_as_list = self.read_canto_lines(canto)
            current_canto_length = len(canto_as_list)
            if current_canto_length > longest_canto_length:
                longest_canto = canto
                longest_canto_length = current_canto_length
        return { "canto_number": longest_canto, "canto_len": longest_canto_length }
    
    def count_words(self, canto_number, words):
        word_counter = {}
        for word in words:
            word_occurences = self.count_word(canto_number, word)
            word_counter[word] = word_occurences
        return word_counter
    
    def get_hell_verses(self):
        hell_verses = []
        for canto in range(1, 35):
            canto_verses = self.read_canto_lines(canto)
            for verse in canto_verses:
                hell_verses.append(verse)
        return hell_verses

virgilio_instance = Virgilio("canti")
print(len(virgilio_instance.get_hell_verses()))
