import os

# Lista nazw folderów
folders = [
    "01_Deklaracja_Zgodności",
    "02_Instrukcja_Obsługi_i_Konserwacji",
    "03_Instrukcje_Procesowe",
    "04_Schematy",
    "05_Instrukcja_Bezpiecznej_Obsługi",
    "06_Pomiary_Przeciwoporzeniowe",
    "07_Pomiary_EMF",
    "08_Standaryzacja_Pracy",
    "09_Ocena_Ergonomii",
    "10_BOM",
    "11_WRA",
    "12_Zdjęcia",
    "13_Layout",
    "14_Software",
    "15_Oświetlenie",
    "16_Dokumenty_odbiorowe",
    "17_Troubleshooting",
    "18_Instrukcje_UTR",
    "19_Walidacja",
    "20_Archiwum",
    "21_Listy_wykonania_EP_BS_AM",
    "99_Inne"
]

# Funkcja tworząca foldery
def create_folders(base_path):
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"Utworzono: {folder_path}")
        except Exception as e:
            print(f"Błąd przy tworzeniu {folder_path}: {e}")

# Zapytanie o ścieżkę od użytkownika
base_directory = input("Podaj pełną ścieżkę, gdzie mają zostać utworzone katalogi: ").strip()

# Tworzenie folderów
create_folders(base_directory)
