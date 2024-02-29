import java.util.*;   // import 구문은 하위 패키지를 자동으로 포함하지 않음 따라서 해당 코드는 util에 있는 동위 레벨 패키지들만 불러옴
import java.util.stream.*; // 이렇게해야 stream에 필요한 패키지들을 호출할 수 있음 

class Solution {
    public int solution(int n) {        
        // for (int x = 2; x < n; x++) {
        //     if (n % x == 1) {
        //         return x;
        //     }
        // }
        // return -1;
        
        return IntStream.range(2,n).filter(x -> n%x == 1).findFirst().getAsInt();
    }
}