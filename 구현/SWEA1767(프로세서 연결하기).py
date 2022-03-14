def remove(depth, dir, error):
    global connect
    # 행,열 좌표를 받는다.
    r, c = maxinos[depth][0], maxinos[depth][1]
    # 좌표를 돈다.
    while True:
        nr = r + dr[dir]
        nc = c + dc[dir]

        # 끝까지 왔을때
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            break
        # -1이라면 다시 0으로 바꿔준다.
        if processer[nr][nc] == -1:
            processer[nr][nc] = 0
        # 계속해서 이동하기 위해 좌표를 다음좌표로 이동
        r, c = nr, nc
    # 만약 에러가 아니라면 연결된 개수에서 -1
    if not error:
        connect -= 1


def solution(depth):
    global connect
    global max_connect
    global result
    # 만약 깊이가 1~맥시노스의 개수사이라면
    if 0 < depth <= len(maxinos):
        # 전선의 길이를 구해준다.
        length = 0
        for i in range(N):
            length += processer[i].count(-1)

        # 현재 저장된 최대 맥시노스개수보다 연결된 맥시노스의 개수가 더 많다면
        if max_connect < connect:
            max_connect = connect  # 그 개수를 최대연결된 맥시노스의 개수로 저장
            result = length

        # 현재 저장된 최대 맥시노스개수와 연결된 맥시노스의 개수가 동일하다면
        elif max_connect == connect:
            if result > length:  # 저장된 전선의 길이보다 짧다면
                result = length  # 그 길이를 저장
        # 현재 저장된 맥시노스의 연결 개수 보다 적다면
        else:
            if length > result:  # 이미 저장된 길이보다 길다면
                return  # 더돌 필요가 없으므로 리턴
        # 깊이가 이미 맥시노스의 길이만큼 돌았다면
        if depth == len(maxinos):
            return  # 재귀 종료

    error_stack = 0  # 에러 스택 저장
    for j in range(4):
        r, c = maxinos[depth][0], maxinos[depth][1]
        error = False  # 에러 여부(연결되지 못했다면 에러 True 저장)
        while True:
            nr = r + dr[j]
            nc = c + dc[j]

            r, c = nr, nc
            # 만약 범위내에 있고 0이 아니라면 에러가 발생한 것이므로
            if 0 <= nr < N and 0 <= nc < N and processer[nr][nc] != 0:
                while True:  # 다시 반대로 돈다.
                    nr = r - dr[j]
                    nc = c - dc[j]
                    # 다시 반대로 돌다 시작지점까지 왔다면
                    if nr == maxinos[depth][0] and nc == maxinos[depth][1]:
                        error = True  # 에러 여부를 True로 변경 후
                        break  # 탈출

                    processer[nr][nc] = 0  # 해당 프로세스 값을 다시 0으로 바꿔준다.

                    r, c = nr, nc  # 계속 이동

            # 만약 범위내에 있고 값이 0이라면
            elif 0 <= nr < N and 0 <= nc < N and processer[nr][nc] == 0:
                processer[nr][nc] = -1  # 그 값을 전선으로 바꾸기위해 -1로 표시

            # 끝까지 왔을때
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                connect += 1  # 연결 개수를 1개 추가 후
                break  # 반복문 탈출

            if error:  # 만약 에러라면
                break  # 반복문 탈출

        if error:  # 만약 에러라면
            error_stack += 1  # 에러스택한개 추가 후
            if error_stack != 4:  # 에러가 4개(모든방향이 에러)가 아니라면
                continue  # 다음재귀를 실행하지 않고 다음 방향을 검사한다.

        solution(depth + 1)  # 재귀를 돈다.
        remove(depth, j, error)  # 탐색 했던 길이를 돌고 난 후 다시 0으로 바꿔준다.


T = int(input())

dr = [-1, 0, 1, 0]  # 행 상 우 하 좌
dc = [0, 1, 0, -1]  # 행 상 우 하 좌

for tc in range(1, T + 1):

    N = int(input())
    processer = []  # 프로세스 전체 배치도
    maxinos = []  # 맥시노스 좌표(가장자리 제외)
    result = 1 << 60  # 출력할 전선의 최소 길이
    connect = 0  # 작동된 매시노스 개수
    max_connect = 0  # 최대 맥시노스 작동 개수

    # 맥시노스의 좌표 저장(단, 가장자리의 맥시노스는 저장x)
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(len(temp)):
            if temp[j] == 1:
                if i != 0 and j != 0 and i != N - 1 and j != N - 1:
                    maxinos.append((i, j))
        processer.append(temp)

    solution(0)  # 재귀를 돈다.
    print(f'#{tc} {result}')
