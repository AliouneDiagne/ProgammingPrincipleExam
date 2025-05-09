# PP_WITH_PYTHON

# Virgilio

La tua guida Python nell’Inferno di Dante: esplora i canti, conta versi e parole, scopri statistiche sulla “Divina Commedia” in un attimo.

---

##  Caratteristiche

* **Lettura versatile**: scegli quante righe leggere e rimuovi gli spazi superflui.
* **Conteggi rapidi**: versi, terzine e occorrenze di parole (anche in batch).
* **Ricerca parole**: trova il primo verso o tutti i versi con un dato termine.
* **Statistiche globali**: canto più lungo, numero e lunghezza media dei versi.
* **Esportazione JSON**: salva i conteggi parola per parola.

---

## 🛠️ Installazione

1. Clona il repo:

   ```bash
   git clone https://github.com/tuo-utente/virgilio-inferno.git
   ```
2. Prepara la cartella dei canti:

   ```
   divina_commedia/
   ├─ canto_1.txt
   ├─ ...
   └─ canto_34.txt
   ```
3. (Opzionale) ambiente virtuale:

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

---

##  Uso rapido

```python
from virgilio import Virgilio

v = Virgilio("divina_commedia")

# Conta versi e terzine del Canto 1
print(v.count_verses(1), "versi;", v.count_tercets(1), "terzine")

# Primo verso con "selva"
print(v.get_verse_with_word(1, "selva"))

# Canto più lungo
best = v.get_longest_canto()
print(f"Canto {best['canto_number']} con {best['canto_len']} versi")

# Salva i conteggi di parole in JSON
v.count_words_and_save(3, ["Inferno", "Dante"])
```

---



 
