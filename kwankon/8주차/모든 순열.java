import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf;
    static int[] ans = new int[9];
    static int n;
    static ArrayList<Integer> v = new ArrayList<Integer>();

    public static void main(String[] args) throws IOException {
        bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());
        solution();
    }

    public static void solution() {
        if (v.size() == n) {
            for (Integer integer : v) System.out.print(integer + " ");
            System.out.println();
        }
        for (int i = 1; i <= n; ++i) {
            if (ans[i] == 0) {
                ans[i] = 1;
                v.add(i);
                solution();
                ans[i] = 0;
                v.remove(v.size() - 1);
            }
        }
    }
}
