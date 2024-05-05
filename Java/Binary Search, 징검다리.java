import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);
        
        int left = 0;
        int right = distance;
        int result = Integer.MIN_VALUE;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            int cnt = 0;
            int prev = 0;
            
            for (int rock : rocks) {
                if (rock - prev < mid) {
                    cnt += 1;
                } else {
                    prev = rock;
                }
            }
            
            if (distance - prev < mid) {
                cnt += 1;
            }
            
            if (cnt <= n) {
                left = mid + 1;
                result = mid;
            } else {
                right = mid - 1;
            }
        }
        
        return result;
    }
}