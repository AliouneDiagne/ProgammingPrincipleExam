import os
import json

# Classe Virgilio: la nostra guida fidata lungo i meandri dell'Inferno di Dante 
class Virgilio:
    def __init__(self, directory):
        self.directory = directory

    # Nell'esercizio 1 si scrive il metodo read_canto_lines con il parametro canto_number
    # che legge le righe di un file di testo in base al numero del Canto. 
    def read_canto_lines(self, canto_number, strip_lines=False, num_lines=None):
        try:
            file_path = os.path.join(self.directory, f'canto_{canto_number}.txt')
            if not os.path.exists(file_path):
                print(f"Attenzione: il file per il Canto {canto_number} molto probabilmente non esiste!")
                return []
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if strip_lines:
                    lines = [line.strip() for line in lines]
                if num_lines:
                    lines = lines[:num_lines]
                return lines
        except Exception as e:
            print(f"C'è stato un errore durante la lettura del file: {e}")
            return []

    # Nell'esercizio 2 si conta attraverso il metodo count_verses 
    # con il parametro canto_number il numero di versi in un canto.
    def count_verses(self, canto_number):
        lines = self.read_canto_lines(canto_number)
        return len(lines)

    # Esercizio 3: ho scritto il metodo count_tercets con il parametro 
    # canto_number che restituisce il numero intero di terzine in un canto
    def count_tercets(self, canto_number):
        num_verses = self.count_verses(canto_number)
        return num_verses // 3
        

    # Esercizio 4: con il metodo count_word e i parametri canto_number e word
    # si contano le occorrenze di una parola in un canto. il metodo è case-sensitive.
    def count_word(self, canto_number, word):
        lines = self.read_canto_lines(canto_number)
        full_text = "".join(lines)
        count = full_text.count(word)
        return count

    # Esercizio 5: con il metodo get_verse_with_word e i parametri canto_number e word
    # si restituisce il primo verso che contiene una parola specifica in un canto.
    def get_verse_with_word(self, canto_number, word):
        lines = self.read_canto_lines(canto_number)
        for line in lines:
            if word in line:
                return line.strip()
        return None

    # Con l'esercizio 6 e il metodo get_verses_with_word e i parametri canto_number e word
    # si ottengono una lista di tutti i versi del canto scelto.
    def get_verses_with_word(self, canto_number, word):
        lines = self.read_canto_lines(canto_number)
        return [line.strip() for line in lines if word in line]

    # Nell'esercizio 7 usando il metodo get_longest_verse e il parametro canto_number
    # si ottiene il verso più lungo in un canto scelto
    def get_longest_verse(self, canto_number):
        lines = self.read_canto_lines(canto_number)
        return max(lines, key=len).strip() if lines else None

    # Esercizio 8: si crea il metodo get_longest_canto che restituisce un dizionario
    # con due coppie chiave-valore: la chiave canto_number con un valore intero con
    # più versi dell'inferno e la chiave canto_len con il numero di versi del canto.
    def get_longest_canto(self):

        try:
            longest_canto = {'canto_number': 0, 'canto_len': 0}
            for i in range(1, 35):
                verses_count = self.count_verses(i)
                if verses_count > longest_canto['canto_len']:
                    longest_canto = {'canto_number': i, 'canto_len': verses_count}
            return longest_canto

        except Exception as e:
            print(f" Spiacente, si è verificato un errore durante l'operazione: {e}")
            return longest_canto

    # Esercizio 9:si crea il metodo count_words che conta le occorrenze di più parole in un canto
    def count_words(self, canto_number, words):
       word_count = {}
       for word in words:
              count = self.count_word(canto_number, word)
              word_count[word] = count
              return word_count

    # Esercizio 10: con il metodo get_hell_verses si ottengono tutti i versi dell'Inferno in ordine
    def get_hell_verses(self):
        all_verses = []
        for i in range(1, 35):
            all_verses.extend(self.read_canto_lines(i))
        return all_verses


    # Esercizio 11: si sommano tutti i versi di tutti i canti e si restituisce il totale
    def count_hell_verses(self):
        total_verses = sum(self.count_verses(i) for i in range(1, 35))
        return total_verses

    # Esercizio 12: otteniamo tutti i versi sommando la lunghezza di tutti i versi 
    # calcolando e restituendo la media della lunghezza
    def get_hell_verse_mean_len(self):
        all_verses = self.get_hell_verses()
        total_length = sum(len(verse.strip()) for verse in all_verses)
        return total_length / len(all_verses) if all_verses else 0


    # Esercizio 13:  Aggiungendo il parametro strip_lines al metodo read_canto_lines
    # si può decidere se applicare il metodo strip() alle righe lette
    def read_canto_lines_v2(self, canto_number, strip_lines=True, num_lines=None):
        return self.read_canto_lines(canto_number, strip_lines, num_lines)


    # Esercizio 14: Leggi un numero limitato di righe da un canto e se non è specificato il metodo
    # restituirà verranno lette le prime 5 righe
    def read_canto_lines_v3(self, canto_number, strip_lines=False, num_lines=5):
        return self.read_canto_lines(canto_number, strip_lines, num_lines)


    # Esercizio 15: Verifica se il numero del canto è un intero e se non lo è solleva un'eccezione
    # di tipo TypeError per segnalare l'errore ...
    def read_canto_lines_v4(self, canto_number, strip_lines=False, num_lines=None):
        if not isinstance(canto_number, int):
            raise TypeError("Errore: il numero del canto deve essere un intero!")
        return self.read_canto_lines(canto_number, strip_lines, num_lines)

    # Esercizio 16: Verifica che il numero del canto sia valido e se non lo
    # è solleva un'eccezione di tipo CantoNotFoundError
    def read_canto_lines_v5(self, canto_number, strip_lines=False, num_lines=None):
        if canto_number < 1 or canto_number > 34:
            raise CantoNotFoundError("Errore: il numero del canto deve essere compreso tra 1 e 34!")
        return self.read_canto_lines(canto_number, strip_lines, num_lines)


    # Esercizio 17: Gestione delle eccezioni migliorata
    def read_canto_lines_v6(self, canto_number, strip_lines=False, num_lines=None):
        try:
            return self.read_canto_lines(canto_number, strip_lines, num_lines)
        except Exception as e:
            print(f"c'è stato un errore molto probabilmente durante la lettura del file: {e}") 
            return f"error while opening {os.path.join(self.directory, f'canto_{canto_number}.txt')}"

    # Esercizio 18: contando le occorrenze di una lista di parole in un canto e salvando i conteggi
    # in un file JSON con il metodo count_words_and_save
    def count_words_and_save(self, canto_number, words):
        word_count = self.count_words(canto_number, words)
        file_path = os.path.join(self.directory, 'word_counts.json')
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(word_count, f, ensure_ascii=False, indent=4)
            print(f"Conteggi delle parole salvati con successo in: {file_path}")
        except Exception as e:
            print(f"Errore durante il salvataggio del file JSON: {e}")
        return word_count

