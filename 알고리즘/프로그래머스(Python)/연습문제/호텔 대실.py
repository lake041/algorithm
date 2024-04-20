def solution(book_time):
    answer = 0
    number = [0]*(24*60+60)

    for time in book_time:
        start = int(time[0][0:2])*60 + int(time[0][3:5])
        end = int(time[1][0:2])*60 + int(time[1][3:5]) + 10
        for i in range(start, end):
            number[i] += 1
    answer = max(number)
    
    return answer