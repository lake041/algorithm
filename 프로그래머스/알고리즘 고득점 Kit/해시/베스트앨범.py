from collections import defaultdict

# 둘 다 읽기 힘들다.
# 1. 에전 풀이
def solution(genres, plays):
    answer = []
    lenT = len(genres)
    
    # step 1
    dic1 = defaultdict(int)
    for i in range(lenT):
        dic1[genres[i]] += plays[i]
    dicL = sorted(dic1.items(), key = lambda x : x[1])
    
    # step 2
    dic2 = defaultdict(list)
    for i in range(lenT):
        dic2[genres[i]].append([plays[i], i])
    
    # step 3
    while dicL:
        nextGenre = dicL.pop()[0]
        temp = sorted(dic2[nextGenre], key = lambda x :(x[0], -x[1]))
        for i in range(2):
            if temp:
                answer.append(temp.pop()[1])
    return answer

# 2. 지금 풀이
def solution(genres, plays):
    genre_count = defaultdict(int)
    for i in range(len(plays)):
        genre = genres[i]
        genre_count[genre] += plays[i]
    
    play_list = []
    for index, play_count in enumerate(plays):
        genre = genres[index]
        play_list.append((genre_count[genre], play_count, index))
    play_list.sort(key = lambda x : (-x[0], -x[1], x[2]))
    
    answer = []
    prev_genre = 0
    best_song_count = 0
    for song in play_list:
        now_genre = song[0]
        if prev_genre == now_genre:
            best_song_count += 1
        else:
            prev_genre = now_genre
            best_song_count = 1
        if best_song_count <= 2:
            answer.append(song[2])
        
    return answer