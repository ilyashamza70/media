# 📊 Confronto Versioni: v1.0 vs v2.0

## Overview

Questo documento mostra il confronto tra la versione originale (v1.0) e la nuova versione aggiornata (v2.0) del Calcolatore Voto di Laurea.

---

## 🎯 Caratteristiche Principali

| Caratteristica | v1.0 (Originale) | v2.0 (Nuova) |
|----------------|------------------|--------------|
| **Interfaccia** | Testo semplice | Rich UI colorata e interattiva ✨ |
| **Corsi Supportati** | 1 (Embedded Systems) | 6+ (3 Triennali + 3 Magistrali) 🎓 |
| **Input Voti** | Solo manuale | Manuale + File (TXT/CSV/Excel) 📁 |
| **Statistiche** | Base | Avanzate (min/max/median/std) 📊 |
| **Grafici** | 2 grafici semplici | 4 grafici professionali 📈 |
| **Export** | No | JSON + CSV ✅ |
| **Storico** | Pickle | JSON strutturato 💾 |
| **Documentazione** | Minima | Completa (IT/EN) 📚 |
| **File Esempio** | No | Sì (TXT/CSV/Excel) 📄 |
| **Validazione Input** | Minima | Robusta con messaggi chiari ✓ |

---

## 💻 Interfaccia Utente

### v1.0 - Interfaccia Base
```
Enter your grades for the following courses:
Electronics for embedded systems: 28
Computer architectures: 30
...
Weighted Average: 28.45
Arithmetic Average: 28.33
Predicted Graduation Grade: 104.32
```

**Caratteristiche:**
- Testo bianco su nero
- Nessuna formattazione
- Prompt sequenziali

### v2.0 - Interfaccia Avanzata
```
╔══════════════════════════════════════════════════════════════╗
║  🎓 CALCOLATORE AVANZATO VOTO DI LAUREA 🎓              ║
║                                                              ║
║  Calcola media ponderata, aritmetica e voto finale     ║
║  Supporta Triennale e Magistrale                       ║
║  Import da file TXT, CSV, Excel                         ║
╚══════════════════════════════════════════════════════════════╝

Seleziona il tipo di corso:
1. Triennale (Bachelor's - 180 CFU)
2. Magistrale (Master's - 120 CFU)

╭─────────────────────────────────────╮
│         RISULTATI CALCOLO           │
╰─────────────────────────────────────╯
╭────────────────────────────────┬────────────╮
│ Media Ponderata                │   29.13/30 │
│ Media Aritmetica               │   28.36/30 │
│                                │            │
│ Voto di Laurea Previsto        │ 108.32/110 │
╰────────────────────────────────┴────────────╯
```

**Caratteristiche:**
- ✨ Colori vivaci e emoji
- 📊 Tabelle formattate
- 🎨 Box e pannelli decorativi
- ✅ Feedback visuale chiaro
- 📋 Menu interattivi

---

## 📚 Corsi di Laurea

### v1.0
**Solo 1 corso:**
- Embedded Systems (Magistrale)

### v2.0
**6 corsi preconfigurati:**

**Triennale (180 CFU):**
1. **Computer Engineering** - 19 esami
   - Analisi Matematica, Fisica, Programmazione, etc.
   
2. **Information Technology** - 19 esami
   - Sviluppo web, Mobile, Sicurezza, etc.
   
3. **Mathematics** - 18 esami
   - Analisi, Algebra, Geometria, etc.

**Magistrale (120 CFU):**
1. **Embedded Systems** - 14 esami
   - Electronics, IoT, Cybersecurity, etc.
   
2. **Computer Science** - 12 esami
   - ML, AI, Cloud Computing, Big Data, etc.
   
3. **Data Science** - 13 esami
   - Deep Learning, Data Mining, Analytics, etc.

**Bonus:** Sistema modulare per aggiungere facilmente nuovi corsi!

---

## 📁 Metodi di Input

### v1.0
**Solo input manuale:**
```python
for course in courses:
    grade = float(input(f"{course}: "))
    grades[course] = grade
```

**Limitazioni:**
- Tedioso per molti esami
- Nessuna possibilità di salvare/riutilizzare
- Rischio di errori di digitazione

### v2.0
**4 modalità di input:**

#### 1. Manuale (Migliorato)
- ✅ Validazione intelligente (18-30)
- ✅ Supporto 30L per la lode
- ✅ Feedback visuale immediato
- ✅ Barra di progresso

#### 2. File TXT
```text
# voti.txt
Mathematical Analysis I = 28
Computer Programming = 30L
Data Structures = 27
```

#### 3. File CSV
```csv
Corso,Voto
Mathematical Analysis I,28
Computer Programming,30L
```

#### 4. File Excel
Tabella Excel con colonne `Corso` e `Voto`

