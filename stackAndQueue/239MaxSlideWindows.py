from collections import deque
# Driver method
def printMax(arr, n, k):
    Qi = deque()

    for i in range(k):
        while Qi and arr[i] > arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    print(Qi)

    for i in range(k, n):
        print(arr[Qi[0]])

        while Qi and Qi[0] <= i - k:
            Qi.popleft()


        while Qi and arr[i] > arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)
        print(Qi)
    print(str(arr[Qi[0]]))
if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    n = len(arr)
    k = 3
    printMax(arr, n, k)
