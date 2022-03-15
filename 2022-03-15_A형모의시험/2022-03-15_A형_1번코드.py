import sys

sys.stdin = open('input.txt', 'r')


def solution(depth, arr):
    global min_

    if depth == 3:
        visited = [0] * (N + 1)
        for j in range(len(arr)):
            gate, people = arr[j][0], arr[j][1]
            if visited[gate] == 0:
                visited[gate] = 1
                people -= 1

            while people > 0:
                result = []
                for i in range(2):
                    temp_gate = gate
                    count = 1
                    while True:
                        new_gate = temp_gate + brr[j][i]

                        if new_gate <= 0 or new_gate >= N + 1:
                            break
                        count += 1
                        if visited[new_gate] == 0:
                            result.append([new_gate, count])
                            break
                        temp_gate = new_gate

                if len(result) == 1:
                    visited[result[0][0]] = result[0][1]
                    people -= 1
                elif len(result) > 1:
                    if result[0][1] < result[1][1]:
                        visited[result[0][0]] = result[0][1]
                    elif result[0][1] > result[1][1]:
                        visited[result[1][0]] = result[1][1]
                    else:
                        visited[result[0][0]] = result[0][1]
                    people -= 1

                if people <= 0:
                    break

                if sum(visited) > min_:
                    return

        if sum(visited) < min_:
            min_ = sum(visited)
        return

    for i in [[-1, 1], [1, -1]]:
        brr.append(i)
        solution(depth + 1, arr)
        brr.pop()


def dfs(depth):
    if depth == 3:
        solution(0, arr)
        return

    for i in range(3):
        if not visited_gate[i]:
            visited_gate[i] = True
            arr.append(info[i])
            dfs(depth + 1)
            arr.pop()
            visited_gate[i] = False


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    info = []
    for i in range(3):
        gate, people = map(int, input().split())
        info.append([gate, people])
    visited_gate = [False] * 3
    arr = []
    brr = []
    min_ = 1 << 60

    dfs(0)
    print(f'#{tc} {min_}')
