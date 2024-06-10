import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            try {
                int a = sc.nextInt();
                int b = sc.nextInt();
                int c = sc.nextInt();

                System.out.println(maxMoves(a,b,c));
            } catch (Exception e) {
                break;
            }
        }
        sc.close();
    }

    public static int maxMoves(int a, int b, int c) {
        return Math.max(b-a, c-b) - 1;
    }
}