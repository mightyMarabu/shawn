# shawn

Das ZIP-File herunterladen und am Ort der Wahl entpacken. Via Console in den Ordner navigieren und python starten:
```
ipython
```

Die csv-Daten liegen im Ordner sheeps und sollten das Format 'Nummer'Sensor0.csv und 'Nummer'Sensor1.csv haben. Pro Schafnummer gibt es immer Sensor0 und Sensor 1 (2 Dateien).
(Bitte die erste Zeile mit dem Texteditor deiner Wahl löschen.)

## Shawns Toolbox
* Lib zur Analyse der Druckmessdaten

```python
from shawnsToolbox import *
```
### Funktionen
* prepare("sheepnr")
    * einlesen der zwei CSV-Dateien
    * Summe der Werte pro Sensor
    * Index Timestamp
    * Verknüpfung von Sensor 0 und 1 in einem DataFrame
    
```python
sheep32 = prepare("45032")
```
* clean(sheep)
    * Bereinigen der Daten
    * Ausgabe in kg
```python
clean(sheep32)
```
* show(sheep)
    * Visualisierung der Daten

```python
show(sheep32)
```