**Vantaggi:**
- 💾 Riutilizzabile
- ✏️ Modificabile facilmente
- 📊 Compatibile con Excel/Google Sheets
- 🔄 Importabile rapidamente

---

## 📊 Statistiche

### v1.0
Calcola solo:
- Media ponderata
- Media aritmetica
- Voto di laurea base

### v2.0
Calcola tutto questo + :

**Statistiche Avanzate:**
- 📉 Voto minimo
- 📈 Voto massimo
- 📊 Mediana
- 📐 Deviazione standard
- ⭐ Numero di 30 e Lode
- 🏆 Numero di 30
- ⚠️ Numero di voti sotto 24
- 📚 Totale esami

**Bonus Lode:**
- Ogni 30L aggiunge 0.5 punti (max 5)
- Calcolo automatico nel voto finale

---

## 📈 Visualizzazioni

### v1.0 - 2 Grafici Base

**1. Confronto Medie:**
- Barre semplici blu/verde
- Nessuna soglia

**2. Voto di Laurea:**
- Barra viola singola
- Nessun contesto

### v2.0 - 4 Grafici Professionali

**1. Confronto Medie:**
- ✅ Barre colorate con etichette
- ✅ Soglie 24 e 27 visualizzate
- ✅ Valori numerici sui grafici
- ✅ Legenda chiara

**2. Voto di Laurea:**
- ✅ Colore dinamico basato su voto
  - 🔴 < 90: Rosso
  - 🟣 90-100: Viola
  - 🟠 100-110: Arancione
  - 🟢 110: Verde
- ✅ Soglie 100 e 110 evidenziate

**3. Distribuzione Voti (NUOVO!):**
- 📊 Istogramma completo
- 📈 Media ponderata sovrapposta
- 📉 Range 18-30

**4. Top 10 Corsi (NUOVO!):**
- 🏆 Barre orizzontali per corso
- 🎨 Codifica colori:
  - 🟢 Verde: ≥27
  - 🟠 Arancione: 24-26
  - 🔴 Rosso: <24

**Qualità Output:**
- 📸 Salvataggio PNG ad alta risoluzione (300 DPI)
- 📐 Layout ottimizzato (14x10 pollici)
- 🎨 Stile professionale
- 💾 Timestamp nel nome file

---

## 💾 Persistenza Dati

### v1.0
**File:** `simulation_log.pkl`
- Formato binario Pickle
- Non leggibile da umani
- Non facilmente esportabile

### v2.0
**File:** `simulation_log.json`
- ✅ Formato JSON leggibile
- ✅ Facile da parsare/esportare
- ✅ Compatibile con altri tool
- ✅ UTF-8 encoding

**Export Aggiuntivi:**
```
results_TIMESTAMP.json  # Risultati completi
grades_TIMESTAMP.csv    # Tabella voti
grade_analysis_TIMESTAMP.png  # Grafici
```

**Esempio JSON:**
```json
{
  "timestamp": "20251108_214009",
  "degree_course": "Embedded Systems",
  "weighted_average": 29.13,
  "graduation_grade": 108.32,
  "statistics": {
    "num_30L": 3,
    "std_dev": 1.39
  }
}
```

---

## 📚 Documentazione

### v1.0
- README.md base (3 righe)
- ToDoList.txt con note sparse

### v2.0
**5 file di documentazione completa:**

1. **README.md** (Italiano, esteso)
   - 200+ righe
   - Badges, emoji, esempi
   - Installazione, uso, troubleshooting

2. **README_EN.md** (English)
   - Documentazione completa in inglese
   - Per utenti internazionali

3. **DOCUMENTAZIONE_IT.md** (Guida Completa)
   - 500+ righe
   - FAQ dettagliate
   - Esempi pratici step-by-step
   - Interpretazione risultati

4. **USER_GUIDE.md** (Guida Rapida)
   - Quick start 5 minuti
   - Shortcuts e tips
   - Workflow consigliati

5. **COMPARISON.md** (Questo file!)
   - Confronto dettagliato v1 vs v2

**Inoltre:**
- File di esempio (TXT, CSV)
- Commenti nel codice
- Docstrings complete

---

## 🔧 Architettura del Codice

### v1.0
**Struttura procedurale:**
```python
# Script monolitico
courses = {...}  # Hardcoded

def calculate_weighted_average(grades):
    ...

def main():
    grades = {}
    for course in courses:
        grade = input(...)
    ...

if __name__ == "__main__":
    main()
```

**Caratteristiche:**
- Singolo file
- Dati hardcoded
- Funzioni globali

### v2.0
**Architettura OOP modulare:**

```python
# degree_courses.py
MAGISTRALE_COURSES = {...}
TRIENNALE_COURSES = {...}

def get_all_courses():
    ...

# grade_calculator.py
class GradeCalculator:
    def __init__(self):
        ...
    
    def select_degree_type(self):
        ...
    
    def import_grades_from_file(self):
        ...
    
    def calculate_statistics(self):
        ...
    
    def plot_visualizations(self):
        ...
```

