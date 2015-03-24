from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

from kivy.graphics import Color, Rectangle

from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty

from kivy.clock import Clock

import datetime
import time
import os
import sys

from kivy.animation import Animation

from kivy.core.audio import SoundLoader
from os.path import dirname, join, basename

from kivy.uix.slider import Slider

global noteindex, flag_dom, flag_majmin, flag_fast_mode
global notedebug
global tempstring
global root_num
global count, limit
global notecache
global schedl
global masterlist
global sound
global bpm

# assume its 4/4 time.

bpm = 120
sound = None
masterlist = []
schedl = False
count = 1
limit = 4
root_num = 0
tempstring = ''
noteindex = []
notecache = ['NoneGiven'] * 64
flag_dom = False
flag_majmin = False
flag_fast_mode = False
notedebug = ['C','C#','D','D#','E','F','F#','G', \
'G#','A','A#','B','C','C#','D','D#','E','F','F#', \
        'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F'] #### F# G G# A A# B C C# D D# E F F# G G# A A# B

class BPMSlider(Slider):

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            global bpm
            bpm = int(self.value)
            return True

class LabelThing(Label):
    def change_label(self, *args):
        global tempstring, notecache
        self.text = str(tempstring)
        print(tempstring)
        notecache[(count-1)] = tempstring
        
class GridWindow(GridLayout):
    pass
class SquareButton(Button):

    def release_1(self):
        rootPath = os.path.dirname(os.path.realpath(sys.argv[0]))
        soundPath = rootPath + '/audio/'
        sound = SoundLoader.load(soundPath + 'C5.wav')
        if sound:
            print("sound found at %s" % sound.source)
            sound.play()
            def soundunload(*l):
                sound.unload()
            Clock.schedule_once(soundunload, 1)
        else:
            print ("else statement")


class ChordDisplayer(BoxLayout):
    pass
class Scrollable(Scatter):
    pass

class Pointer(FloatLayout):
    pass

