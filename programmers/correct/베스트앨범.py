def solution(genres, plays):
    answer = []
    num_of_music = len(plays)
    music_dict = {}
    """
    music_dict = {
        "장르" : {
            "total_plays" : 장르 별 총 재생 수,
            "musics" : {
                "재생 수" : [같은 재생 수인 음악의 고유 번호 리스트]
            }
        }
    }
    """
    genre_plays = []
    
    for i in range(num_of_music): # music_dict 만들기
        if genres[i] in music_dict:
            if plays[i] in music_dict[genres[i]]["musics"]:
                music_dict[genres[i]]["musics"][plays[i]].append(i)
            else:
                music_dict[genres[i]]["musics"][plays[i]] = [i]
            music_dict[genres[i]]["total_plays"] += plays[i]
        else:
            music_dict[genres[i]] = {
                "musics" : {plays[i] : [i]},
                "total_plays" : plays[i]
            }

    for md_key in music_dict: # total_plays 계산 + 고유번호 리스트 고유번호 순서대로 정렬
        genre_plays.append((md_key, music_dict[md_key]["total_plays"]))
        for p in music_dict[md_key]["musics"]:
            music_dict[md_key]["musics"][p] = sorted(music_dict[md_key]["musics"][p])
    genre_plays = sorted(genre_plays, key=lambda r:r[1], reverse=True) # (장르, 총재생수) 리스트. 총 재생 수가 많은 장르부터 정렬

    for gp in genre_plays:
        genre = gp[0]
        candidate = []
        musics = music_dict[genre]["musics"]
        music_plays = list(musics.keys())
        music_plays = sorted(musics, reverse=True)
        for play in music_plays:
            candidate += music_dict[genre]["musics"][play] # 각 장르에서 재생수, 고유번호 순서 이렇게 2가지 기준으로 음악 정렬
        answer += candidate[:2] # 최대 상위 2개만 뽑음

    return answer