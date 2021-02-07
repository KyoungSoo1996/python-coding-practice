def solution(genres, plays):
    answer = []
    genresList = set(genres)
    print(genresList)
    di = {}

    for i in range(len(genres)):
        di[i] = [testGenres[i], testPlays[i]]

    for i in di:
        print(i)
    # for i in range(len())
    return answer


testGenres = ["classic", "pop", "classic", "classic", "pop"]
testPlays = [500, 600, 150, 800, 2500]

print(solution(testGenres, testPlays))
