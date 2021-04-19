
[![Build Status](https://travis-ci.com/TheNaciaaStrike/pkp_website.svg?token=YJ8RyMCb7eQSyzypLmAi&branch=master)](https://travis-ci.com/TheNaciaaStrike/pkp_website)
<br />
# Projektas

feedback-and-psychological-analysis-project

# Paleidimas

importuoti projekto kodas folderį ir jį  susikonfigūruoti (python interpreter per project structure, importus galima atsisiusti per intellij);

### Reikalingi failai/ programos

* [Python](https://www.python.org/downloads/)

* [MySQL](https://www.mysql.com/downloads/)

* [pip] (https://pip.pypa.io/en/stable/reference/pip_download/)

### konfigūravimas

MySQL konfiguracija:
```
Reikia išsaugoti tokius prisijungimo duomenis:
user="root", password="",
sukurti duomenų bazę pavadinimu "testdb"
ir įvesti SQL kodą, esantį šiame folderyje tekstiniam faile pavadinimu "mysql script.txt"
```

pip konfiguracija:
```
pip3 install flask
pip3 install numpy
pip3 install passlib
pip3 install pyperclip
pip3 install wtforms
pip3 install pandas
pip3 install pymysql
pip3 install pyautogui
```

### Programos paleidimas

```
Atsidarius folder "Programos kodas" reikia paleisti "run.py" failą
Jei programa nepasileidžia pakeisti port numerį "run.py" faile

```

### Papildomai (Linux sistema)
```
XAMPP:
sudo wget https://downloadsapachefriends.global.ssl.fastly.net/7.3.0/xampp-linux-x64-7.3.0-0-installer.run?from_af=true
sudo chmod +x xampp-linux-x64-7.3.0-0-installer.run
sudo ./xampp-linux-x64-7.3.0-0-installer.run

Paleidimas:
cd /opt/lampp/
sudo ./manager-linux-x64.run



pip3 install xlrd (jei neveikia excel failo įkėlimas)
Gali reikėti tkinter jei leidžiama su linux system
Jei permission dennied model.py faile connectToDB funkcijoj pridėti port=xxxx, xxxx - mysql portas xampp programoje
Manjaro: sudo pacman -S tk
```
"# feedback-and-psychological-evaluation" 
