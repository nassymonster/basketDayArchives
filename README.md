# Projekt "basketDayArchives"

## Zadaním tohoto projektu je provést následující kroky::

1. Stažení dat ze stránky https://www.opec.org/basket/basketDayArchives.xml a uložení ve formátu CSV. 
V této fázi je žádoucí vyhnout se použití funkce pandas.read_xml.

2. Pro stažený DataFrame vytvoření nového sloupce s procentuálním denním pohybem a sloupce s procentuálním vývojem ceny. 
Upravený DataFrame bude uložen pod novým názvem ve formátu CSV.

3. Generování grafů ve formátech PNG, JPEG nebo HTML. Prvním vytvořeným grafem bude graf procentuálního vývoje ceny 
za celé období. Dále budou vytvořeny grafy s procentuálním vývojem ceny podle jednotlivých let.

4. Seskupený DataFrame podle roku a výpočet průměrné hodnoty procentuálního denního pohybu pro každý rok. 
Výsledný DataFrame bude uložen do formátu CSV.

5. Vytvoření sloupcového grafu z seskupeného DataFrame z předchozího kroku. Každý sloupec grafu bude znázorňovat 
průměrnou hodnotu denního pohybu za daný rok.

## Výstupy

### Soubory CSV

**[basketDayArchives.csv](results/basketDayArchives.csv)**: Obsahuje data ze stránky https://www.opec.org/basket/basketDayArchives.xml uložená ve formátu CSV.

**[basketDayArchivesComputed.csv](results/basketDayArchivesComputed.csv)**: Předchozí dataset doplněný o sloupec s procentuálním denním pohybem a sloupec s 
procentuálním vývojem ceny. Pro výpočet procentuálního vývoje ceny je použita první hodnota v období.

**[basketDayArchivesGeomMean.csv](results/basketDayArchivesGeomMean.csv)**: Obsahuje data znázorňující průměrné hodnoty procentuálního denního pohybu pro každý rok.

### Soubory PNG

**[plotPercentagePriceChange.png](results/charts/plotPercentagePriceChange.png)**: Graf zobrazující procentuální vývoj ceny za celé období.

**[plotPercentagePriceChange_xxxx.png](results/charts/)**: Grafy s procentuálním vývojem ceny podle jednotlivých let.

**[plotAveragePercentageDailyMovement.png](results/charts/plotAveragePercentageDailyMovement.png)**: Graf znázorňující průměrnou hodnotu denního pohybu za každý rok.
 
## Kroky pro spuštění Python kódu
1. Vytvoření virtuálního prostředí (venv):

   - Otevřete příkazový řádek (Command Prompt) nebo terminál ve složce projektu.
   - Zadejte následující příkaz pro vytvoření virtuálního prostředí:
     ```
     python -m venv venv
     ```
2. Aktivace virtuálního prostředí (venv):

   - Pro aktivaci virtuálního prostředí zadejte příkaz podle operačního systému:
     - Windows:
     ```
     venv\Scripts\activate
     ```
     - Mac/Linux:
     ```
     source venv/bin/activate
     ```
3. Instalace knihoven ze souboru requirements.txt:

   - Ujistěte se, že jste ve virtuálním prostředí (venv) (zkontrolujte, zda je před názvem příkazové řádky nebo promptu uvedeno (venv)).
   - Zadejte následující příkaz pro instalaci knihoven:
     ```
     pip install -r requirements.txt
     ```
4. Spuštění main.py:

   - Ujistěte se, že jste stále ve virtuálním prostředí (venv).
   - Zadejte následující příkaz pro spuštění main.py:
     ```
     python main.py
     ```
Po provedení těchto kroků by měl být Python kód ve souboru main.py úspěšně spuštěn ve virtuálním prostředí.

Poznámka: Pokud nemáte nainstalovaný Python, je třeba ho nejprve nainstalovat. Doporučuje se použít 
nejnovější stabilní verzi Pythonu, kterou lze stáhnout z oficiálních webových stránek Pythonu.