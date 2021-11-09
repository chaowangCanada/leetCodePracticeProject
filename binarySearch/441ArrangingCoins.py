# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.

def arrangeCoins(self, n: int) -> int:
    return (int)((2 * n + 0.25) ** 0.5 - 0.5)

def arrangeCoins2(self, n: int) -> int:
    left, right = 0, n
    while left <= right:
        mid = (left + right) //2
        print("mid: ", mid)
        if mid * (mid +1) // 2 == n:
            return mid
        elif mid * (mid +1) // 2 < n:
            left = mid + 1
            print("left", left)
        else :
            right = mid - 1
            print("right", right)
    return right


if __name__ == '__main__':
    arrangeCoins2(None, 5)

