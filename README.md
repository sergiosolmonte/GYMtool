# GYMtool
Progetto realizzato in flask
Per utilizzare GYMtool è necessario aver installato pycharm sul proprio pc.
1. Scaricare il codice come .zip 
2. Avviare pycharm e aprire il **progetto** GYMtool contenuto nell'omonima cartella
3. Aprire "edit configuration" e selezionare "Custom" -> poi scrivere app.py :
![alt text](https://github.com/sergiosolmonte/GYMtool/blob/main/custom.png?raw=true)
4.Nel terminale di Pycharm ora bisogna creare un virtual env:
Prima installando (se si ha la versione di python3)
```
python3 -m venv venv
```
oppure utilizzare il default:
```
python -m venv venv
```
Poi creare il venv
```
virtualenv venv
```
e infine 
(con Ubuntu/mac)
```
source venv/bin/activate
```
(con windows)
```
pip install -r requirements.txt
```
5. Nel terminale di pycharm effettuare il caricamento dei requirements:
```
venv\Scripts\activate
```
6. Avviare il progetto con il comando:
```
flask run
```

n.b. per una corretta visualizzazione, utilizzarlo online dato l'utilizzo di font bootstrap e immagini dinamicamente caricate.
