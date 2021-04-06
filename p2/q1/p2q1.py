def dfs(graph, start, end):
    fringe = [(start, [])]
    count = 0
    print(fringe)
    while fringe:
        count += 1
        if count > 100000:
            break
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

def get_cycle(followers,s):
    graph ={}
    for i in range(len(followers)):
        graph[i] = followers[i]
    
    cycles = [[s]+path for path in dfs(graph, s, s)]
    if len(cycles) == 0:
        return []
    cycles.sort(key=len,reverse=True)
    return list(reversed(cycles[0]))