# Don`t pay attention to it, this function invert the dictionary
def invert_my_dict(dict):
    inv_dict = {}
    for key in dict:
        val = dict[key]
        if val not in inv_dict:
            inv_dict[val] = [key]
        else:
            inv_dict[val].append(key)
    return inv_dict

class Song:
    def __init__(self, artist, name, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = year
        self.duration = duration

    def __repr__(self):
        song = 'Song ' + self.name + ' by ' + self.artist + ' Album: ' + self.album + ' №:' + self.position + ' Year:' + self.year + ' Duration:' + self.duration
        return song

    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False

def import_songs(file_name):
    with open(file_name, 'r') as songs:
        all_songs = songs.read()
    all_songs = all_songs.split('\n')
    songs = []
    for song in all_songs:
        tmp = song.split('\t')
        if len(tmp) == 6:
            name, artist, album, position, year, duration = song.split('\t')
            songs.append(Song(artist, name, album, position, year, duration))
    return(songs)

songs = import_songs('songs1.txt')

def export_songs(songs, file_names):
    export_song = open(file_names, 'w')
    for song in songs:
        export_song.write('\t'.join([song.name, song.artist, song.album, song.position, song.year, song.duration]))
        export_song.write('\n')
    export_song.close()

def shuffle_songs(songs):
    from random import shuffle
    shuffled_songs = songs
    shuffle(shuffled_songs)
    return(shuffled_songs)

# Вывести на экран самого часто встречающегося исполнителя (по числу песен), если таких несколько, вывести любого из них (artist_name)

artist_list = []
for song in songs:
    artist_list.append(song.artist)
import collections
dict = collections.Counter(artist_list)
inv_dict = invert_my_dict(dict)
for i in inv_dict[max(inv_dict.keys())]:
    print(i)

# Вывести на экран самую длинную песню, если таких несколько, вывести любую из них (song_name (TAB) artist_name)

current_duration = 0
for song in songs[1:]:
    if int(song.duration) > int(current_duration):
        current_duration = song.duration
        longest = (song.name+'\t'+song.artist)
print(longest)

#Вывести на экран самый длинный (по длительности) альбом (песни считаются в одном альбоме, если название альбомов и название исполнителей совпадают), если таких несколько, вывести любой из них (album_name (TAB) artist_name)
album_dur = {}
for song in songs:
    key_tmp = (song.album+'\t'+song.artist)
    if key_tmp not in album_dur:
        album_dur[key_tmp] = int(song.duration)
    else:
        album_dur[key_tmp] += int(song.duration)
longest_album = invert_my_dict(album_dur)
for i in longest_album[max(longest_album.keys())]:
    print(i)

#Вывести на экран 10 слов наиболее встречающихся в названиях песен

name_word = []
import re
for song in songs:
    list_w = song.name.split(' ')
    for word in list_w:
        word = word.lower()
        word = re.findall('[a-z]+', word)
        for i in word:
            name_word.append(i)
word_dict = collections.Counter(name_word)
word_dict = invert_my_dict(word_dict)

n = 0
while n < 10:
    word = word_dict[max(word_dict.keys())]
    for i in word:
        print(i, end='\t')
    del(word_dict[max(word_dict.keys())])
    n += 1


# Вывести на экран исполнителя с наибольшим числом альбомов
albums = {}
all_album = []
for song in songs:
    if song.artist not in albums:
        albums[song.artist] = 1
    else:
        if song.album in all_album:
            continue
        else:
            albums[song.artist] += 1
    all_album.append(song.album)

albums_inv = invert_my_dict(albums)
for i in albums_inv[max(albums_inv.keys())]:
    print('\n', i)
    break