# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer
# temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
from typing import List


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    output = [0 for _ in temperatures]
    stack = []
    for i in range(len(temperatures)-1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        if stack:
           output[i] = stack[-1] - i
        stack.append(i)
    return output

if __name__ == '__main__':
    print(dailyTemperatures(None,  [73,74,75,71,69,72,76,73]))

