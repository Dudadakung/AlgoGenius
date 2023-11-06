import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf;
    static int n, m;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = i;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(bf.readLine());
            int k = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (k == 1 && isUnion(a, b)) System.out.println("YES");
            if (k == 1 && !isUnion(a, b)) System.out.println("NO");
            else union(a, b);
        }
    }

    public static boolean isUnion(int x, int y){
        return find(x) == find(y);
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
