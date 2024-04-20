import java.util.*;

class Solution {
    public String solution(String s) {
        int[] numbers = Arrays.stream(s.split(" "))
            .mapToInt(Integer::parseInt) // 메소드 참조 (method reference), 특정 메소드를 직접 호출하는 대신 메소드의 참조를 전달
            .sorted()
            .toArray();

        return numbers[0] + " " + numbers[numbers.length - 1];
    }
}