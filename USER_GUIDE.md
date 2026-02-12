# 📘 Guida Utente Rapida

## 🚀 Quick Start (5 minuti)

### Installazione Veloce
```bash
git clone https://github.com/ilyashamza70/media.git
cd media
pip install -r requirements.txt
python grade_calculator.py
```

## 🎯 Modalità d'Uso

### 1️⃣ Inserimento Manuale (Più Semplice)

**Quando usarlo**: Primo utilizzo, pochi esami da inserire

**Passi**:
1. Avvia: `python grade_calculator.py`
2. Scegli tipo corso (1=Triennale, 2=Magistrale)
3. Scegli corso specifico dalla lista
4. Inserisci voti uno per uno quando richiesto
5. Visualizza risultati e grafici

**Esempio**:
```
Scelta: 1 (Triennale)
Scelta: 1 (Computer Engineering)
Scelta: 1 (Inserimento manuale)
Mathematical Analysis I: 28
Physics I: 26
[...]
```

### 2️⃣ Import da File TXT (Consigliato)

**Quando usarlo**: Hai già i voti in un file, molti esami

**Passi**:
1. Crea file `miei_voti.txt`:
   ```text
   Mathematical Analysis I = 28
   Computer Programming = 30L
   Data Structures = 27
   ```

2. Avvia e importa:
   ```bash
   python grade_calculator.py
   # Scegli tipo e corso
   # Opzione: 2 (Import da file)
   # File: miei_voti.txt
   ```

### 3️⃣ Import da Excel (Più Comodo)

**Quando usarlo**: Preferisci interfaccia grafica

**Passi**:
1. Apri Excel/Google Sheets
2. Crea due colonne: `Corso` e `Voto`
3. Inserisci i tuoi voti
4. Salva come `.xlsx`
5. Importa nel programma

### 4️⃣ Crea File di Esempio (Per Iniziare)

**Quando usarlo**: Non sai come formattare i file

**Passi**:
```bash
python grade_calculator.py
# Scegli tipo e corso
# Opzione: 3 (Crea file di esempio)
```

Questo crea 3 file di esempio che puoi modificare:
- `sample_grades.txt`
- `sample_grades.csv`
- `sample_grades.xlsx`

## 📊 Capire i Risultati

### Dashboard Risultati

Dopo il calcolo vedrai:

```
RISULTATI CALCOLO
╭────────────────────────────────────╮
│ Media Ponderata      │     28.50/30 │
│ Media Aritmetica     │     28.33/30 │
│ Voto di Laurea       │   105.28/110 │
╰────────────────────────────────────╯
```

### Cosa Significano

- **Media Ponderata**: Tiene conto dei CFU (più importante!)
- **Media Aritmetica**: Semplice media dei voti
- **Voto di Laurea**: Previsione del voto finale (può variare ±3 punti)

### Grafici Generati

1. **Confronto Medie**: Barre colorate con le due medie
2. **Voto di Laurea**: Visualizzazione del voto previsto
3. **Distribuzione Voti**: Istogramma dei tuoi voti
4. **Top 10 Corsi**: I tuoi migliori voti

## 💡 Tips e Trucchi

### Per Ottenere 110
```
Calcolo approssimativo:
- Media 28+ → Voto base ~103
- 3+ Lodi → Bonus +1.5
- Tesi eccellente → +3/5
= 107.5+ (ottima possibilità di 110L!)
```

### Per Migliorare la Media
1. **Priorità**: Esami con più CFU
2. **Target**: Punta sempre a 27+
3. **Lodi**: Ogni 30L conta!

### Quando Usare lo Storico
- Confrontare progressi nel tempo
- Simulare scenari "what-if"
- Tenere traccia dei miglioramenti

## 🔧 Risoluzione Problemi

### Problema: Errore import file
**Soluzione**:
- Verifica che il file sia nella stessa cartella del programma
- Usa percorso completo: `/path/to/file.txt`
- Controlla non ci siano errori di battitura nei nomi corsi

### Problema: Voto non accettato
**Soluzione**:
- Usa voti da 18 a 30
- Per 30 e Lode scrivi: `30L` (non 31)
- No decimali estremi (es: 27.5 va bene, 27.123 no)

### Problema: Grafici non si aprono
**Soluzione**:
```bash
# Su Linux
sudo apt-get install python3-tk

# Su Mac
brew install python-tk

# Su Windows
# Reinstalla Python con opzione "tcl/tk"
```

## 📁 File Generati

Il programma crea automaticamente:

| File | Contenuto |
|------|-----------|
| `grade_analysis_*.png` | Grafici visualizzazioni |
| `results_*.json` | Risultati dettagliati |
| `grades_*.csv` | Tabella voti |
| `simulation_log.json` | Storico simulazioni |

**Nota**: `*` = timestamp (data e ora)

## 🎓 Corsi Disponibili

### Triennale (180 CFU)
- Computer Engineering
- Information Technology  
- Mathematics

### Magistrale (120 CFU)
- Embedded Systems
- Computer Science
- Data Science

**Vuoi aggiungere il tuo corso?** Vedi `DOCUMENTAZIONE_IT.md`

## ⌨️ Shortcuts e Comandi

### Durante l'esecuzione
- `Ctrl+C`: Interrompi programma
- `Enter`: Conferma con valore di default
- `y/n`: Conferma sì/no

### Voti speciali
- `30L` o `30 e Lode`: 30 con lode
- Range: `18` - `30`
- Decimali: Supportati (es: `27.5`)

## 🎯 Workflow Consigliato

### Per Studenti del Primo Anno
1. Usa inserimento manuale (pochi esami)
2. Salva risultati dopo ogni sessione
3. Usa storico per tracciare progressi

### Per Studenti degli Anni Successivi
1. Crea file Excel con tutti i voti
2. Aggiorna file ad ogni esame
3. Importa file per calcoli veloci
4. Confronta con storico per vedere miglioramenti

### Per Laureandi
1. Inserisci tutti i voti finali
2. Genera tutti i grafici
3. Esporta risultati in JSON/CSV
4. Usa grafici per presentazioni

## 📞 Supporto

**Problemi?**
- 📖 Leggi `DOCUMENTAZIONE_IT.md` (completa)
- 🐛 Apri issue su GitHub
- 💬 Contatta [@ilyashamza70](https://github.com/ilyashamza70)

**Suggerimenti?**
- ⭐ Lascia una stella su GitHub
- 🔀 Apri Pull Request
- 💡 Proponi feature via Issue

---

**Versione**: 2.0.0 | **Ultimo aggiornamento**: Novembre 2024