class MainWindowWidget(FloatLayout):
    def printnotecache(obj):
        global notecache
        print(notecache)

    rootPath = os.path.dirname(os.path.realpath(sys.argv[0]))
    soundPath = rootPath + '/audio/'
    window_1 = ObjectProperty(None)
    window_2 = ObjectProperty(None)
    window_3 = ObjectProperty(None)
    window_4 = ObjectProperty(None)
    cd_1 = ObjectProperty(None)
    cd_2 = ObjectProperty(None)
    cd_3 = ObjectProperty(None)
    cd_4 = ObjectProperty(None)
    BPM_slider = ObjectProperty(None)

    button_dom = ObjectProperty(None)
    button_majmin = ObjectProperty(None)
    button_fastmode = ObjectProperty(None)
    button_tog = ObjectProperty(None)

    button_C = ObjectProperty(None)
    button_Cs = ObjectProperty(None)
    button_D = ObjectProperty(None)
    button_Ds = ObjectProperty(None)
    button_E = ObjectProperty(None)
    button_F = ObjectProperty(None)
    button_Fs = ObjectProperty(None)
    button_G = ObjectProperty(None)
    button_Gs = ObjectProperty(None)
    button_A = ObjectProperty(None)
    button_As = ObjectProperty(None)
    button_B = ObjectProperty(None)

    sound_C = SoundLoader.load(soundPath + 'C4.wav')
    sound_Cs = SoundLoader.load(soundPath + 'C#4.wav')
    sound_D = SoundLoader.load(soundPath + 'D4.wav')
    sound_Ds = SoundLoader.load(soundPath + 'D#4.wav')
    sound_E = SoundLoader.load(soundPath + 'E4.wav')
    sound_F = SoundLoader.load(soundPath + 'F4.wav')
    sound_Fs = SoundLoader.load(soundPath + 'F#4.wav')
    sound_G = SoundLoader.load(soundPath + 'G4.wav')
    sound_Gs = SoundLoader.load(soundPath + 'G#4.wav')
    sound_A = SoundLoader.load(soundPath + 'A4.wav')
    sound_As = SoundLoader.load(soundPath + 'A#4.wav')
    sound_B = SoundLoader.load(soundPath + 'B5.wav')

    def down_C(self):
        self.button_C.background_color = 0.5, 0.5, 0.5, 1

    def up_C(self, inputroot):
        self.button_C.background_color = 255, 255, 255, 1
        self.setroot(inputroot)

    def down_Cs(self):
        self.button_Cs.background_color = 0.5, 0.5, 0.5, 1

    def up_Cs(self, inputroot):
        self.button_Cs.background_color = 0, 0, 0, 1
        self.setroot(inputroot)

    def down_D(self):
        self.button_D.background_color = 0.5, 0.5, 0.5, 1

    def up_D(self, inputroot):
        self.button_D.background_color = 255, 255, 255, 1
        self.setroot(inputroot)

    def down_Ds(self):
        self.button_Ds.background_color = 0.5, 0.5, 0.5, 1

    def up_Ds(self, inputroot):
        self.button_Ds.background_color = 0, 0, 0, 1
        self.setroot(inputroot)

    def down_E(self):
        self.button_E.background_color = 0.5, 0.5, 0.5, 1

    def up_E(self, inputroot):
        self.button_E.background_color = 255, 255, 255, 1
        self.setroot(inputroot)

    def down_F(self):
        self.button_F.background_color = 0.5, 0.5, 0.5, 1

    def up_F(self, inputroot):
        self.button_F.background_color = 255, 255, 255, 1
        self.setroot(inputroot)

    def down_Fs(self):
        self.button_Fs.background_color = 0.5, 0.5, 0.5, 1

    def up_Fs(self, inputroot):
        self.button_Fs.background_color = 0, 0, 0, 1
        self.setroot(inputroot)

    def down_G(self):
        self.button_G.background_color = 0.5, 0.5, 0.5, 1

    def up_G(self, inputroot):
        self.button_G.background_color = 255, 255, 255, 1
        self.setroot(inputroot)

    def down_Gs(self):
        self.button_Gs.background_color = 0.5, 0.5, 0.5, 1

    def up_Gs(self, inputroot):
        self.button_Gs.background_color =  0, 0, 0, 1
        self.setroot(inputroot)

    def down_A(self):
        self.button_A.background_color = 0.5, 0.5, 0.5, 1

    def up_A(self, inputroot):
        self.button_A.background_color = 255, 255, 255, 1
        self.setroot(inputroot)

    def down_As(self):
        self.button_As.background_color = 0.5, 0.5, 0.5, 1

    def up_As(self, inputroot):
        self.button_As.background_color = 0, 0, 0, 1
        self.setroot(inputroot)

    def down_B(self):
        self.button_B.background_color = 0.5, 0.5, 0.5, 1

    def up_B(self, inputroot):
        self.button_B.background_color = 255, 255, 255, 1
        self.setroot(inputroot)

    def playback(self, dt):
        global count, notecache, masterlist

        if notecache:
            # print notecache[count-1]
            masterlist = notecache[count-1].split()
            print(masterlist)


            #sound_C = SoundLoader.load('C4.wav')
            #sound_Cs = SoundLoader.load('C#4.wav')
            #sound_D = SoundLoader.load('D4.wav')
            #sound_Ds = SoundLoader.load('D#4.wav')
            #sound_E = SoundLoader.load('E4.wav')
            #sound_F = SoundLoader.load('F4.wav')
            #sound_Fs = SoundLoader.load('F#4.wav')
            #sound_G = SoundLoader.load('G4.wav')
            #sound_Gs = SoundLoader.load('G#4.wav')
            #sound_A = SoundLoader.load('A4.wav')
            #sound_As = SoundLoader.load('A#4.wav')
            #sound_B = SoundLoader.load('B5.wav')

            #sound_C = SoundLoader.load('C5.wav')
            #sound_Cs = SoundLoader.load('C#5.wav')
            #sound_D = SoundLoader.load('D5.wav')
            #sound_Ds = SoundLoader.load('D#5.wav')
            #sound_E = SoundLoader.load('E5.wav')
            #sound_F = SoundLoader.load('F5.wav')
            #sound_Fs = SoundLoader.load('F#5.wav')
            #sound_G = SoundLoader.load('G5.wav')
            #sound_Gs = SoundLoader.load('G#5.wav')
            #sound_A = SoundLoader.load('A5.wav')
            #sound_As = SoundLoader.load('A#5.wav')
            #sound_B = SoundLoader.load('B5.wav')

            #sound_C = SoundLoader.load('C6.wav')
            #sound_Cs = SoundLoader.load('C#6.wav')
            #sound_D = SoundLoader.load('D6.wav')
            #sound_Ds = SoundLoader.load('D#6.wav')
            #sound_E = SoundLoader.load('E6.wav')
            #sound_F = SoundLoader.load('F6.wav')
            #sound_Fs = SoundLoader.load('F#6.wav')
            #sound_G = SoundLoader.load('G6.wav')
            #sound_Gs = SoundLoader.load('G#6.wav')
            #sound_A = SoundLoader.load('A6.wav')
            #sound_As = SoundLoader.load('A#6.wav')
            #sound_B = SoundLoader.load('B6.wav')

            for note in masterlist:
                if note == 'C':
                    #Clock.unschedule(self.unload_C)
                    self.sound_C = SoundLoader.load(self.soundPath +'C4.wav')
                    if self.sound_C:
                        self.sound_C.play()
                        Clock.schedule_once(self.unload_C, 5)
                    else:
                        print('sound_C not found')

                if note == 'C#':
                    #Clock.unschedule(self.unload_Cs)
                    self.sound_Cs = SoundLoader.load(self.soundPath +'C#4.wav')
                    if self.sound_Cs:
                        self.sound_Cs.play()
                        Clock.schedule_once(self.unload_Cs, 5)
                    else:
                        print('sound_Cs not found')

                if note == 'D':
                    #Clock.unschedule(self.unload_D)
                    self.sound_D = SoundLoader.load(self.soundPath +'D4.wav')
                    if self.sound_D:
                        self.sound_D.play()
                        Clock.schedule_once(self.unload_D, 5)
                    else:
                        print('sound_D not found')

                if note == 'D#':
                    #Clock.unschedule(self.unload_Ds)
                    self.sound_Ds = SoundLoader.load(self.soundPath +'D#4.wav')
                    if self.sound_Ds:
                        self.sound_Ds.play()
                        Clock.schedule_once(self.unload_Ds, 5)
                    else:
                        print('sound_Ds not found')

                if note == 'E':
                    #Clock.unschedule(self.unload_E)
                    self.sound_E = SoundLoader.load(self.soundPath +'E4.wav')
                    if self.sound_E:
                        self.sound_E.play()
                        Clock.schedule_once(self.unload_E, 5)
                    else:
                        print('sound_E not found')

                if note == 'F':
                    #Clock.unschedule(self.unload_F)
                    self.sound_F = SoundLoader.load(self.soundPath +'F4.wav')
                    if self.sound_F:
                        self.sound_F.play()
                        Clock.schedule_once(self.unload_F, 5)
                    else:
                        print('sound_F not found')

                if note == 'F#':
                    #Clock.unschedule(self.unload_Fs)
                    self.sound_Fs = SoundLoader.load(self.soundPath +'F#4.wav')
                    if self.sound_Fs:
                        self.sound_Fs.play()
                        Clock.schedule_once(self.unload_Fs, 5)
                    else:
                        print('sound_Fs not found')

                if note == 'G':
                    #Clock.unschedule(self.unload_G)
                    self.sound_G = SoundLoader.load(self.soundPath +'G4.wav')
                    if self.sound_G:
                        self.sound_G.play()
                        Clock.schedule_once(self.unload_G, 5)
                    else:
                        print('sound_G not found')

                if note == 'G#':
                    #Clock.unschedule(self.unload_Gs)
                    self.sound_Gs = SoundLoader.load(self.soundPath +'G#4.wav')
                    if self.sound_Gs:
                        self.sound_Gs.play()
                        Clock.schedule_once(self.unload_Gs, 5)
                    else:
                        print('sound_Gs not found')

                if note == 'A':
                    #Clock.unschedule(self.unload_A)
                    self.sound_A = SoundLoader.load(self.soundPath +'A4.wav')
                    if self.sound_A:
                        self.sound_A.play()
                        Clock.schedule_once(self.unload_A, 5)
                    else:
                        print('sound_A not found')

                if note == 'As':
                    #Clock.unschedule(self.unload_As)
                    self.sound_As = SoundLoader.load(self.soundPath +'A#4.wav')
                    if self.sound_As:
                        self.sound_As.play()
                        Clock.schedule_once(self.unload_As, 5)
                    else:
                        print('sound_As not found')

                if note == 'B':
                    #Clock.unschedule(self.unload_B)
                    self.sound_B = SoundLoader.load(self.soundPath +'B4.wav')
                    if self.sound_B:
                        self.sound_B.play()
                        Clock.schedule_once(self.unload_B, 5)
                    else:
                        print('sound_B not found')

        self.moveanim(False)
        count = count + 1
        if count == limit + 1:
            count = 1
    def unload_C(self, *args):
        if self.sound_C:
            self.sound_C.unload()
            self.sound_C = None
    def unload_Cs(self, *args):
        if self.sound_Cs:
            self.sound_Cs.unload()
            self.sound_Cs = None
    def unload_D(self, *args):
        if self.sound_D:
            self.sound_D.unload()
            self.sound_D = None
    def unload_Ds(self, *args):
        if self.sound_Ds:
            self.sound_Ds.unload()
            self.sound_Ds = None
    def unload_E(self, *args):
        if self.sound_E:
            self.sound_E.unload()
            self.sound_E = None
    def unload_F(self, *args):
        if self.sound_F:
            self.sound_F.unload()
            self.sound_F = None
    def unload_Fs(self, *args):
        if self.sound_Fs:
            self.sound_Fs.unload()
            self.sound_Fs = None
    def unload_G(self, *args):
        if self.sound_G:
            self.sound_G.unload()
            self.sound_G = None
    def unload_Gs(self, *args):
        if self.sound_Gs:
            self.sound_Gs.unload()
            self.sound_Gs = None
    def unload_A(self, *args):
        if self.sound_A:
            self.sound_A.unload()
            self.sound_A = None
    def unload_As(self, *args):
        if self.sound_As:
            self.sound_As.unload()
            self.sound_A = None
    def unload_B(self, *args):
        if self.sound_B:
            self.sound_B.unload()
            self.sound_B = None

    def togdom(self):
        global flag_dom
        if flag_dom == False:
            flag_dom = True
            self.button_dom.background_color = 0, 255, 0, 0.5
        else:
            flag_dom = False
            self.button_dom.background_color = 255, 0, 0, 0.5

        print('flag_dom', flag_dom)

    def togmajmin(self):

        global flag_majmin
        if flag_majmin == False:
            flag_majmin = True
            self.button_majmin.background_color = 0, 255, 0, 0.5
        else:
            flag_majmin = False
            self.button_majmin.background_color = 255, 0, 0, 0.5

        print('flag_majmin', flag_majmin)

    def togfastmode(self):
        global flag_fast_mode
        if flag_fast_mode == False:
            flag_fast_mode = True
            self.button_fastmode.background_color = 0, 255, 0, 0.5
        else:
            flag_fast_mode = False
            self.button_fastmode.background_color = 255, 0, 0, 0.5

    def setroot(self, inputroot):
        global flag_dom
        global flag_majmin
        global flag_fast_mode
        global root_num
        global count
        root_num = inputroot
        del noteindex[:]
        noteindex.append(inputroot)
        if flag_fast_mode == False:

            if flag_majmin == True:
                noteindex.append(inputroot + 3)
            else:
                noteindex.append(inputroot + 4)

            noteindex.append(inputroot + 7)
            if flag_dom == True:
                noteindex.append(inputroot + 10)

        self.convertnotes()

        if count == 1:
            self.window_1.change_label()
        elif count == 2:
            self.window_2.change_label()
        elif count == 3:
            self.window_3.change_label()
        elif count == 4:
            self.window_4.change_label()
        self.moveanim(False)
        count = count + 1
        if count == limit + 1:
            count = 1

    def moveanim(self, repos):
        global count, limit
        if (repos == True):
            anim = Animation(x=0 ,y=self.pointer_id.y, d=0.1, t='in_out_circ')
            anim.start(self.pointer_id)
        elif (count < limit):
            anim = Animation(x=count*200 ,y=self.pointer_id.y, d=0.1, t='in_out_circ')
            anim.start(self.pointer_id)
        else:
            anim = Animation(x=0, y=self.pointer_id.y, d=0.1, t='in_out_circ')
            anim.start(self.pointer_id)

    def printnoteindex(self):
        global noteindex
        print(noteindex)

    def convertnotes(self):
        global noteindex, notedebug, tempstring
        tempstring = ''
        for i in noteindex:
            tempstring += notedebug[i]
            tempstring += ' '

    def spawnbox(self, *args):
        mww = MainWindowWidget()
        mww.add_widget(ChordDisplayer)

    def calcbeat(self):
        # take number of presses in last 3 seconds
        # *30
        
        print(datetime.datetime.now())
        print(datetime.time())
        print(time.clock())

    def sched(self):
        global schedl, bpm
        while notecache.count('NoneGiven') > 0:
            notecache.remove('NoneGiven')
        Clock.schedule_interval(self.playback, 1.0/(bpm/4.0/60.0))
        print('scheduled playback')
        schedl= True

    def unsched(self):
        global schedl, notecache
        schedl = False
        Clock.unschedule(self.playback)
        while len(notecache) < 64:
            notecache.append('NoneGiven')
            
    def schedtog(self):
        global schedl
        if schedl == False:
            self.sched()
            #self.button_tog.text = 'playing'
        else:
            self.unsched()
            #self.button_tog.background_color = 0.5, 0.5, 0.5, 1

    def on_touch_down(self, touch):
        if self.cd_1.collide_point(*touch.pos):
            global count
            count = 1
            print(count)
            self.moveanim(True)
            return True
        else:
            return super(MainWindowWidget, self).on_touch_down(touch)

class ChordApp(App):
    def build(self):
        return MainWindowWidget()

if __name__ == '__main__':
    ChordApp().run()


def on_pause():
    return True
