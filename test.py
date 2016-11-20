from time import sleep

import midi
import pygame
import pygame.midi
import _tkinter
from threading import Thread


pattern = midi.read_midifile('jinglebells.mid')

class Voice(Thread):
    def __init__(self, syllables, pitches, rates):
        super(Voice, self).__init__()
        self.syllables = syllables
        self.pitches = pitches
        self.rates = rates

    def run(self):
        for i in range(len(self.syllables)):
            print "X"
            #subprocess.call(["spd-say", syllables[i], "-p " + str(pitches[i]) + " -r " + str(rates[i])])


class Music(Thread):

    def __init__(self):
        super(Music, self).__init__()

    def run(self):
        pygame.mixer.init()
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load('jinglebells.mid')
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

syllables = ['we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'we', ' ', "don'", ' ', 'tawk', ' ', 'anymor', ' ',
             'we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'lahyk', ' ', 'we', ' ', 'use', ' ', 'to', ' ', 'do',
             ' ', 'we', ' ', "don'", ' ', 'lov', ' ', 'anymor', ' ', 'wha', ' ', 'was', ' ', 'all', ' ', 'of', ' ',
             'it', ' ', 'for', ' ', 'oh,', ' ', 'we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'lahyk', ' ', 'we',
             ' ', 'use', ' ', 'to', ' ', 'do', ' ']


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