# Classe per l'eccezione personalizzata
class CantoNotFoundError(Exception):
    pass

# Testiamo il nostro codice

# Creiamo un oggetto Virgilio che lavorerà sui file contenuti nella directory 'divina_commedia'
directory = 'C:/Users/merli/Desktop/file di python/Progetto PP di Alioune Diagne/divina_commedia'
v = Virgilio(directory)


### Test della maggior parte degli esercizi alcuni esercizi per vedere se funzionano ###

# Test Esercizio 1: si va leggere delle righe del canto 1
print("\n es 1")
canto_number = 1
lines = v.read_canto_lines(canto_number)
print(f"\nLe righe totale del Canto {canto_number}sono: {lines}")

# Test Esercizio 2 dove si contano i versi del canto 1
print("\n es 2")
verses_count = v.count_verses(canto_number)
print(f"IL numero di versi che si trova nel canto {canto_number} risulta: {verses_count}")

# Test Esercizio 3: si contano le terzine del Canto 1
print("\n es 3")
tercets_count = v.count_tercets(canto_number)
print(f"Il numero di terzine nel Canto {canto_number} è: {tercets_count}")

# Test Esercizio 4: si contano occorrenze della parola "Inferno" nel Canto 1
print("\n es 4")
word_to_search = "Inferno" 
word_count = v.count_word(canto_number, word_to_search)
print(f"\nLa parola '{word_to_search}' si ripete {word_count} volte nel Canto {canto_number}.")

# Test Esercizio 5: il primo verso che contiene la parola "Inferno" nel Canto 1 è:
print("\n es 5")
verse_with_word = v.get_verse_with_word(canto_number, word_to_search)
print(f"\nIl primo verso che contiene la parola '{word_to_search}' nel Canto {canto_number} è:\n{verse_with_word}")

# Test Esercizio 7: si trova il verso più lungo nel Canto 1 con il metodo get_longest_verse
print("\n es 7")
longest_verse = v.get_longest_verse(canto_number)
print(f"\nIl verso più lungo del Canto {canto_number} è il seguente:\n{longest_verse}")

# Test Esercizio 8: si trova il canto più lungo dell'Inferno
print("\n es 8")
longest_canto = v.get_longest_canto()
print(f"\nIl Canto più lungo dell'Inferno è il Canto {longest_canto['canto_number']} con {longest_canto['canto_len']} versi.")

# Esercizio 9: si contano le occorrenze di più parole nel Canto 1
print("\n es 9")
words_to_search = ["Inferno", "Dante", "Virgilio"]
word_counts = v.count_words(canto_number, words_to_search)
print(f"\nConteggio delle parole nel Canto {canto_number}:\n{word_counts}")

# Esercizio 10: si ottengono il numero tutti i versi dell'Inferno
print("\n es 10")
all_verses = v.get_hell_verses()
print(f"\nIl numero totale di versi nell'Inferno è: {len(all_verses)}")

# Test Esercizio 11: ora contiamo il numero totale di versi dell'Inferno
print("\n es 11")
total_verses = v.count_hell_verses()
print(f"\nIl conteggio totale dei versi nell'Inferno risulta: {total_verses}")

# Test Esercizio 15: si leggono le righe del Canto 1 con strip_lines=True
print("\n es 15")
try:
    v.read_canto_lines_v4("1")
except TypeError as e:
    print(f"c'è stato un errore durante la lettura del file: {e}")

# Test Esercizio 16: si leggono le righe del Canto 100 che non esiste
print("\n es 16")
try:
    v.read_canto_lines_v5(100)
except CantoNotFoundError as e:
    print(f" c'è stato un errore durante la lettura del file: {e}")

# Test Esercizio 17: qui introduciamo una gestione delle eccezioni quando proviamo a leggere 
# un canto che non esiste. In caso di errore, verrà stampato un messaggio di errore 
print("\n es 17")
canto_number = 100
lines = v.read_canto_lines_v6(canto_number)


# Test Esercizio 18: Salva i conteggi delle parole in un file JSON
print("\n es 18")
word_counts_saved = v.count_words_and_save(canto_number, words=["Vita", "Selva", "Camminando"])
print(f"\n i conteggi delle parole salvati sono: {word_counts_saved}")
