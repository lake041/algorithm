import java.util.*;

class Solution {
    public boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        // Stack<Character> 제네릭 타입 Stack에 구체적인 타입 매개변수로 Character 사용
        // new Stack<>() 다이아몬드 연산자를 사용한 인스턴스 생성문, 타입 추론을 통해 제네릭 타입을 자동으로 채워넣음
        
        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(c);       
            else if (c == ')') {
                if (stack.isEmpty()) return false;
                stack.pop();
            } 
        }

        return stack.isEmpty();
    }
}