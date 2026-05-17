import sys
from collections import Counter

# slowa kluczowe, szukane w logach
error_patterns = ["ERROR", "timeout", "failed", "refused", "database"]

def analyze_log(file_path):
    errors = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                for pattern in error_patterns:
                    if pattern.lower() in line.lower():
                        errors.append(pattern)
    except FileNotFoundError:
        print(f"Blad: Plik '{file_path}' nie istnieje!")
        return

    summary = Counter(errors)

    with open("report.txt", "w") as f:
        f.write("=====================================\n")
        f.write("       LOG ANALYSIS REPORT\n")
        f.write("=====================================\n\n")
        for k, v in summary.items():
            f.write(f"Typ bledu: '{k}' -> znaleziono razy: {v}\n")

    print(f"Raport z pliku '{file_path}' zostal pomyslnie wygnerowany w report.txt")

    penguin = """
     .-"-.
    / 0 0 \\
    \\_ v _/         LINUX LOG ANALYZER
    //   \\\\         Analiza zakonczona!
   ||     ||        Raport zapisano w report.txt
   \\\\_ _ _//
    `-` `-'
"""
    print(penguin)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Blad: Nie podales plikou z logami!")
        print("Uzycie: python3 analyzer.py <sciezka_do_pliku_z_logami>")
        sys.exit(1)

    # pobieramy drugi argument z terminala podany do pythona czyli plik z logami
    wybrany_plik = sys.argv[1]

    # uruchamiamy skrypt
    analyze_log(wybrany_plik)
