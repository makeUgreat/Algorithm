import java.util.stream.*;

class Solution {
    boolean solution(String s) {
        int balance = s.toLowerCase().chars()
            .map(c -> {
                if ( c == 'p' ) return 1;
                else if (c == 'y') return -1;
                else return 0;
            }).sum();

        return balance == 0;
    }
}