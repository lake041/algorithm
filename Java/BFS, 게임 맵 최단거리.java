import java.util.*;

class Solution {    
    int[] dy = {0, 1, 0, -1};
    int[] dx = {1, 0, -1, 0};

    public int solution(int[][] maps) {
        int N = maps.length;
        int M = maps[0].length;

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1});
        boolean[][] visited = new boolean[N][M];
        visited[0][0] = true;
        
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int y = current[0];
            int x = current[1];
            int cnt = current[2];
            
            if (y == N-1 && x == M-1)
                return cnt;
            
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                
                if (0<=ny && ny<N && 0<=nx && nx<M 
                && maps[ny][nx]==1 && !visited[ny][nx]) {
                    q.add(new int[]{ny, nx, cnt+1});
                    visited[ny][nx] = true;
                }
            }
        }

        return -1;
    }
}