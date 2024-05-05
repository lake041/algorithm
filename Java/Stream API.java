import java.util.*;
import java.util.stream.*;

class StreamAPI {
    public void solution() {
        String[] arr = {"apple", "banana", "cherry"};
        Stream<String> stream = Arrays.stream(arr);

        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> filteredNumbers =
            list.stream()
            .filter(x -> x % 2 == 0)
            .collect(Collectors.toList());

        List<String> uppercased =
            Arrays.asList("apple", "banana", "cherry").stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());

        List<Integer> sortedNumbers = 
            Arrays.asList(5, 3, 8, 2).stream()
            .sorted()
            .collect(Collectors.toList());

        list.stream().forEach(System.out::println); // 1, 2, 3, 4, 5 출력

        String resultString = stream.collect(Collectors.joining(", "));
        System.out.println(resultString); // apple, banana, cherry

        Integer sum = list.stream().reduce(0, (a, b) -> a + b);
        long count = list.stream().filter(x -> x > 2).count();

        boolean anyMatch = list.stream().anyMatch(x -> x > 4);
        boolean allMatch = list.stream().allMatch(x -> x > 0);
        boolean noneMatch = list.stream().noneMatch(x -> x < 0);
    }
}
