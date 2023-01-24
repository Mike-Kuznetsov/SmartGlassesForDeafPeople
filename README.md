# SmartGlassesForDeafPeople
This Python program converts sound into text on the screen of smart glasses in real-time.  
My devices i used it with:  
  Portable PC: Orange Pi PC2 / Orange Pi One  
  Smart Glasses: Vufine Plus / VUF-110  
  
Before using you have to install this list of packages:  
apt install libffi-dev  
apt install libportaudio2  
apt install python3-dev  
apt install python3-pip  
pip install vosk  
pip install sounddevice  
pip install pyqt5  
Also you have to download language model from https://alphacephei.com/vosk/models, unzip it into folder with this program and change model name variable in program to the name of your language model. You can put it into autostart list to make it start automatically with operating system, also you can turn off password auth.  
If i forgot something write me.  
  
Orange Pi One has no microphone so you have to buy USB microphone.    

Эта Пайтон-программа распознает слова по звуку с микрофона в реальном времени и выводит их на экран очков.  
Устройства с которыми я использовал программу:  
  Portable PC: Orange Pi PC2 / Orange Pi One  
  Smart Glasses: Vufine Plus / VUF-110  
  
Перед использованием необходимо установить следующие пакеты:    
apt install libffi-dev  
apt install libportaudio2  
apt install python3-dev  
apt install python3-pip  
pip install vosk  
pip install sounddevice  
pip install pyqt5  
Также вам необходимо скачать языковую модель с сайта https://alphacephei.com/vosk/models, распаковать её в папку с этой программой и изменить название модели в программе на название вашей модели. Вы можете добавить эту программу в автозагрузку, чтобы она запускалась автоматически вместе с операционной системой, и вы можете отключить необходимость ввода пароля.  
Если я что-то забыл, можете написать мне.  
  
У Orange Pi One нет микрофона, вам надо докупить USB-микрофон.  

