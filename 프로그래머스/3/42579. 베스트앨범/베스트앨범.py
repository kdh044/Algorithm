def solution(genres, plays):
    answer = []

    song = {}
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in song:
            song[genre] += play
        else:
            song[genre] = play

        if genre in genre_songs:
            genre_songs[genre].append((play, i))
        else:
            genre_songs[genre] = [(play, i)]

    genres_sorted = sorted(song, key=song.get, reverse=True)

    for genre in genres_sorted:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))

        for s in songs[:2]:
            answer.append(s[1])

    return answer