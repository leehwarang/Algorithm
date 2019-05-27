def solution(clothes):
    dict = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] in dict.keys():
            value = cloth[0]
            key = cloth[1]
            dict[key].append(value)
        else:
            value = cloth[0]
            key = cloth[1]
            dict[key] = []
            dict[key].append(value)

    for d in dict:
        answer *= len(dict[d]) + 1
    return answer - 1