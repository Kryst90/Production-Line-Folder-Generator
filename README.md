# Production Line Folder Generator

A Python script that automatically creates a standardized folder structure for a new production line or project.  
This ensures consistency in documentation and file organization across multiple lines.

## How It Works
1. The script asks the user for a base directory where the folders should be created.
2. It generates a predefined set of folders such as:
   - `01_Deklaracja_Zgodności`
   - `02_Instrukcja_Obsługi_i_Konserwacji`
   - `03_Instrukcje_Procesowe`
   - ...
   - `21_Listy_wykonania_EP_BS_AM`
   - `99_Inne`
3. If a folder already exists, it will not be overwritten (safe operation).
4. Prints a confirmation message for each created folder.

## Example
Run the script in a terminal:
```bash
python "PLFG.py"
Then enter a path such as:

makefile
Skopiuj kod
C:\Projects\New_Production_Line
The following structure will be created automatically:

makefile
Skopiuj kod
C:\Projects\New_Production_Line\
 ├─ 01_Deklaracja_Zgodności
 ├─ 02_Instrukcja_Obsługi_i_Konserwacji
 ├─ 03_Instrukcje_Procesowe
 ├─ ...
 └─ 99_Inne
```
## Requirements
Python 3.8+

No external dependencies (uses built-in os module)

## Benefits
Saves time when setting up documentation for a new production line

Ensures consistency in naming and folder structure

Prevents human error by automating the process

## License
MIT License – free to use and modify
