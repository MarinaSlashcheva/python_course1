import sqlite3 as sq
with sq.connect('data.sqlite') as con:
    cur = con.cursor()

#1 Перечислить пользователей в алфавитном порядке (все колонки в любом порядке)
    for row in cur.execute(
            'select * from  Users '
            'order by username'):
        print(row)

#2 5 пользователей, которые зарегистрировались последними
    for row in cur.execute(
            'select * from  Users '
            'order by registered desc limit 5'):
        print(row)

#3 Топ 5 пользователей по числу прослушиваний
    for row in cur.execute(
            'select username, count(Listened.user_id) from  Listened '
            'inner join Users on user_id = Users.id '
            'group by Listened.user_id '
            'order by count(Listened.user_id) desc limit 5'):
        print(row)

#4 Инфа об исполнителях и количестве их альбомов
    for row in cur.execute(
            'select Artists.name, count(artist_id) from Albums '
            'inner join Artists on artist_id = Artists.id '
            'group by Albums.artist_id '):
        print(row)

#5 Инфа об исполнителях и количестве их песен
    for row in cur.execute(
            'select Artists.id, Artists.name, count(*) from Songs '
            'inner join Albums on album_id = Albums.id '
            'inner join Artists on artist_id = Artists.id '
            'group by artist_id '
            'order by count(*) desc '):
         print(row)

#6 Самый длинный альбом по числу песен
    for row in cur.execute(
            'select Artists.name, Albums.name, count(*) from Songs '
            'inner join Albums on album_id = Albums.id '
            'inner join Artists on artist_id = Artists.id '
            'group by album_id '
            'order by count(*) desc limit 1'):
        print(row)

#7 Самый длинный альбом по суммарной продолжительности
    for row in cur.execute(
            'select Artists.name, Albums.name, total(Songs.duration) from Songs '
            'inner join Albums on album_id = Albums.id '
            'inner join Artists on artist_id = Artists.id '
            'group by album_id '
            'order by total(Songs.duration) desc limit 1'):
        print(row)

#8 Альбом самой большой средней продолжит трека
    for row in cur.execute(
            'select Artists.name, Albums.name, total(Songs.duration)/count(Songs.name) from Songs '
            'inner join Albums on album_id = Albums.id '
            'inner join Artists on artist_id = Artists.id '
            'group by album_id '
            'order by total(Songs.duration)/count(Songs.name) desc limit 1'):
        print(row)

#9 Топ 5 самых прослушиваемых треков
    for row in cur.execute(
            'select Artists.name, Albums.name, Songs.name, '
            'count(*) from Listened '
            'inner join Albums on album_id = Albums.id '
            'inner join Artists on artist_id = Artists.id '
            'inner join Songs on song_id = Songs.id '
            'group by Listened.song_id '
            'order by count(*) desc limit 5'):
        print(row)

#10 Год, что песни, выпущенные в этом году, слушают больше всего
    for row in cur.execute(
            'select Albums.release_year, count(song_id) from Listened '
            'inner join Songs on song_id = Songs.id '
            'inner join Albums on album_id = Albums.id '
            'group by release_year '
            'order by count(song_id) desc'):
        print(row)

#11 Топ 20 песен прослушанных для пользователя с id=47
    for row in cur.execute(
            'select Artists.name, Albums.name, Songs.name, Listened.start_time from Listened '
            'inner join Songs on song_id = Songs.id '
            'inner join Albums on album_id = Albums.id '
            'inner join Artists on artist_id = Artists.id '
            'where user_id = 47 '
            'order by start_time desc limit 20'):
        print(row)

#12 Для каждого пользователя и каждой песни, кот он прослушал, найти количество прослушиваний
    for row in cur.execute(
            'select Users.username, Artists.name, Albums.name, Songs.name, count(*) from Listened '
            'inner join Songs on song_id = Songs.id '
            'inner join Albums on album_id = Albums.id '
            'inner join Artists on artist_id = Artists.id '
            'inner join Users on user_id = Users.id '
            'group by user_id, song_id '
            'order by count(*) desc'):
        print(row)