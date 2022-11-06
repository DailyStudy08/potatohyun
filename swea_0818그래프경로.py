from pprint import pprint

def dfs(graph,S):
    stack = []
    stack.append(S)
    visited[S] = 1
    # print(visited)
    while stack:
        top = stack[-1]
        for i in range(V+1):
            if graph[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    print(visited)

    for e in range(E):
        a,b = map(int, input().split())
        graph[a][b] = 1
    S, G = map(int, input().split())
    dfs(graph,S)

    # pprint(graph)
    if visited[G]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

    
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''