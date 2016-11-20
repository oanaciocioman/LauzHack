import sys
import os
from urllib.request import urlopen

midi_file = "music file";
syl_link = "https://www.howmanysyllables.com/words/"

def get_syl_word(word, isRec):
	syllabled = word
	if len(word) > 3 or word.find("'"):
		link = syl_link + word
		source = urlopen(link)
		source = source.read().decode('utf-8')[12500 : 13500]

		start = source.find('<br>How to pronounce')
		start = source.find('_Red">', start)
		start += len('_Red">')
		end = source.find('</span>', start)
		syllabled = source[start : end]
		if isRec:
			syllabled += 's'

		if (syllabled.find('>') > 0 or syllabled.find('<') > 0) and isRec == False:
			return get_syl_word(word[:-1], True)
		elif isRec == True:
			return word

	return syllabled

def get_syl_lyrics(lyrics):
	syllabled_lyr = []
	lyrics = lyrics.lower().split(' ')
	for word in lyrics:
		syllabled_word = get_syl_word(word, False)
		syllabled_lyr += syllabled_word.split('-')
		syllabled_lyr += [' ']
	return syllabled_lyr

def get_file():
	music = sys.argv[1]
	# global midi_file = os.path.basename(music)
	return music

print(get_syl_lyrics("Jingle bells jingle bells jingle all the way oh what fun it is to ride in a one horse open sleigh oh the weather outside is frightful but the fire is so delightful and since we've no place to go let it snow"))


print(len(['we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'we', ' ', "don'", ' ', 'tawk', ' ', 'anymor', ' ', 'we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'lahyk', ' ', 'we', ' ', 'use', ' ', 'to', ' ', 'do', ' ', 'we', ' ', "don'", ' ', 'lov', ' ', 'anymor', ' ', 'wha', ' ', 'was', ' ', 'all', ' ', 'of', ' ', 'it', ' ', 'for', ' ', 'oh,', ' ', 'we', ' ', "don'", ' ', 'tawk', ' ', 'anymore', ' ', 'lahyk', ' ', 'we', ' ', 'use', ' ', 'to', ' ', 'do', ' ']))
