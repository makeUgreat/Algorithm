import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int price = sc.nextInt();
        int[] money = {500,100,50,10,5,1};
        int cnt = 0;

        int changes = 1000 - price;
        for (int m : money) {
            cnt += changes / m;
            changes %= m;
        }

        System.out.println(cnt);
    }
}