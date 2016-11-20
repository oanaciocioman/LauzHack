import os
from time import sleep
import midi
import pygame
import pygame.midi
from threading import Thread

import subprocess

pattern = midi.read_midifile('feliznavidad.mid')

class Voice(Thread):
    def __init__(self, syllables, pitches, rates):
        super(Voice, self).__init__()
        self.syllables = syllables
        self.pitches = pitches
        self.rates = rates

    def run(self):
        sleep(5)
        for i in range(len(self.syllables)):
            file = open(str(i) + "file.txt", "w+")
            file.write(syllables[i])
            if i + 1 < len(self.syllables) and syllables[i + 1] == ' ':
                file.write(syllables[i])
                i += 1
            file.close()
            os.system("espeak.exe" + " -f " + str(i) + "file.txt" + " -p " + str(pitches[i]) + " -s " + str(260) + " -w " + str(i) + ".wav")
            os.remove(str(i) + "file.txt")
            sleep(0.00000001 * len(syllables[i]))
        """
        sound1 = AudioSegment.from_file("/0.wav")
        sound2 = AudioSegment.from_file("/1.wav")

        combined = sound1.overlay(sound2)

        combined.export("/path/to/combined.wav", format='wav')
     """

class Music(Thread):

    def __init__(self):
        super(Music, self).__init__()

    def run(self):
        pygame.mixer.init()
        try:
            pygame.mixer.music.load('feliznavidad.mid')
            print "Music file %s loaded!" % pattern
        except pygame.error:
            print "File %s not found! (%s)" % (pattern, pygame.get_error())
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sleep(1)
pitches = []
rates = []

for track in pattern:
    for event in track:
        if isinstance(event, midi.NoteEvent):
            pitches.append(event.get_pitch())
            rates.append(event.get_velocity())

syllables = ['jing', 'gull']

"""
syllables = ['jing', 'gull', ' ', 'belz', ' ', 'jing', 'gull', ' ', 'belz', ' ', 'jing', 'gull', ' ', 'awl', ' ',
             'thuh', ' ', 'wey', ' ', 'oh', ' ', 'wha', ' ', 'fuhn', ' ', 'it', ' ', 'iz', ' ', 't', ' ', 'rahyd',
             ' ', 'in', ' ', 'A', ' ', 'won', ' ', 'hawrs', ' ', 'oh', 'pun', ' ', 'sley', ' ', 'oh', ' ', 'thuh',
             ' ', 'weh', 'ther', ' ', 'outsid', ' ', 'iz', ' ', 'frahyt', 'full', ' ', 'bu', ' ', 'thuh', ' ', 'fah',
             'yer', ' ', 'iz', ' ', 'soh', ' ', 'dih', 'lite', 'full', ' ', 'an', ' ', 'sins', ' ', 'we', 'v', ' ',
             'noh', ' ', 'pleys', ' ', 't', ' ', 'goh', ' ', 'let', ' ', 'it', ' ', 'snoh', ' ']

"""

t1 = Voice(syllables, pitches, rates)
t2 = Music()
t1.start()
t2.start()
t1.join()
t2.join()

"""
daniweb.play_music('jinglebells.mid')
pygame.midi.init()
port = pygame.midi.get_default_output_id()
player = pygame.midi.Output(port, 0)
for i in range(1000):
    # subprocess.call(["spd-say", syllables[i], "-p " + str(pitches[i]) + " -r " + str(rates[i])])
    # player.set_instrument(0)
    player.note_on(pitches[i], rates[i], channel)
    time.sleep(0.15)
    player.note_off(pitches[i], rates[i], channel)
del player
pygame.midi.quit()

thread_1 = Lyrics(syllables, pitches, rates)
thread_2 = Music(syllables, pitches, rates)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

spaces_syllabels = []
for i in range(len(syllables)):
	spaces_syllabels.append(syllables[i])
	spaces_syllabels.append(' ')

syllables = spaces_syllabels

for i in range(len(syllables)):
	subprocess.call(["spd-say", syllables[i], "-p " + str(pitches[i]) + " -r " + str(rates[i])])
	time.sleep(0.1 * len(syllables[i]))
"""
