class bfsUtil:
    @staticmethod
    def bfs(temp, key, graph, visited):
        visited[key] = True
        queue = []
        queue.append(key)

        while queue:
            s = queue.pop(0)

            for i in graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
        return temp
