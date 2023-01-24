"""This program is free software: you can redistribute it and/or modify 
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>."""

# This program is written by Mikhail 'Mautoz' Kuznetsov
# My Youtube channel: https://www.youtube.com/c/mautoztech
# My second Youtube channel only about programming: https://www.youtube.com/@aidev

# CHANGE THIS VARIABLE TO THE NAME OF YOUR MODEL:
model = "small-22-ru"
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont, QFontMetrics, QCursor
from PyQt5.QtCore import Qt, QPoint, QObject
import queue
import sounddevice as sd
import vosk
from threading import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.fontSize=40
        self.text="Loading..."
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.title = QLabel(self)
        self.title.setText(self.text)
        self.title.setFont(QFont("Helvetica", self.fontSize, QFont.Bold))
        self.title.setGeometry(195, 0, 940, 716)
        self.title.setScaledContents(True)
        self.title.setWordWrap(True)
        self.title.setAlignment(Qt.AlignTop)
        self.keyPressEvent = self.exitEvent
        #kek.setPos(100, 100)
        self.show()#FullScreen()
        kek = QCursor()
        print(kek.pos())
        self.fm = QFontMetrics(QFont("Helvetica", self.fontSize, QFont.Bold))
        print(self.fm.horizontalAdvance(self.text))
        def recognizing():
            q = queue.Queue()
            def callback(indata, frames, time, status):
                if status:
                    print(status, file=sys.stderr)
                q.put(bytes(indata))
            
            device=None
            device_info = sd.query_devices(device, 'input')
            samplerate = int(device_info['default_samplerate'])
            vmodel = vosk.Model(model)
            with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device, dtype='int16',
                                        channels=1, callback=callback):
                rec = vosk.KaldiRecognizer(vmodel, samplerate)
                self.text=""
                self.title.setText(self.text)
                while True:
                    data = q.get()
                    if rec.AcceptWaveform(data):
                        res=rec.Result()
                        if (res[14:-3]!= "" and res[14:-3]!= " "):
                            self.text=self.text+res[14:-3]+" "
                            if (len(self.text)<=168):#144
                                self.title.setText(self.text)
                            else:
                                while (len(self.text)>168):#144
                                    lastSpace=0
                                    for i in range(len(self.text)):
                                        if (self.text[i]==" "):
                                            if (self.fm.horizontalAdvance(self.text[:i])>940):
                                                self.text=self.text[lastSpace+1:]
                                                self.title.setText(self.text)
                                                break
                                            lastSpace=i
                                            
                    else:
                        partRes=rec.PartialResult()[17:-3]
                        if (partRes!= "" and partRes!= " "):
                            #self.text=self.text+res[14:-3]+" "
                            partRes=self.text+partRes+" "
                            if (len(partRes)<=240):#144
                                self.title.setText(partRes)
                            else:
                                while (len(partRes)>240):#144
                                    lastSpace=0
                                    for i in range(len(partRes)):
                                        if (partRes[i]==" "):
                                            if (self.fm.horizontalAdvance(partRes[:i])>940):
                                                partRes=partRes[lastSpace+1:]
                                                self.title.setText(partRes)
                                                break
                                            lastSpace=i
                                                
                        #print(rec.PartialResult()[16:-3])
        self.t1 = Thread(target = recognizing, daemon=True)
        self.t1.start()
    def background_init(self):
        frame = QLabel(self)
        frame.setGeometry(0,0,self.width,self.height)
        frame.setStyleSheet('background-color: white; border-style: solid; border-width: 1px; border-color: black;')
        
    def exitEvent(self,event):
        if (event.key()==16777216 or event.key()==32):
            print("exit")
            sys.exit(app.exec_())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
