from collections import deque


def bfs(tree, start, desired):
    P, Q = {start: None}, deque([start])
    while Q:
        u = Q.popleft()
        for v in tree[u]:
            if v in P: continue
            if v == desired:
                return True
            P[v] = u
            Q.append(v)
    return False


def test_bfs():
    tree = {
        1: [2, 3, 4],
        2: [5, 6],
        3: [],
        4: [7, 8],
        5: [9, 10],
        6: [],
        7: [11, 12],
        8: [],
        9: [],
        10: [],
        11: [],
        12: []
    }
    if bfs(tree, 1, 11):
        print('OK')
    if bfs(tree, 1, 6):
        print('OK')
    if bfs(tree, 2, 10):
        print('OK')
    if not bfs(tree, 2, 11):
        print('OK')
    if bfs(tree, 4, 12):
        print('OK')
    if not bfs(tree, 4, 10):
        print('OK')


def main():
    test_bfs()


if __name__ == '__main__':
    main()