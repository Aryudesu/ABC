import heapq

def lexicomin_euler_cycle_complete_graph(N: int, start: int = 1):
    assert N % 2 == 1, "N が偶数だと K_N はオイラー巡回路を持たない"
    # 隣接ヒープ（完全グラフなので全部入れる）
    g = [[] for _ in range(N+1)]
    for u in range(1, N+1):
        for v in range(1, N+1):
            if u != v:
                g[u].append(v)
        heapq.heapify(g[u])

    used = set()  # (a,b)
    st = [start]
    tour = []

    while st:
        u = st[-1]
        # 未使用辺で行ける最小 v を探す
        while g[u]:
            v = heapq.heappop(g[u])
            a, b = (u, v) if u < v else (v, u)
            if (a, b) in used:
                continue
            used.add((a, b))
            st.append(v)
            break
        else:
            # 行き止まり：確定
            tour.append(st.pop())

    tour.reverse()  # 頂点列（長さ E+1）
    return tour


