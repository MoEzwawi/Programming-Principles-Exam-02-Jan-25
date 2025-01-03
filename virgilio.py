import os

class Virgilio:
    def __init__(self, directory):
        self.directory = directory

    class CantoNotFoundError(Exception):
        def __init__(self):
            super().__init__("canto_number must be between 1 and 34.")

    def read_canto_lines(self, canto_number, strip_lines = False, num_lines = None):
        if not isinstance(canto_number, int):
            raise TypeError("canto_number must be an integer")
        
        if canto_number < 1 or canto_number > 34:
            raise self.CantoNotFoundError()
        
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            if num_lines is None:
                canto_lines = file.readlines()
            else:
                canto_lines = [file.readline() for _ in range(num_lines)]

            if strip_lines:
                return [line.strip() for line in canto_lines]
            else:
                return canto_lines

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
            hell_verses += canto_verses
        return hell_verses
    
    def count_hell_verses(self):
        return len(self.get_hell_verses())
    
    def get_hell_verse_mean_len(self):
        total_length = 0
        hell_verses = self.get_hell_verses()
        for verse in hell_verses:
            total_length += len(verse)
        total_verses = self.count_hell_verses()
        return total_length / total_verses

virgilio_instance = Virgilio("canti")
print(virgilio_instance.read_canto_lines("uno", True, 10))