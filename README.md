# 🎓 Calcolatore Avanzato Voto di Laurea

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un calcolatore avanzato e simulatore del voto di laurea con interfaccia interattiva, supporto per multiple corsi di laurea (Triennale e Magistrale), e capacità di importazione da file.

## 📁 Struttura Repository Organizzata

Il progetto è ora organizzato in modo chiaro e professionale:
- **`src/`** - Codice sorgente Python
- **`docs/`** - Tutta la documentazione
- **`examples/`** - File di esempio per import
- **`data/`** - Log e dati generati

Vedi la sezione [Struttura del Progetto](#-struttura-del-progetto) per i dettagli completi.

## ✨ Caratteristiche Principali

- 🎯 **Supporto Completo**: Corsi di laurea Triennale (180 CFU) e Magistrale (120 CFU)
- 📊 **Calcoli Avanzati**: Media ponderata, media aritmetica, voto di laurea previsto
- 📈 **Statistiche Dettagliate**: Min, max, mediana, deviazione standard, analisi voti
- 🎨 **Interfaccia Bellissima**: UI colorata e interattiva con Rich library
- 📁 **Import Multi-formato**: Supporto per TXT, CSV, Excel (XLSX)
- 📉 **Grafici Professionali**: Visualizzazioni dettagliate con matplotlib
- 💾 **Persistenza Dati**: Salvataggio automatico storico simulazioni
- 🔄 **Export Risultati**: Esportazione in JSON e CSV

## 🚀 Installazione Rapida

### Prerequisiti
- Python 3.8 o superiore
- pip (gestore pacchetti Python)

### Installazione

```bash
# Clona il repository
git clone https://github.com/ilyashamza70/media.git
cd media

# Installa le dipendenze
pip install -r requirements.txt
```

## 📖 Guida all'Uso

### Avvio del Programma

```bash
# Dalla directory principale del progetto
python main.py

# Oppure direttamente dal modulo src
python src/grade_calculator.py
```

### Modalità di Input

#### 1. **Inserimento Manuale**
Inserisci i voti direttamente tramite prompt interattivo:
```
Seleziona tipo corso → Seleziona corso specifico → Inserisci voti uno per uno
```

#### 2. **Import da File TXT**
Crea un file `voti.txt` con il formato:
```text
# Formato: Nome Corso = Voto
Mathematical Analysis I = 28
Computer Programming = 30L
Data Structures = 27
```

#### 3. **Import da CSV**
Crea un file `voti.csv`:
```csv
Corso,Voto
Mathematical Analysis I,28
Computer Programming,30L
Data Structures,27
```

#### 4. **Import da Excel**
Crea un file Excel con due colonne: `Corso` e `Voto`

### Corsi di Laurea Disponibili

#### Triennale (180 CFU)
- **Computer Engineering**: Ingegneria Informatica completa
- **Information Technology**: IT con focus su sviluppo e reti
- **Mathematics**: Matematica pura e applicata

#### Magistrale (120 CFU)
- **Embedded Systems**: Sistemi embedded e IoT
- **Computer Science**: Informatica avanzata con AI/ML
- **Data Science**: Data science e analytics

## 📊 Calcoli Eseguiti

### 1. Media Ponderata
```
Media Ponderata = Σ(Voto × CFU) / Σ(CFU)
```

### 2. Media Aritmetica
```
Media Aritmetica = Σ(Voti) / Numero_Esami
```

### 3. Voto di Laurea
```
Voto Base = (Media_Ponderata / 30) × 110
Bonus Lode = min(Numero_30L × 0.5, 5)
Voto Finale = min(Voto_Base + Bonus_Lode, 110)
```

## 📈 Visualizzazioni

Il programma genera grafici professionali che includono:

1. **Confronto Medie**: Visualizza media ponderata vs aritmetica
2. **Voto di Laurea**: Mostra il voto di laurea previsto con scale colorate
3. **Distribuzione Voti**: Istogramma della distribuzione dei voti
4. **Top Voti per Corso**: Classifica dei migliori voti ottenuti

![Esempio Grafici](https://via.placeholder.com/800x600.png?text=Grade+Analysis+Charts)

## 💾 File Generati

### Durante l'Esecuzione
- `sample_grades.txt/csv/xlsx`: File di esempio per l'import
- `grade_analysis_YYYYMMDD_HHMMSS.png`: Grafici dell'analisi
- `results_YYYYMMDD_HHMMSS.json`: Risultati dettagliati in JSON
- `grades_YYYYMMDD_HHMMSS.csv`: Tabella voti esportata
- `simulation_log.json`: Storico di tutte le simulazioni

## 🎯 Esempi d'Uso

### Esempio 1: Calcolo Rapido
```bash
python main.py
# Seleziona: 1 (Triennale)
# Seleziona: 1 (Computer Engineering)
# Seleziona: 1 (Inserimento manuale)
# Inserisci i voti quando richiesto
```

### Esempio 2: Import da File
```bash
python main.py
# Seleziona: 2 (Magistrale)
# Seleziona: 1 (Embedded Systems)
# Seleziona: 2 (Import da file)
# Inserisci: examples/example_grades.txt
```

### Esempio 3: Crea File di Esempio
```bash
python main.py
# Seleziona tipo corso
# Seleziona corso specifico
# Seleziona: 3 (Crea file di esempio)
# Modifica i file generati e riesegui con opzione 2
```

## 🔧 Struttura del Progetto

```
media/
├── src/                     # Codice sorgente
│   ├── grade_calculator.py  # Programma principale
│   ├── degree_courses.py    # Database corsi di laurea
│   └── trial.py             # Versione originale (legacy)
├── docs/                    # Documentazione
│   ├── COMPARISON.md        # Confronto versioni
│   ├── DOCUMENTAZIONE_IT.md # Documentazione italiana dettagliata
│   ├── FEATURES.md          # Lista delle funzionalità
│   ├── PROJECT_SUMMARY.md   # Sommario del progetto
│   ├── USER_GUIDE.md        # Guida utente dettagliata
│   └── README_EN.md         # README in inglese
├── examples/                # File di esempio
│   ├── example_grades.csv   # Esempio formato CSV
│   ├── example_grades.txt   # Esempio formato TXT
│   └── DEMO_OUTPUT.txt      # Output demo
├── data/                    # Dati e log
│   ├── simulation_log.json  # Storico simulazioni (JSON)
│   └── simulation_log.pkl   # Storico simulazioni (pickle)
├── main.py                  # Script principale per avviare l'applicazione
├── requirements.txt         # Dipendenze Python
├── LICENSE                  # Licenza MIT
├── README.md               # Questo file
├── BRANCH_STATUS.md        # Stato del repository e branch
├── ToDoList.txt           # Note di sviluppo
└── .gitignore             # File da ignorare in git
```

### Descrizione delle Directory

- **`src/`**: Contiene tutto il codice sorgente dell'applicazione
  - `grade_calculator.py`: Il calcolatore principale con interfaccia Rich
  - `degree_courses.py`: Database dei corsi di laurea con relativi CFU
  - `trial.py`: Versione originale legacy per riferimento

- **`docs/`**: Tutta la documentazione del progetto
  - Documentazione in italiano e inglese
  - Guide utente e feature list
  - Comparazioni tra versioni

- **`examples/`**: File di esempio per import e test
  - Esempi in formato TXT, CSV per l'importazione voti
  - Output di demo per riferimento

- **`data/`**: File di dati generati dall'applicazione
  - Log delle simulazioni in formato JSON e pickle
  - Vengono creati automaticamente dall'applicazione
```

## 📚 API e Moduli

### GradeCalculator Class
```python
calc = GradeCalculator()
calc.select_degree_type()           # Seleziona tipo corso
calc.select_degree_course()         # Seleziona corso specifico
calc.input_grades_manual()          # Input manuale
calc.import_grades_from_file(path)  # Import da file
calc.calculate_weighted_average()   # Calcola media ponderata
calc.calculate_graduation_grade()   # Calcola voto laurea
calc.plot_visualizations()          # Genera grafici
calc.export_results()               # Esporta risultati
```

## 🎨 Personalizzazione

### Aggiungere Nuovi Corsi di Laurea

Modifica `degree_courses.py`:

```python
MAGISTRALE_COURSES["Nuovo Corso"] = {
    "type": "magistrale",
    "total_credits": 120,
    "courses": {
        "Esame 1": 12,
        "Esame 2": 9,
        # ... altri esami
        "Final project work": 30
    }
}
```

## 🐛 Troubleshooting

### Problema: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Problema: File non trovato durante import
- Verifica che il file sia nella stessa directory del programma
- Usa percorsi assoluti: `/path/to/file.txt`
- Controlla l'encoding del file (UTF-8 consigliato)

### Problema: Grafici non visualizzati
```bash
# Su Linux, potrebbe servire un backend
sudo apt-get install python3-tk
```

## 🤝 Contribuire

I contributi sono benvenuti! Per contribuire:

1. Fai un Fork del progetto
2. Crea un Branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al Branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📝 Changelog

### Versione 2.0.0 (Corrente)
- ✨ Interfaccia completamente ridisegnata con Rich
- 🎓 Supporto per Triennale e Magistrale
- 📁 Import multi-formato (TXT, CSV, Excel)
- 📊 Statistiche avanzate
- 🎨 Grafici professionali migliorati
- 💾 Sistema di logging e export
- 🌍 Multiple corsi di laurea preconfigurati

### Versione 1.0.0 (Legacy)
- Calcolatore base per Embedded Systems
- Input manuale sequenziale
- Grafici semplici

## 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file `LICENSE` per i dettagli.

## 👨‍💻 Autore

**Ilyas Hamza**
- GitHub: [@ilyashamza70](https://github.com/ilyashamza70)

## 🙏 Ringraziamenti

- Rich library per l'interfaccia colorata
- Matplotlib per le visualizzazioni
- Pandas per la gestione dati
- La comunità open source

---

⭐ Se questo progetto ti è stato utile, lascia una stella su GitHub!
