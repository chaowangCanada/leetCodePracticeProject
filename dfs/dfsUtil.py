class dfsUtil:
    @staticmethod
    def dfs(temp, key, graph, visited):
        visited[key] = True

        temp.append(key)

        for i in graph[key]:
            if not visited[i]:
                temp = dfsUtil.dfs(temp, i, graph, visited)
        return temp
