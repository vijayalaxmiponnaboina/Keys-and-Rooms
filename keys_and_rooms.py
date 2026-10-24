from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n=len(rooms)
        visited=[False]*n
        q=deque([0])
        visited[0]=True
        while q:
            front=q.popleft()
            for x in rooms[front]:
                if not visited[x]:
                    q.append(x)
                    visited[x]=True
        for val in visited:
            if val==False:
                return False
        return True