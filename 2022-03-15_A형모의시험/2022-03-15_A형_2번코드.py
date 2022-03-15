import sys

sys.stdin = open('input2.txt', 'r')


def dfs(depth):
    global min_
    global arr

    # 만약 1개 이상 뽑았다면(가지치기)
    if len(loc) > depth >= 1:
        if miro[arr[depth][0]][arr[depth][1]] < 0:  # 만약 사람인데 아직 몬스터를 잡지않았다면 재귀종료
            if not visited_monster[abs(miro[arr[depth][0]][arr[depth][1]])]:
                return

    # 만약 깊이가 사람수 + 몬스터 수와 같다면
    elif depth == len(loc):

        distance = 0  # 거리 0으로 초기화
        for i in range(len(arr) - 1):  # 돌면서 길이의 차만큼 계속 더해준다.
            distance += abs(arr[i + 1][0] - arr[i][0]) + abs(arr[i + 1][1] - arr[i][1])
            if distance >= min_:  # 만약 그 거리가 저장된 길이보다 이미 같거나 크다면
                return  # 종료
        if distance < min_:  # 만약 거리가 더 짧다면
            min_ = distance  # 최솟값으로 설정
        return

    for i in range(len(loc)):
        if not visited[i]:  # 만약 방문하지 않았다면
            visited[i] = True  # 해당 위치를 방문처리
            arr.append(loc[i])  # 몬스터와 사람 위치 하나를 넣어준다.
            if miro[loc[i][0]][loc[i][1]] > 0:  # 만약 몬스터라면
                visited_monster[miro[loc[i][0]][loc[i][1]]] = True  # 해당 몬스터의 방문 여부를 True설정
            dfs(depth + 1)  # dfs돈다.
            temp = arr.pop()  # 재귀를 돌았다면 다시 원소를 하나 빼준다.
            if miro[temp[0]][temp[1]] > 0:  # 그 원소가 몬스터라면
                visited_monster[miro[temp[0]][temp[1]]] = False  # 방문 여부 다시 False
            visited[i] = False  # 해당 위치 방문처리 False


T = int(input())

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
for tc in range(1, T + 1):
    N = int(input())
    miro = []  # 미로 저장
    loc = []  # 사람,몬스터 위치 저장
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(len(temp)):
            if temp[j] != 0:
                loc.append([i, j])
        miro.append(temp)
    arr = [[0, 0]]
    visited = [False] * len(loc)
    visited_monster = [False] * 5
    min_ = 1 << 60  # 출력할 최솟값
    dfs(0)
    print(f'#{tc} {min_}')
