import java.util.*;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        Integer[][] arr = {{0, 1}, {2, 3}, {1, 1}, {3, 3}, {2, 2}, {3, 1}, {0, 2}};
        
        Arrays.sort(arr, new Comparator<Integer[]>() {
            public int compare(Integer[] a, Integer[] b) {
                if (a[1].equals(b[1])) {
                    return b[0].compareTo(a[0]); // 두 번째 요소가 같으면 첫 번째 요소의 내림차순으로 정렬
                }
                return a[1].compareTo(b[1]); // 먼저 두 번째 요소의 오름차순으로 정렬
            }
        });
        
        for (Integer[] x : arr) {
            System.out.println(Arrays.toString(x));
        }
    }
}