**Vantaggi:**
- 📦 Modulare e manutenibile
- 🔄 Riutilizzabile
- 🧪 Testabile
- 📈 Scalabile
- 🎯 Separazione delle responsabilità

---

## 🎯 Casi d'Uso

### Scenario 1: Studente Triennale al 1° Anno

**v1.0:**
❌ Non supportato (solo Magistrale)

**v2.0:**
✅ Seleziona "Computer Engineering"
✅ Inserisce 6-8 esami completati
✅ Ottiene proiezione del voto finale
✅ Pianifica strategia per gli esami futuri

### Scenario 2: Studente con Molti Esami

**v1.0:**
😰 Deve inserire 14 voti manualmente
⏱️ Tempo: ~5 minuti
❌ Nessun salvataggio

**v2.0:**
😊 Crea file Excel con tutti i voti
⏱️ Tempo: 30 secondi per import
✅ File riutilizzabile per aggiornamenti

### Scenario 3: Analisi "What-If"

**v1.0:**
🔄 Riesegui tutto da zero
📊 Confronto manuale dei risultati

**v2.0:**
💾 Salva simulazione 1 (voti attuali)
🔄 Cambia alcuni voti
💾 Salva simulazione 2
📊 Confronta nello storico con un click

### Scenario 4: Presentazione Risultati

**v1.0:**
📝 Copia risultati testuali
🎨 Crea grafici manualmente in Excel

**v2.0:**
📸 Grafici professionali auto-generati
📄 Export JSON/CSV per report
🖼️ PNG ad alta risoluzione pronto per slide

---

## 📊 Metriche del Codice

| Metrica | v1.0 | v2.0 | Differenza |
|---------|------|------|------------|
| **Linee di Codice** | ~110 | ~650+ | +491% |
| **File** | 1 | 9 | +800% |
| **Funzionalità** | 6 | 25+ | +317% |
| **Corsi Supportati** | 1 | 6+ | +500% |
| **Formati Input** | 1 | 4 | +300% |
| **Grafici** | 2 | 4 | +100% |
| **Statistiche** | 3 | 11 | +267% |
| **Doc (righe)** | 3 | 1000+ | +33233% |

---

## 🚀 Performance

### Tempo di Esecuzione

**Input Manuale (14 esami):**
- v1.0: ~5 minuti
- v2.0: ~5 minuti (uguale, ma con UI migliore)

**Import da File:**
- v1.0: ❌ Non supportato
- v2.0: ✅ ~2 secondi

**Generazione Grafici:**
- v1.0: ~3 secondi (2 grafici)
- v2.0: ~5 secondi (4 grafici professionali)

**Export Risultati:**
- v1.0: ~0.5 secondi (Pickle)
- v2.0: ~1 secondo (JSON + CSV + PNG)

---

## 🎓 Conclusioni

### Punti di Forza v2.0

1. **User Experience** ⭐⭐⭐⭐⭐
   - Interfaccia bellissima e intuitiva
   - Feedback visuale chiaro
   - Workflow guidato

2. **Flessibilità** ⭐⭐⭐⭐⭐
   - 6+ corsi di laurea
   - 4 metodi di input
   - Facilmente estensibile

3. **Funzionalità** ⭐⭐⭐⭐⭐
   - Statistiche avanzate
   - Visualizzazioni professionali
   - Export multipli formati

4. **Documentazione** ⭐⭐⭐⭐⭐
   - Completa e dettagliata
   - Multilingua (IT/EN)
   - Esempi pratici

5. **Qualità Codice** ⭐⭐⭐⭐⭐
   - Architettura OOP
   - Modulare e testabile
   - Best practices

### Quando Usare Quale Versione?

**Usa v1.0 se:**
- ❌ Probabilmente mai... v2.0 è meglio in tutto!

**Usa v2.0 se:**
- ✅ Vuoi un'esperienza utente moderna
- ✅ Hai bisogno di supporto per più corsi
- ✅ Vuoi importare voti da file
- ✅ Ti servono statistiche avanzate
- ✅ Vuoi grafici professionali
- ✅ Necessiti di documentazione completa

---

## 📈 Roadmap Futura

Possibili migliorie per v3.0:

- 🌐 Web interface (Flask/Django)
- 📱 App mobile
- 🤖 ML per predizioni avanzate
- 📊 Dashboard interattivi (Plotly)
- 🔗 API REST
- 💾 Database SQL
- 🌍 Supporto altri sistemi di voto (GPA)
- 📧 Report via email
- 📅 Pianificatore esami
- 🎯 Goal tracker

---

**Versione documento:** 1.0  
**Data:** Novembre 2024  
**Autore:** Ilyas Hamza
