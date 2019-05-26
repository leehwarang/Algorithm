def solution(phone_book):

    for i, j in enumerate(phone_book):
        if i == 0:
            for k in phone_book[i + 1:]:
                if j == k[:len(j)]:
                    answer = False
                    return answer
        else:
            for x in phone_book[0:i]:
                if j == x[:len(j)]:
                    answer = False
                    return answer
            for y in phone_book[i + 1:]:
                if j == y[:len(j)]:
                    answer = False
                    return answer

    answer = True
    return answer