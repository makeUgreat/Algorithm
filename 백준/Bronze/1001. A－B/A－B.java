import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        try {
            int a = in.nextInt();
            // nextInt는 입력값 중 정수만 읽어낸다
            int b = in.nextInt();
            System.out.println(a-b);

        } catch (InputMismatchException e) {
            System.out.println("정수가 아닌 값이 포함된 입력");
        }

    }
}
