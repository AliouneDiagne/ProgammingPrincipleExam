from pathlib import Path
import json
from typing import List, Dict, Optional

class CantoNotFoundError(Exception):
    """Errore: il numero del canto deve essere compreso tra 1 e 34."""
    pass

class Virgilio:
    """
    Virgilio, guida fidata attraverso l'Inferno di Dante.
    Permette di leggere canti, contare versi, terzine, parole e
    ottenere utili statistiche sull'intera cantica.
    """
    def __init__(self, directory: str):
        """
        :param directory: cartella contenente i file 'canto_1.txt' ... 'canto_34.txt'
        """
        self.directory = Path(directory)

    def read_canto_lines(
        self,
        canto_number: int,
        strip_lines: bool = False,
        num_lines: Optional[int] = None
    ) -> List[str]:
        """
        Legge e restituisce le righe del canto richiesto.

        1. Verifica che canto_number sia intero e nell'intervallo valido.
        2. Controlla l'esistenza del file; se manca, solleva FileNotFoundError.
        3. Applica strip() se richiesto e limita il numero di righe.

        :param canto_number: intero tra 1 e 34
        :param strip_lines: True per rimuovere spazi iniziali/finali da ogni riga
        :param num_lines: se non None, legge solo le prime num_lines righe
        :raises TypeError: se canto_number non è int
        :raises CantoNotFoundError: se canto_number non in [1, 34]
        :raises FileNotFoundError: se il file non esiste
        :return: lista di righe (con '\n' se strip_lines=False)
        """
        if not isinstance(canto_number, int):
            raise TypeError("Il numero del canto deve essere un intero.")
        if not (1 <= canto_number <= 34):
            raise CantoNotFoundError("Il numero del canto deve essere tra 1 e 34.")
        
        file_path = self.directory / f"canto_{canto_number}.txt"
        if not file_path.exists():
            raise FileNotFoundError(f"File non trovato: {file_path}")

        with file_path.open(encoding='utf-8') as f:
            lines = f.readlines()

        if strip_lines:
            lines = [ln.strip() for ln in lines]
        if num_lines is not None:
            lines = lines[:num_lines]

        return lines

    def count_verses(self, canto_number: int) -> int:
        """Ritorna il numero totale di versi (righe) in un canto."""
        return len(self.read_canto_lines(canto_number))

    def count_tercets(self, canto_number: int) -> int:
        """Ogni terzina ha 3 versi: restituisce quante terzine intere ci sono."""
        return self.count_verses(canto_number) // 3

    def count_word(self, canto_number: int, word: str) -> int:
        """
        Conta le occorrenze di una parola (case-sensitive) nel canto.
        Unisce tutte le righe in un unico testo per semplificare la ricerca.
        """
        text = "".join(self.read_canto_lines(canto_number))
        return text.count(word)

    def count_words(self, canto_number: int, words: List[str]) -> Dict[str, int]:
        """
        Conta più parole in un canto, restituendo un dizionario
        {parola: occorrenze}.
        """
        return {w: self.count_word(canto_number, w) for w in words}

    def get_verse_with_word(self, canto_number: int, word: str) -> Optional[str]:
        """
        Restituisce il primo verso che contiene la parola specificata,
        o None se non la trova.
        """
        for ln in self.read_canto_lines(canto_number):
            if word in ln:
                return ln.strip()
        return None

    def get_verses_with_word(self, canto_number: int, word: str) -> List[str]:
        """
        Restituisce tutti i versi del canto che contengono la parola data.
        """
        return [ln.strip() for ln in self.read_canto_lines(canto_number) if word in ln]

    def get_longest_verse(self, canto_number: int) -> str:
        """
        Trova il verso più lungo in termini di caratteri
        (inclusi spazi, escludendo '\n').
        """
        lines = self.read_canto_lines(canto_number)
        return max(lines, key=len).strip()

    def get_longest_canto(self) -> Dict[str, int]:
        """
        Scorre tutti i 34 canti e restituisce
        {'canto_number': N, 'canto_len': numero_versi}
        per il canto più lungo.
        """
        best = {'canto_number': 0, 'canto_len': 0}
        for n in range(1, 35):
            cnt = self.count_verses(n)
            if cnt > best['canto_len']:
                best = {'canto_number': n, 'canto_len': cnt}
        return best

    def get_hell_verses(self) -> List[str]:
        """Ritorna la lista di tutti i versi dell'Inferno, canto per canto."""
        verses: List[str] = []
        for n in range(1, 35):
            verses.extend(self.read_canto_lines(n))
        return verses

    def count_hell_verses(self) -> int:
        """Somma semplicemente il totale dei versi di tutti i canti."""
        return sum(self.count_verses(n) for n in range(1, 35))

    def get_hell_verse_mean_len(self) -> float:
        """
        Calcola la lunghezza media dei versi (in caratteri) su tutto l'Inferno.
        """
        all_verses = self.get_hell_verses()
        if not all_verses:
            return 0.0
        total_chars = sum(len(v.strip()) for v in all_verses)
        return total_chars / len(all_verses)

    def count_words_and_save(self, canto_number: int, words: List[str]) -> Dict[str, int]:
        """
        Conta le occorrenze di una lista di parole e salva il risultato
        in 'word_counts.json' nella directory specificata.
        """
        counts = self.count_words(canto_number, words)
        out_path = self.directory / 'word_counts.json'
        with out_path.open('w', encoding='utf-8') as f:
            json.dump(counts, f, ensure_ascii=False, indent=4)
        print(f"✅ Conteggi salvati in: {out_path}")
        return counts

# Esempio di utilizzo:
if __name__ == "__main__":
    base_dir = "divina_commedia"
    v = Virgilio(base_dir)
    print("Versione rifattorizzata di Virgilio pronta all'uso!")
    # Puoi ora fare: v.count_verses(1), v.get_longest_canto(), ecc.
