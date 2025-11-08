#!/usr/bin/env python3
"""
Enhanced Grade Calculator and Simulator
Supports both Bachelor's (Triennale) and Master's (Magistrale) degrees
with interactive interface and file import capabilities.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import track
from rich import box
from degree_courses import get_all_courses, get_course_info, list_courses_by_type

console = Console()

class GradeCalculator:
    """Advanced grade calculator with multiple features."""
    
    def __init__(self):
        self.log_file = 'simulation_log.json'
        self.degree_course = None
        self.degree_type = None
        self.courses = {}
        self.grades = {}
        
    def display_welcome(self):
        """Display welcome message with styled interface."""
        console.clear()
        welcome_text = """
[bold cyan]╔══════════════════════════════════════════════════════════════╗[/bold cyan]
[bold cyan]║[/bold cyan]  [bold yellow]🎓 CALCOLATORE AVANZATO VOTO DI LAUREA 🎓[/bold yellow]              [bold cyan]║[/bold cyan]
[bold cyan]║[/bold cyan]                                                              [bold cyan]║[/bold cyan]
[bold cyan]║[/bold cyan]  [white]Calcola media ponderata, aritmetica e voto finale[/white]     [bold cyan]║[/bold cyan]
[bold cyan]║[/bold cyan]  [white]Supporta Triennale e Magistrale[/white]                       [bold cyan]║[/bold cyan]
[bold cyan]║[/bold cyan]  [white]Import da file TXT, CSV, Excel[/white]                         [bold cyan]║[/bold cyan]
[bold cyan]╚══════════════════════════════════════════════════════════════╝[/bold cyan]
"""
        console.print(welcome_text)
        
    def select_degree_type(self):
        """Let user select between Bachelor's and Master's degree."""
        console.print("\n[bold]Seleziona il tipo di corso:[/bold]")
        console.print("1. [cyan]Triennale[/cyan] (Bachelor's - 180 CFU)")
        console.print("2. [magenta]Magistrale[/magenta] (Master's - 120 CFU)")
        
        choice = Prompt.ask("\nScelta", choices=["1", "2"], default="1")
        
        if choice == "1":
            self.degree_type = "triennale"
            console.print("[green]✓[/green] Selezionato: [cyan]Triennale[/cyan]")
        else:
            self.degree_type = "magistrale"
            console.print("[green]✓[/green] Selezionato: [magenta]Magistrale[/magenta]")
            
    def select_degree_course(self):
        """Let user select a specific degree course."""
        available_courses = list_courses_by_type(self.degree_type)
        
        if not available_courses:
            console.print("[red]Nessun corso disponibile per questo tipo.[/red]")
            return False
            
        console.print(f"\n[bold]Corsi di Laurea {self.degree_type.capitalize()} disponibili:[/bold]")
        
        course_list = list(available_courses.keys())
        for idx, course_name in enumerate(course_list, 1):
            total_credits = available_courses[course_name]["total_credits"]
            num_exams = len(available_courses[course_name]["courses"])
            console.print(f"{idx}. [yellow]{course_name}[/yellow] - {total_credits} CFU - {num_exams} esami")
        
        choice = Prompt.ask("\nSeleziona il numero del corso", 
                          choices=[str(i) for i in range(1, len(course_list) + 1)])
        
        self.degree_course = course_list[int(choice) - 1]
        course_info = get_course_info(self.degree_course)
        self.courses = course_info["courses"]
        
        console.print(f"[green]✓[/green] Selezionato: [yellow]{self.degree_course}[/yellow]")
        return True
        
    def display_courses(self):
        """Display selected courses in a formatted table."""
        table = Table(title=f"Esami - {self.degree_course}", box=box.ROUNDED)
        table.add_column("Corso", style="cyan", no_wrap=False)
        table.add_column("CFU", style="magenta", justify="right")
        
        for course, credits in self.courses.items():
            table.add_row(course, str(credits))
        
        total_credits = sum(self.courses.values())
        table.add_row("[bold]TOTALE[/bold]", f"[bold]{total_credits}[/bold]", style="yellow")
        
        console.print("\n")
        console.print(table)
        
    def input_grades_manual(self):
        """Manual input of grades for each course."""
        console.print("\n[bold]Inserisci i voti per ciascun esame:[/bold]")
        console.print("[dim]Usa voti da 18 a 30 (30L per 30 e Lode)[/dim]\n")
        
        for course in track(list(self.courses.keys()), description="Inserimento voti..."):
            while True:
                grade_input = Prompt.ask(f"[cyan]{course}[/cyan] ({self.courses[course]} CFU)")
                
                # Handle 30L (30 e Lode)
                if grade_input.upper() in ["30L", "30 E LODE", "30ELODE"]:
                    self.grades[course] = 31
                    break
                
                try:
                    grade = float(grade_input)
                    if 18 <= grade <= 30:
                        self.grades[course] = grade
                        break
                    else:
                        console.print("[red]Voto non valido. Inserisci un voto tra 18 e 30.[/red]")
                except ValueError:
                    console.print("[red]Input non valido. Inserisci un numero.[/red]")
        
        console.print("\n[green]✓ Voti inseriti con successo![/green]")
        
    def import_grades_from_file(self, file_path):
        """Import grades from a file (txt, csv, or excel)."""
        try:
            file_ext = os.path.splitext(file_path)[1].lower()
            
            if file_ext == '.txt':
                self._import_from_txt(file_path)
            elif file_ext == '.csv':
                self._import_from_csv(file_path)
            elif file_ext in ['.xlsx', '.xls']:
                self._import_from_excel(file_path)
            else:
                console.print("[red]Formato file non supportato. Usa .txt, .csv, o .xlsx[/red]")
                return False
                
            console.print(f"[green]✓ Voti importati da {file_path}[/green]")
            return True
        except Exception as e:
            console.print(f"[red]Errore durante l'importazione: {str(e)}[/red]")
            return False
    
    def _import_from_txt(self, file_path):
        """Import grades from txt file (format: course_name=grade)."""
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if '=' in line:
                    course_name, grade = line.split('=', 1)
                    course_name = course_name.strip()
                    grade = grade.strip()
                    
                    if course_name in self.courses:
                        if grade.upper() in ["30L", "30 E LODE"]:
                            self.grades[course_name] = 31
                        else:
                            self.grades[course_name] = float(grade)
    
    def _import_from_csv(self, file_path):
        """Import grades from CSV file."""
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            course_name = row.iloc[0].strip()
            grade = row.iloc[1]
            
            if course_name in self.courses:
                if isinstance(grade, str) and grade.upper() in ["30L", "30 E LODE"]:
                    self.grades[course_name] = 31
                else:
                    self.grades[course_name] = float(grade)
    
    def _import_from_excel(self, file_path):
        """Import grades from Excel file."""
        df = pd.read_excel(file_path)
        for _, row in df.iterrows():
            course_name = row.iloc[0].strip()
            grade = row.iloc[1]
            
            if course_name in self.courses:
                if isinstance(grade, str) and grade.upper() in ["30L", "30 E LODE"]:
                    self.grades[course_name] = 31
                else:
                    self.grades[course_name] = float(grade)
    
    def create_sample_files(self):
        """Create sample input files for user reference."""
        # Create sample TXT file
        with open('sample_grades.txt', 'w', encoding='utf-8') as f:
            f.write("# Format: Course Name = Grade\n")
            f.write("# Use grades from 18 to 30 (30L for 30 e Lode)\n\n")
            for idx, (course, credits) in enumerate(list(self.courses.items())[:3]):
                f.write(f"{course} = 28\n")
        
        # Create sample CSV file
        sample_data = []
        for course, credits in list(self.courses.items())[:3]:
            sample_data.append([course, 28])
        df = pd.DataFrame(sample_data, columns=['Corso', 'Voto'])
        df.to_csv('sample_grades.csv', index=False)
        
        # Create sample Excel file
        df.to_excel('sample_grades.xlsx', index=False)
        
        console.print("[green]✓ File di esempio creati: sample_grades.txt, sample_grades.csv, sample_grades.xlsx[/green]")
    
    def calculate_weighted_average(self):
        """Calculate weighted average based on credits."""
        if not self.grades:
            return 0
        
        total_weight = sum(self.courses[course] for course in self.grades.keys())
        weighted_sum = sum(grade * self.courses[course] 
                          for course, grade in self.grades.items())
        return weighted_sum / total_weight
    
    def calculate_arithmetic_average(self):
        """Calculate simple arithmetic average."""
        if not self.grades:
            return 0
        
        # Convert 31 (30L) to 30 for arithmetic average
        grades_normalized = [min(grade, 30) for grade in self.grades.values()]
        return sum(grades_normalized) / len(grades_normalized)
    
    def calculate_graduation_grade(self, weighted_avg):
        """Calculate predicted graduation grade."""
        # Base conversion: (weighted_avg / 30) * 110
        base_grade = (weighted_avg / 30) * 110
        
        # Add bonus for 30L grades
        num_lode = sum(1 for grade in self.grades.values() if grade > 30)
        bonus = min(num_lode * 0.5, 5)  # Max 5 points bonus
        
        final_grade = min(base_grade + bonus, 110)
        return final_grade
    
    def calculate_statistics(self):
        """Calculate advanced statistics."""
        if not self.grades:
            return {}
        
        grade_values = [min(grade, 30) for grade in self.grades.values()]
        
        stats = {
            'min_grade': min(grade_values),
            'max_grade': max(grade_values),
            'median': np.median(grade_values),
            'std_dev': np.std(grade_values),
            'num_30L': sum(1 for g in self.grades.values() if g > 30),
            'num_30': sum(1 for g in grade_values if g == 30),
            'num_below_24': sum(1 for g in grade_values if g < 24),
            'num_exams': len(grade_values)
        }
        
        return stats
    
    def display_results(self, weighted_avg, arithmetic_avg, graduation_grade, stats):
        """Display calculation results in a formatted table."""
        console.print("\n")
        console.print(Panel.fit(
            "[bold yellow]RISULTATI CALCOLO[/bold yellow]",
            border_style="yellow"
        ))
        
        # Main results table
        results_table = Table(box=box.ROUNDED, show_header=False)
        results_table.add_column("Metrica", style="cyan", width=30)
        results_table.add_column("Valore", style="yellow", justify="right")
        
        results_table.add_row("Media Ponderata", f"{weighted_avg:.2f}/30")
        results_table.add_row("Media Aritmetica", f"{arithmetic_avg:.2f}/30")
        results_table.add_row("", "")
        results_table.add_row("[bold]Voto di Laurea Previsto[/bold]", 
                            f"[bold]{graduation_grade:.2f}/110[/bold]")
        
        console.print(results_table)
        
        # Statistics table
        console.print("\n[bold]Statistiche:[/bold]")
        stats_table = Table(box=box.SIMPLE)
        stats_table.add_column("Statistica", style="cyan")
        stats_table.add_column("Valore", style="green", justify="right")
        
        stats_table.add_row("Voto Minimo", f"{stats['min_grade']}")
        stats_table.add_row("Voto Massimo", f"{stats['max_grade']}")
        stats_table.add_row("Mediana", f"{stats['median']:.2f}")
        stats_table.add_row("Deviazione Standard", f"{stats['std_dev']:.2f}")
        stats_table.add_row("Numero 30 e Lode", f"{stats['num_30L']}")
        stats_table.add_row("Numero 30", f"{stats['num_30']}")
        stats_table.add_row("Voti < 24", f"{stats['num_below_24']}")
        stats_table.add_row("Totale Esami", f"{stats['num_exams']}")
        
        console.print(stats_table)
        
    def plot_visualizations(self, weighted_avg, arithmetic_avg, graduation_grade):
        """Create enhanced visualizations."""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(f'Analisi Completa - {self.degree_course}', 
                     fontsize=16, fontweight='bold')
        
        # 1. Averages comparison
        ax1 = axes[0, 0]
        averages = [weighted_avg, arithmetic_avg]
        labels = ['Media\nPonderata', 'Media\nAritmetica']
        colors = ['#3498db', '#2ecc71']
        bars1 = ax1.bar(labels, averages, color=colors, edgecolor='black', linewidth=1.5)
        ax1.set_ylabel('Voto', fontsize=12)
        ax1.set_title('Confronto Medie', fontsize=13, fontweight='bold')
        ax1.set_ylim([0, 30])
        ax1.axhline(y=24, color='orange', linestyle='--', alpha=0.5, label='Soglia 24')
        ax1.axhline(y=27, color='green', linestyle='--', alpha=0.5, label='Soglia 27')
        ax1.legend()
        
        # Add value labels on bars
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontweight='bold')
        
        # 2. Graduation grade
        ax2 = axes[0, 1]
        grade_color = '#e74c3c' if graduation_grade < 90 else '#9b59b6' if graduation_grade < 100 else '#f39c12' if graduation_grade < 110 else '#27ae60'
        bar2 = ax2.bar(['Voto di\nLaurea'], [graduation_grade], 
                      color=grade_color, edgecolor='black', linewidth=1.5)
        ax2.set_ylabel('Voto', fontsize=12)
        ax2.set_title('Voto di Laurea Previsto', fontsize=13, fontweight='bold')
        ax2.set_ylim([0, 110])
        ax2.axhline(y=100, color='orange', linestyle='--', alpha=0.5, label='100/110')
        ax2.axhline(y=110, color='gold', linestyle='--', alpha=0.5, label='110/110')
        ax2.legend()
        
        # Add value label
        for bar in bar2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        # 3. Grade distribution
        ax3 = axes[1, 0]
        grade_values = [min(g, 30) for g in self.grades.values()]
        ax3.hist(grade_values, bins=range(18, 32), color='#3498db', 
                edgecolor='black', alpha=0.7)
        ax3.set_xlabel('Voto', fontsize=12)
        ax3.set_ylabel('Frequenza', fontsize=12)
        ax3.set_title('Distribuzione Voti', fontsize=13, fontweight='bold')
        ax3.axvline(x=weighted_avg, color='red', linestyle='--', 
                   linewidth=2, label=f'Media Ponderata ({weighted_avg:.2f})')
        ax3.legend()
        
        # 4. Grade by course (top 10 or all if less)
        ax4 = axes[1, 1]
        sorted_grades = sorted(self.grades.items(), key=lambda x: x[1], reverse=True)
        top_courses = sorted_grades[:10]
        
        course_names = [c[0][:20] + '...' if len(c[0]) > 20 else c[0] 
                       for c in top_courses]
        course_grades = [min(c[1], 30) for c in top_courses]
        
        colors_bars = ['#27ae60' if g >= 27 else '#f39c12' if g >= 24 else '#e74c3c' 
                      for g in course_grades]
        
        ax4.barh(course_names, course_grades, color=colors_bars, 
                edgecolor='black', linewidth=1)
        ax4.set_xlabel('Voto', fontsize=12)
        ax4.set_title('Top 10 Voti per Corso', fontsize=13, fontweight='bold')
        ax4.set_xlim([18, 30])
        
        plt.tight_layout()
        
        # Save plot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'grade_analysis_{timestamp}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        console.print(f"\n[green]✓ Grafici salvati in: {filename}[/green]")
        
        plt.show()
    
    def export_results(self, weighted_avg, arithmetic_avg, graduation_grade, stats):
        """Export results to JSON and CSV files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Prepare data
        results = {
            'timestamp': timestamp,
            'degree_course': self.degree_course,
            'degree_type': self.degree_type,
            'weighted_average': round(weighted_avg, 2),
            'arithmetic_average': round(arithmetic_avg, 2),
            'graduation_grade': round(graduation_grade, 2),
            'statistics': stats,
            'grades': {k: v for k, v in self.grades.items()}
        }
        
        # Export to JSON
        json_filename = f'results_{timestamp}.json'
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        
        # Export to CSV
        csv_filename = f'grades_{timestamp}.csv'
        df_grades = pd.DataFrame([
            {'Corso': course, 'Voto': grade, 'CFU': self.courses[course]}
            for course, grade in self.grades.items()
        ])
        df_grades.to_csv(csv_filename, index=False)
        
        console.print(f"[green]✓ Risultati esportati in: {json_filename} e {csv_filename}[/green]")
        
        # Save to log
        self._save_to_log(results)
    
    def _save_to_log(self, results):
        """Save simulation to log file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r', encoding='utf-8') as f:
                log = json.load(f)
        else:
            log = []
        
        log.append(results)
        
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(log, f, indent=4, ensure_ascii=False)
    
    def view_history(self):
        """View previous simulations."""
        if not os.path.exists(self.log_file):
            console.print("[yellow]Nessuno storico disponibile.[/yellow]")
            return
        
        with open(self.log_file, 'r', encoding='utf-8') as f:
            log = json.load(f)
        
        if not log:
            console.print("[yellow]Nessuno storico disponibile.[/yellow]")
            return
        
        console.print("\n[bold]Storico Simulazioni:[/bold]\n")
        
        for idx, sim in enumerate(log, 1):
            table = Table(title=f"Simulazione {idx} - {sim.get('timestamp', 'N/A')}", 
                         box=box.ROUNDED)
            table.add_column("Campo", style="cyan")
            table.add_column("Valore", style="yellow")
            
            table.add_row("Corso di Laurea", sim.get('degree_course', 'N/A'))
            table.add_row("Tipo", sim.get('degree_type', 'N/A'))
            table.add_row("Media Ponderata", f"{sim.get('weighted_average', 0):.2f}")
            table.add_row("Media Aritmetica", f"{sim.get('arithmetic_average', 0):.2f}")
            table.add_row("Voto di Laurea", f"{sim.get('graduation_grade', 0):.2f}")
            
            console.print(table)
            console.print()


def main():
    """Main function to run the grade calculator."""
    calc = GradeCalculator()
    calc.display_welcome()
    
    # Select degree type and course
    calc.select_degree_type()
    if not calc.select_degree_course():
        return
    
    # Display courses
    calc.display_courses()
    
    # Input method selection
    console.print("\n[bold]Metodo di inserimento voti:[/bold]")
    console.print("1. [cyan]Inserimento manuale[/cyan]")
    console.print("2. [magenta]Importa da file[/magenta] (TXT, CSV, Excel)")
    console.print("3. [yellow]Crea file di esempio[/yellow]")
    console.print("4. [green]Visualizza storico[/green]")
    
    choice = Prompt.ask("\nScelta", choices=["1", "2", "3", "4"], default="1")
    
    if choice == "3":
        calc.create_sample_files()
        return
    elif choice == "4":
        calc.view_history()
        return
    elif choice == "2":
        file_path = Prompt.ask("Inserisci il percorso del file")
        if not calc.import_grades_from_file(file_path):
            console.print("[yellow]Passaggio a inserimento manuale...[/yellow]")
            calc.input_grades_manual()
    else:
        calc.input_grades_manual()
    
    # Calculate results
    if not calc.grades:
        console.print("[red]Nessun voto inserito. Uscita.[/red]")
        return
    
    console.print("\n[bold cyan]Calcolo in corso...[/bold cyan]")
    
    weighted_avg = calc.calculate_weighted_average()
    arithmetic_avg = calc.calculate_arithmetic_average()
    graduation_grade = calc.calculate_graduation_grade(weighted_avg)
    stats = calc.calculate_statistics()
    
    # Display results
    calc.display_results(weighted_avg, arithmetic_avg, graduation_grade, stats)
    
    # Ask for visualizations
    if Confirm.ask("\nVuoi visualizzare i grafici?", default=True):
        calc.plot_visualizations(weighted_avg, arithmetic_avg, graduation_grade)
    
    # Ask for export
    if Confirm.ask("\nVuoi esportare i risultati?", default=True):
        calc.export_results(weighted_avg, arithmetic_avg, graduation_grade, stats)
    
    console.print("\n[bold green]✓ Operazione completata con successo![/bold green]")


if __name__ == "__main__":
    main()
