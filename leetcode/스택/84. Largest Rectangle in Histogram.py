class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights += [0]
        stack = [(-1, 0)]
        nemo = []

        for index, height in enumerate(heights):
            while stack and height < stack[-1][1]:
                h = stack.pop()[1]
                w = index - stack[-1][0] - 1
                nemo.append(h*w)
            stack.append((index, height))
        
        return max(nemo) if nemo else 0