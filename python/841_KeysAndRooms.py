from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        l = len(rooms)
        visited = [False] * l

        def dfs(index: int):
            if visited[index]:
                return
            visited[index] = True
            for key in rooms[index]:
                dfs(key)

        dfs(0)
        return all(visited)
