import sys
input = sys.stdin.readline

def main():

    # 어려웠던 점:
    # 빈칸을 0으로 저장해뒀는데 좌표 0으로 가는 손님을 빈칸 취급해서 오래걸림

    N, M, fuel = map(int, input().split())
    L = N+1
    brd = [-1] * L*L # 벽은 -1로, 빈칸은 -2로 저장
    for y in range(0, N*L, L):
        brd[y:y+N] = map(lambda x: int(x)-2, input().split())
    dir = (-L, -1, 1, L)
    dst = -1    # dst는 승객을 찾은 경우엔 목적지 좌표 저장, 승객 목적지 도달시 -1로 초기화.
    ans = -1
    ty, tx = map(lambda x: int(x)-1, input().split())
    cque = [ty*L+tx]

    # 지도 각 승객 위치에 목적지 좌표를 저장
    for _ in range(M):
        sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
        brd[sy*L+sx] = ey*L+ex

    for _ in range(M):
        
        '''승객 찾기 페이즈'''
        vis = [0] * N*L
        mnm = len(brd)
        for fuel in range(fuel, 0, -1):
            nque = []
            for cur in cque:
                if brd[cur] >= 0 and cur < mnm:
                    mnm = cur
                    dst = brd[mnm]

                for d in dir:
                    if brd[cur+d] != -1 and not vis[cur+d]:
                        vis[cur+d] = 1
                        nque.append(cur+d)

            if dst != -1:
                brd[mnm] = -2
                cque = [mnm]
                break
            cque = nque
            
        if dst == -1: # 다음 승객을 못찾아 목적지 갱신이 안된 경우
            break

        '''목적지 찾기 페이즈'''
        vis = [0] * N*L
        for used in range(fuel+1):
            nque = []
            for cur in cque:
                if cur == dst:
                    cque = [dst]
                    dst = -1
                    break

                for d in dir:
                    if brd[cur+d] != -1 and not vis[cur+d]:
                        vis[cur+d] = 1
                        nque.append(cur+d)
            
            if dst == -1:
                fuel += used
                break
            cque = nque

        if dst != -1: # 목적지를 못찾아 -1로 초기화가 안된 경우
            break
        
    else: # for문 M번 다 돈 경우 == 모든 손님을 태운 경우
        ans = fuel

    print(ans)

if __name__ == "__main__":
    main()