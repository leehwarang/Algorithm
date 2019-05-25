def solution(heights):
    answer = []
    while len(heights) != 0:
        top = heights.pop()
        if len(heights) == 0:
            answer.append(0)
            answer = answer[::-1]
            return answer

        top_index = len(heights) - 1

        while top_index >= 0:
            if top < heights[top_index]:
                answer.append(top_index + 1)
                break
            else:
                if top_index == 0 and top >= heights[top_index]:
                    answer.append(0)
                top_index -= 1
