import subprocess
import time
import midi
import pygame
import pygame.midi
import daniweb

from threading import Thread
import time


class Lyrics(Thread):
    def __init__(self, syl_lyr, pitches, rates):
        super(Lyrics, self).__init__()
        self.syl_lyr = syl_lyr
        self.pitches = pitches
        self.rates = rates

    def run(self):
        syllables = self.syl_lyr
        pitches = self.pitches
        rates = self.rates
        for i in range(len(syllables)):
            # subprocess.call(["spd-say", syllables[i], "-p " + str(pitches[i]) + " -r " + str(rates[i])])
            print "Oana e frumoasa"
            time.sleep(0.1 * len(syllables[i]))


class Music(Thread):
    def __init__(self, syllables, pitches, rates):
        super(Music, self).__init__()
        self.syllables = syllables
        self.pitches = pitches
        self.rates = rates

    def run(self):
        for i in range(len(self.syllables)):
            print "X"
            pygame.midi.init()
            port = pygame.midi.get_default_output_id()
            player = pygame.midi.Output(port, 0)
            player.set_instrument(0)
            player.note_on(self.pitches[i], self.rates[i])
            time.sleep(0.1 * len(self.syllables[i]))
            player.note_off(self.pitches[i], self.rates[i])
            del player
            pygame.midi.quit()


pattern = midi.read_midifile('ABBA_-_Money_Money_Money.mid')

pitches = []
rates = []

for track in pattern:
    for event in track:
        if isinstance(event,
                      midi.NoteEvent):  # check that the current event is a NoteEvent, otherwise it won't have the method get_pitch() and we'll get an error
            pitches.append(event.get_pitch())
            rates.append(event.get_velocity())

syllables = ['we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'we', ' ', "don'", ' ', 'tawk', ' ', 'anymor', ' ',
             'we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'lahyk', ' ', 'we', ' ', 'use', ' ', 'to', ' ', 'do',
             ' ', 'we', ' ', "don'", ' ', 'lov', ' ', 'anymor', ' ', 'wha', ' ', 'was', ' ', 'all', ' ', 'of', ' ',
             'it', ' ', 'for', ' ', 'oh,', ' ', 'we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'lahyk', ' ', 'we',
             ' ', 'use', ' ', 'to', ' ', 'do', ' ']


daniweb.play_music('jinglebells.mid')

"""
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
