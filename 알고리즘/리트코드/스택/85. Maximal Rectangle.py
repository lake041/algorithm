# 비슷한 문제
# 85. Maximal Rectangle (https://leetcode.com/problems/maximal-rectangle/description/)
# 최대 직사각형 (https://www.acmicpc.net/problem/11873)
# 84. Largest Rectangle in Histogram (https://leetcode.com/problems/largest-rectangle-in-histogram/)
# 히스토그램에서 가장 큰 직사각형 (https://www.acmicpc.net/problem/6549)
# 히스토그램 (https://www.acmicpc.net/problem/1725)

# 이것도 같은 방식으로 풀 수 있음
# 가장 큰 정사각형 찾기 (https://school.programmers.co.kr/learn/courses/30/lessons/12905)

class Solution:
    def maximalRectangle(self, bod: list[list[str]]) -> int:
        bod = [row + ["0"] for row in bod]
        H = [0]*len(bod[0])
        nemo = []

        for row in bod:
            H = [prev+1 if now=="1" else 0 for prev, now in zip(H, row)]
            stack = [(-1, 0)]
            for index, height in enumerate(H):
                while stack and height < stack[-1][1]:
                    h = stack.pop()[1]
                    w = index - stack[-1][0] -1
                    nemo.append(h*w)
                stack.append((index, height))

        return max(nemo) if nemo else 0