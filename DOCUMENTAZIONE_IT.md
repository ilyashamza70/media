# 🎓 Documentazione Completa - Calcolatore Voto di Laurea

## Indice
1. [Introduzione](#introduzione)
2. [Installazione Dettagliata](#installazione-dettagliata)
3. [Guida Passo-Passo](#guida-passo-passo)
4. [Formati File Supportati](#formati-file-supportati)
5. [Algoritmi di Calcolo](#algoritmi-di-calcolo)
6. [Interpretazione Risultati](#interpretazione-risultati)
7. [Esempi Pratici](#esempi-pratici)
8. [FAQ](#faq)

## Introduzione

Il **Calcolatore Avanzato Voto di Laurea** è uno strumento completo progettato per aiutare gli studenti universitari italiani a:

- Calcolare la media ponderata e aritmetica dei voti
- Prevedere il voto di laurea finale
- Analizzare statisticamente il proprio percorso accademico
- Visualizzare graficamente i propri risultati
- Gestire voti per diversi corsi di laurea (Triennale e Magistrale)

### Perché Usare Questo Strumento?

- **Precisione**: Calcoli accurati basati sul sistema universitario italiano
- **Flessibilità**: Supporta sia lauree triennali che magistrali
- **Facilità**: Interfaccia intuitiva e colorata
- **Completezza**: Import da file, export risultati, storico simulazioni
- **Professionalità**: Grafici dettagliati pronti per presentazioni

## Installazione Dettagliata

### Passo 1: Verifica Prerequisiti

Prima di iniziare, assicurati di avere:

```bash
# Verifica versione Python (deve essere 3.8 o superiore)
python --version
# oppure
python3 --version
```

Se Python non è installato:
- **Windows**: Scarica da [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python3`
- **Linux**: `sudo apt-get install python3 python3-pip`

### Passo 2: Clona il Repository

```bash
# Usando HTTPS
git clone https://github.com/ilyashamza70/media.git

# Oppure usando SSH
git clone git@github.com:ilyashamza70/media.git

# Entra nella directory
cd media
```

### Passo 3: Crea un Ambiente Virtuale (Consigliato)

```bash
# Crea ambiente virtuale
python -m venv venv

# Attiva ambiente virtuale
# Su Windows:
venv\Scripts\activate
# Su macOS/Linux:
source venv/bin/activate
```

### Passo 4: Installa le Dipendenze

```bash
pip install -r requirements.txt
```

Le librerie installate sono:
- **pandas**: Gestione dati e import file
- **numpy**: Calcoli numerici e statistici
- **matplotlib**: Creazione grafici
- **openpyxl**: Supporto file Excel
- **rich**: Interfaccia colorata e interattiva

### Passo 5: Verifica Installazione

```bash
python grade_calculator.py
```

Se vedi il menu principale, l'installazione è riuscita! 🎉

## Guida Passo-Passo

### Primo Utilizzo: Inserimento Manuale

1. **Avvia il programma**
   ```bash
   python grade_calculator.py
   ```

2. **Seleziona il tipo di corso**
   - Digita `1` per Triennale (180 CFU)
   - Digita `2` per Magistrale (120 CFU)

3. **Seleziona il corso di laurea**
   - Vedrai una lista di corsi disponibili
   - Digita il numero corrispondente al tuo corso

4. **Visualizza gli esami**
   - Il programma mostrerà tutti gli esami con i rispettivi CFU

5. **Inserisci i voti**
   - Per ogni esame, inserisci il voto (18-30)
   - Per 30 e Lode, scrivi `30L`

6. **Visualizza i risultati**
   - Media ponderata
   - Media aritmetica
   - Voto di laurea previsto
   - Statistiche dettagliate

7. **Genera grafici** (opzionale)
   - Rispondi `y` per visualizzare i grafici
   - I grafici vengono salvati automaticamente

8. **Esporta risultati** (opzionale)
   - Rispondi `y` per esportare in JSON e CSV

### Utilizzo Avanzato: Import da File

#### Opzione 1: File TXT

1. **Crea file di esempio**
   ```bash
   python grade_calculator.py
   # Seleziona tipo e corso
   # Scegli opzione 3 (Crea file di esempio)
   ```

2. **Modifica `sample_grades.txt`**
   ```text
   # Formato: Nome Esame = Voto
   Mathematical Analysis I = 28
   Computer Programming = 30L
   Data Structures = 27
   Physics I = 25
   ```

3. **Importa il file**
   ```bash
   python grade_calculator.py
   # Seleziona tipo e corso
   # Scegli opzione 2 (Import da file)
   # Inserisci: sample_grades.txt
   ```

#### Opzione 2: File CSV

1. **Crea `voti.csv` con Excel o editor testo**
   ```csv
   Corso,Voto
   Mathematical Analysis I,28
   Computer Programming,30L
   Data Structures,27
   Physics I,25
   ```

2. **Importa**
   ```bash
   python grade_calculator.py
   # Seleziona opzione 2 (Import da file)
   # Inserisci: voti.csv
   ```

#### Opzione 3: File Excel

1. **Crea file Excel** con due colonne:
   - Colonna A: Nome Corso
   - Colonna B: Voto

2. **Salva come** `.xlsx` o `.xls`

3. **Importa**
   ```bash
   python grade_calculator.py
   # Seleziona opzione 2 (Import da file)
   # Inserisci: voti.xlsx
   ```

### Visualizzazione Storico

Per vedere tutte le simulazioni precedenti:

```bash
python grade_calculator.py
# Seleziona tipo e corso
# Scegli opzione 4 (Visualizza storico)
```

## Formati File Supportati

### 1. TXT (Text File)

**Vantaggi**: Semplice, modificabile con qualsiasi editor
**Formato**:
```text
# Commenti iniziano con #
Nome Corso = Voto

# Esempi
Mathematical Analysis I = 28
Computer Programming = 30L
Data Structures = 27.5
```

**Note**:
- Un esame per riga
- Formato: `Nome Esame = Voto`
- Supporta decimali (es: 27.5)
- Usa `30L` per 30 e Lode

### 2. CSV (Comma-Separated Values)

**Vantaggi**: Compatibile con Excel, Google Sheets
**Formato**:
```csv
Corso,Voto
Mathematical Analysis I,28
Computer Programming,30L
Data Structures,27
```

**Note**:
- Prima riga: intestazione (Corso,Voto)
- Valori separati da virgola
- Supporta 30L per la lode

### 3. Excel (XLSX/XLS)

**Vantaggi**: Interfaccia grafica, formule, formattazione
**Struttura**:
| Corso | Voto |
|-------|------|
| Mathematical Analysis I | 28 |
| Computer Programming | 30L |
| Data Structures | 27 |

**Note**:
- Due colonne: Corso e Voto
- Prima riga con intestazioni
- Supporta 30L per la lode

## Algoritmi di Calcolo

### Media Ponderata

La media ponderata tiene conto dei CFU di ogni esame:

```
Media_Ponderata = Σ(Voto_i × CFU_i) / Σ(CFU_i)
```

**Esempio**:
- Analisi Matematica I: 28 (12 CFU) → 28 × 12 = 336
- Programmazione: 30 (12 CFU) → 30 × 12 = 360
- Strutture Dati: 27 (9 CFU) → 27 × 9 = 243

```
Media_Ponderata = (336 + 360 + 243) / (12 + 12 + 9)
                = 939 / 33
                = 28.45
```

### Media Aritmetica

La media aritmetica è la semplice media dei voti:

```
Media_Aritmetica = Σ(Voti) / Numero_Esami
```

**Esempio** (stessi voti sopra):
```
Media_Aritmetica = (28 + 30 + 27) / 3
                 = 85 / 3
                 = 28.33
```

**Nota**: Per la media aritmetica, 30L viene contato come 30.

### Voto di Laurea

Il calcolo del voto di laurea segue il sistema italiano:

1. **Conversione base**: Converte la media ponderata in base 110
   ```
   Voto_Base = (Media_Ponderata / 30) × 110
   ```

2. **Bonus per le lodi**: Aggiunge un bonus per ogni 30L
   ```
   Bonus = min(Numero_30L × 0.5, 5)
   ```
   - Ogni 30L vale 0.5 punti
   - Massimo 5 punti di bonus

3. **Voto finale**:
   ```
   Voto_Laurea = min(Voto_Base + Bonus, 110)
   ```
   - Non può superare 110

**Esempio Completo**:
- Media ponderata: 28.45
- Numero 30L: 3

```
Voto_Base = (28.45 / 30) × 110 = 104.32
Bonus = min(3 × 0.5, 5) = 1.5
Voto_Laurea = min(104.32 + 1.5, 110) = 105.82
```

### Statistiche Calcolate

Il programma calcola anche:

1. **Voto Minimo**: Il voto più basso ottenuto
2. **Voto Massimo**: Il voto più alto ottenuto
3. **Mediana**: Il valore centrale dei voti
4. **Deviazione Standard**: Misura della dispersione dei voti
   - Bassa → voti simili tra loro
   - Alta → voti molto variabili
5. **Contatori**:
   - Numero di 30 e Lode
   - Numero di 30
   - Numero di voti sotto 24

## Interpretazione Risultati

### Media Ponderata vs Aritmetica

- **Media Ponderata > Media Aritmetica**: 
  - Hai preso voti alti in esami con molti CFU ✅
  - Ottimo! Hai dato priorità agli esami più importanti

- **Media Ponderata < Media Aritmetica**:
  - Hai preso voti più bassi in esami con molti CFU
  - Consiglio: Concentrati sugli esami con più crediti

- **Differenza minima**:
  - Performance costante su tutti gli esami

### Voto di Laurea

- **110+**: 105-110
  - Eccellente! Possibilità concreta di 110 e Lode
  
- **105-109**: 
  - Ottimo percorso! Possibilità di 110

- **100-104**:
  - Buon risultato! Obiettivo: mantenere o migliorare

- **95-99**:
  - Sopra la media. C'è margine di miglioramento

- **< 95**:
  - Buon inizio. Focus su esami con molti CFU

### Statistiche

**Deviazione Standard**:
- < 2: Voti molto costanti (ottimo)
- 2-4: Buona costanza
- > 4: Alta variabilità (normale, ma migliorabile)

**Voti sotto 24**:
- 0-2: Eccellente
- 3-5: Buono
- > 5: Opportunità di miglioramento negli esami rimanenti

## Esempi Pratici

### Esempio 1: Studente Triennale - Primo Anno

**Scenario**: Studente di Ingegneria Informatica, primo anno

```bash
python grade_calculator.py
# Seleziona: 1 (Triennale)
# Seleziona: 1 (Computer Engineering)
# Seleziona: 1 (Inserimento manuale)
```

**Voti inseriti**:
- Mathematical Analysis I (12 CFU): 26
- Physics I (12 CFU): 24
- Computer Programming (12 CFU): 28
- Linear Algebra (9 CFU): 27

**Risultati**:
```
Media Ponderata: 26.27/30
Media Aritmetica: 26.25/30
Voto di Laurea Previsto: 96.32/110
```

**Analisi**: Buon inizio! Per arrivare a 100+, punta a 27-28 di media nei prossimi esami.

### Esempio 2: Studente Magistrale - Import da File

**Scenario**: Studente di Embedded Systems con voti in Excel

1. **Crea `voti_magistrale.xlsx`**:
   | Corso | Voto |
   |-------|------|
   | Electronics for embedded systems | 30L |
   | Computer architectures | 28 |
   | Operating systems | 29 |
   | Software engineering | 30 |

2. **Esegui**:
   ```bash
   python grade_calculator.py
   # Seleziona: 2 (Magistrale)
   # Seleziona: 1 (Embedded Systems)
   # Seleziona: 2 (Import)
   # File: voti_magistrale.xlsx
   ```

3. **Risultati**: Media alta con bonus per 30L!

### Esempio 3: Simulazione "What-If"

**Scenario**: Vuoi sapere come cambierebbe il voto con voti diversi

1. **Prima simulazione**: Inserisci voti attuali
2. **Salva risultati**: Sì all'export
3. **Seconda simulazione**: Cambia alcuni voti
4. **Confronta**: Guarda lo storico (opzione 4)

## FAQ

### Domande Generali

**Q: Il programma supporta altri sistemi di voto (es. 0-100)?**
A: No, è progettato per il sistema universitario italiano (18-30).

**Q: Posso aggiungere il mio corso di laurea?**
A: Sì! Modifica `degree_courses.py` seguendo il formato esistente.

**Q: I dati sono salvati online?**
A: No, tutto è salvato localmente sul tuo computer.

**Q: Posso eliminare lo storico?**
A: Sì, elimina il file `simulation_log.json`.

### Problemi Tecnici

**Q: "ModuleNotFoundError: No module named 'pandas'"**
A: Esegui `pip install -r requirements.txt`

**Q: I grafici non si aprono**
A: Su Linux, installa: `sudo apt-get install python3-tk`

**Q: Errore durante import file**
A:
1. Verifica che il file esista nella directory corretta
2. Controlla il formato del file
3. Assicurati che l'encoding sia UTF-8

**Q: Il programma è lento**
A: Normale con molti esami e grafici. Disabilita grafici per velocizzare.

### Calcoli e Risultati

**Q: Perché media ponderata ≠ media aritmetica?**
A: La ponderata considera i CFU di ogni esame, è più accurata.

**Q: Il voto di laurea è garantito?**
A: No, è una previsione. Il voto finale dipende anche da:
   - Tesi
   - Valutazione commissione
   - Punti extra dell'università

**Q: Come migliorare il voto di laurea previsto?**
A:
1. Focus su esami con molti CFU
2. Punta a voti > 27
3. Cerca le lodi (30L)

**Q: Cosa significa "31" nei file salvati?**
A: È il codice interno per 30L (30 e Lode).

### File e Export

**Q: Dove vengono salvati i file?**
A: Nella stessa directory del programma.

**Q: Posso condividere i risultati?**
A: Sì, usa i file JSON o CSV esportati, o gli screenshot dei grafici.

**Q: Come apro i file JSON?**
A: Con editor testo, o online su [jsonviewer.stack.hu](https://jsonviewer.stack.hu)

**Q: I grafici sono modificabili?**
A: Sì, sono salvati come PNG, modificabili con qualsiasi editor immagini.

## Supporto e Contatti

### Hai Trovato un Bug?

Apri un issue su GitHub:
1. Vai su https://github.com/ilyashamza70/media/issues
2. Clicca "New Issue"
3. Descrivi il problema con dettagli

### Vuoi Proporre una Feature?

Apri una Pull Request o un issue "Feature Request"

### Contatti

- **GitHub**: [@ilyashamza70](https://github.com/ilyashamza70)
- **Repository**: [ilyashamza70/media](https://github.com/ilyashamza70/media)

---

📚 **Ultimo aggiornamento**: Novembre 2024
✨ **Versione**: 2.0.0
