class Solution {
    public boolean solution(String s) {
        int openCount = 0;
        int closeCount = 0;

        for (char c : s.toCharArray()) {
            if (c == '(')
                openCount++;
            else if (c == ')')
                closeCount++;
            
            if (openCount < closeCount)
                return false;
        }
        
        if (openCount == closeCount)
            return true;
        return false;
    }
}