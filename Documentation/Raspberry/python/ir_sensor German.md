# Code für IR (Infrarot) gesteuerte Kamera

## Erklärung

Die Datei `src/python/ir_sensor.py` steuert die Picamera und Infrarot Sensoren. Dies Erfolgt durch IR Signale. 
Ein IR Empfänger ist am Raspbery Pi befestigt. Wen der IR Empfänger ein Signal empfängt 
wird die Camera ein 5 Sek. Video machen. Das Video wird dann auf einem Speicherplatz
gespeichert. In unserem Fall einem USB Stick. Man kann den IR Empfänger mit allem das IR sendet ansteuern. 
Man muss nur auf die Frequenz achten. 

## Tipps
Gehe zum Ordner mit dem Python Code 
```bash 
$ cd src/python/ir_sensor.py
```
Dort nun bitte den Code mit dem Program `python3` ausführen.
Überprüfen sie ob sie dieses installiert haben mit:
```bash
$ python3 --version
Python 3.6.7
```
Wenn sie etwas derartiges sehen (oder höher) können sie diesen Code ausführen mit:
```bash
$ python3 ir_sensor.py
```
Sie können dieses Programm jederzeit mit der Tastenkombination Strg + c stoppen und wieder in den Terminal
kommen.
