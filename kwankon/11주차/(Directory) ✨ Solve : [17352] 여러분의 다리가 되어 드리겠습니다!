import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf;
    static int n;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());
        dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = i;
        for (int i = 0; i < n - 2; i++) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            union(a, b);
        }
        int start = 0;
        int end = 0;
        for (int i = 1; i <= n; i++) {
            if (dp[i] != i) continue;
            if (start == 0) start = i;
            else end = i;
        }
        System.out.println(start + " " + end);
    }

    public static int find(int x) {
        if (x == dp[x]) return x;
        return dp[x] = find(dp[x]);
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return;
        if (x > y) dp[x] = y;
        else dp[y] = x;
    }
}
