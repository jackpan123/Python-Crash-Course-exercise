def make_album(singer_name, album_name, song_number=''):
    album = {'singer_name': singer_name, 'album_name': album_name}
    if song_number:
        album['song_number'] = song_number
    return album


while True:
    print("Input your favorite singer and album:")
    print("(enter 'q' to quit)")
    s_name = input("singer name:")
    if s_name == 'q':
        break

    a_name = input("album name:")
    if a_name == 'q':
        break

    print(make_album(s_name, a_name))


# print(make_album('jack', 'plant', 14))
# print(make_album('pan', 'boss'))
# print(make_album('mess', 'yet'))