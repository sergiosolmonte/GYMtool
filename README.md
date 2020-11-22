# GYMtool
Progetto realizzato in flask.
Per utilizzare GYMtool è necessario aver installato pycharm sul proprio pc.
1. Scaricare il codice come .zip 
2. Avviare pycharm e aprire il **progetto** GYMtool contenuto nell'omonima cartella
3. Aprire "edit configuration", aggiungere un nuovo **flask server**, selezionare "Custom" -> poi scrivere app.py :
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
venv\Scripts\activate
```
5. Nel terminale di pycharm effettuare il caricamento dei requirements:
```
pip install -r requirements.txt
```
6. Avviare il progetto con il comando:
```
flask run
```

**Per il correto funzionamento del CDN occorre essere conessi alla rete.


-----CONFIGURAZIONE INTERPRETE PYTHON-----
È possibile avviare il progetto anche direttamente con il run di pycharm, basta configurare il corretto interprete.
1. Recarsi in *File -> Setting* 
2. Project: GYMtool e selezionare Project Interpreter
3. Click sulla rotella e poi su add come in figura: 
<img src="https://github.com/sergiosolmonte/GYMtool/blob/main/add.png?raw=true" width="500" height="400"/>
4. Selezionare Existing Environment e poi su OK:
<img src="https://github.com/sergiosolmonte/GYMtool/blob/main/existing.png?raw=true" width="500" height="400"/>
5. Click su apply e poi OK
<img src="https://github.com/sergiosolmonte/GYMtool/blob/main/apply.png?raw=true" width="500" height="400"/>
6. Andare di nuovo in edit configuration e selezionare il nuovo python interpreter appena aggiunto:
<img src="https://github.com/sergiosolmonte/GYMtool/blob/main/new_interpreter.png?raw=true" width="500" height="400"/>
7. Apply e poi Ok

Ora il progetto è configurato al 100% ed è possibile avviarlo tramite il RUN del pycharm.
