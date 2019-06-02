def solution(prices):
    answer = []
    for i, x in enumerate(prices):
        cnt = 0
        if i == len(prices) - 1:
            answer.append(cnt)
            return answer
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[i] <= prices[j]:
                if j == len(prices) - 1:
                    answer.append(cnt)
            else:
                answer.append(cnt)
                break
