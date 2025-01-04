import os
import json
from typing import Optional, Union


class Virgilio:
    """
    Classe che permette di leggere e analizzare i canti dell'Inferno dantesco.
    Come Virgilio guida Dante nell'opera,
    questa classe fornisce metodi per esplorare e fare analisi sui versi,
    aiutando a comprendere il testo.

    Attributes:
        directory (str): La directory contenente i file dei canti dell'Inferno.
    """

    def __init__(self, directory: str):
        """
        Inizializza una nuova istanza della classe Virgilio.

        Args:
            directory (str): La directory dove sono memorizzati i file dei canti.
        """
        self.directory = directory

    class CantoNotFoundError(Exception):
        """
        Eccezione sollevata quando il numero del canto è fuori dal range valido (1-34).
        """

        def __init__(self):
            super().__init__("canto_number must be between 1 and 34.")

    def read_canto_lines(
        self,
        canto_number: int,
        strip_lines: bool = False,
        num_lines: Optional[int] = None,
    ) -> Union[list[str], str]:
        """
        Legge le righe di un canto specificato da un numero.

        Args:
            canto_number (int): Il numero del canto da leggere.
            strip_lines (bool, opzionale): Se True, rimuove gli spazi bianchi dalle righe. Default è False.
            num_lines (int, opzionale): Il numero massimo di righe da leggere. Se None, legge tutte le righe.

        Raises:
            CantoNotFoundError: Se il numero del canto è fuori dal range 1-34.
            TypeError: Se il numero del canto non è un intero.

        Returns:
            Union[list[str], str]: Una lista di righe del canto o un messaggio di errore.
        """
        if not isinstance(canto_number, int):
            raise TypeError("canto_number must be an integer")

        if canto_number < 1 or canto_number > 34:
            raise self.CantoNotFoundError()

        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                if num_lines is None:
                    canto_lines = file.readlines()
                else:
                    canto_lines = [file.readline() for _ in range(num_lines)]

                if strip_lines:
                    return [line.strip() for line in canto_lines]
                else:
                    return canto_lines
        except Exception:
            return f"error while opening {file_path}"

    def count_verses(self, canto_number: int) -> int:
        """
        Conta il numero di versi di un canto specificato.

        Args:
            canto_number (int): Il numero del canto.

        Returns:
            int: Il numero di versi nel canto.
        """
        return len(self.read_canto_lines(canto_number))

    def count_tercets(self, canto_number: int) -> int:
        """
        Conta il numero di terzine (gruppi di 3 versi) di un canto.

        Args:
            canto_number (int): Il numero del canto.

        Returns:
            int: Il numero di terzine nel canto.
        """
        return int(self.count_verses(canto_number) / 3)

    def count_word(self, canto_number: int, word: str) -> int:
        """
        Conta quante volte una parola appare in un canto.

        Args:
            canto_number (int): Il numero del canto.
            word (str): La parola da contare.

        Returns:
            int: Il numero di occorrenze della parola nel canto.
        """
        canto_as_string = "".join(self.read_canto_lines(canto_number))
        return canto_as_string.count(word)

    def get_verse_with_word(self, canto_number: int, word: str) -> Union[str, None]:
        """
        Ottiene il primo verso che contiene una parola specificata.

        Args:
            canto_number (int): Il numero del canto.
            word (str): La parola da cercare.

        Returns:
            str: Il primo verso che contiene la parola, o None se non trovata.
        """
        canto_as_list = self.read_canto_lines(canto_number)
        for verse in canto_as_list:
            if word in verse:
                return verse

    def get_verses_with_word(self, canto_number: int, word: str) -> list[str]:
        """
        Ottiene tutti i versi che contengono una parola specificata.

        Args:
            canto_number (int): Il numero del canto.
            word (str): La parola da cercare.

        Returns:
            list[str]: Una lista di versi che contengono la parola.
        """
        canto_as_list = self.read_canto_lines(canto_number)
        verses_with_word = []
        for verse in canto_as_list:
            if word in verse:
                verses_with_word.append(verse)
        return verses_with_word

    def get_longest_verse(self, canto_number: int) -> str:
        """
        Ottiene il verso più lungo di un canto.

        Args:
            canto_number (int): Il numero del canto.

        Returns:
            str: Il verso più lungo del canto.
        """
        canto_as_list = self.read_canto_lines(canto_number)
        longest_verse = ""
        for verse in canto_as_list:
            if len(verse) > len(longest_verse):
                longest_verse = verse
        return longest_verse

    def get_longest_canto(self) -> dict[str, int]:
        """
        Trova il canto dell'Inferno con il maggior numero di versi.

        Returns:
            dict[str, int]: Un dizionario contenente il numero del canto e la lunghezza in versi.
        """
        longest_canto = None
        longest_canto_length = 0
        for canto in range(1, 35):
            canto_as_list = self.read_canto_lines(canto)
            current_canto_length = len(canto_as_list)
            if current_canto_length > longest_canto_length:
                longest_canto = canto
                longest_canto_length = current_canto_length
        return {
            "canto_number": longest_canto,
            "canto_len": longest_canto_length,
        }

    def count_words(
        self,
        canto_number: int,
        words: list[str],
    ) -> dict[str, int]:
        """
        Conta le occorrenze di più parole in un canto e salva i risultati in un file JSON.

        Args:
            canto_number (int): Il numero del canto.
            words (list[str]): La lista di parole da contare.

        Returns:
            dict[str, int]: Un dizionario con le parole come chiavi e il numero di occorrenze come valori.
        """
        word_counter = {}
        for word in words:
            word_occurences = self.count_word(canto_number, word)
            word_counter[word] = word_occurences
        file_path = os.path.join(self.directory, "word_counts.json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(word_counter, json_file)
        return word_counter

    def get_hell_verses(self) -> list[str]:
        """
        Ottiene tutti i versi dell'Inferno (canti da 1 a 34).

        Returns:
            list[str]: Una lista di tutti i versi dei canti.
        """
        hell_verses = []
        for canto in range(1, 35):
            canto_verses = self.read_canto_lines(canto)
            hell_verses += canto_verses
        return hell_verses

    def count_hell_verses(self) -> int:
        """
        Conta il numero totale di versi nell'Inferno.

        Returns:
            int: Il numero totale di versi nell'Inferno.
        """
        return len(self.get_hell_verses())

    def get_hell_verse_mean_len(self) -> float:
        """
        Calcola la lunghezza media dei versi dell'Inferno in termini di caratteri.

        Returns:
            float: La lunghezza media dei versi dell'Inferno.
        """
        total_length = 0
        hell_verses = self.get_hell_verses()
        for verse in hell_verses:
            total_length += len(verse)
        total_verses = self.count_hell_verses()
        return total_length / total_verses


virgilio_instance = Virgilio("canti")
