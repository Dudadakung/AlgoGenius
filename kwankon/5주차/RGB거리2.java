import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf;
    static int n;
    static int[][] check;

    public static void main(String[] args) throws IOException {
        bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());
        check = new int[n+1][3];
        input();
        int ans = solve(0, 1);
        ans = Math.min(ans, solve(0, 2));
        ans = Math.min(ans, solve(1, 0));
        ans = Math.min(ans, solve(1, 2));
        ans = Math.min(ans, solve(2, 0));
        ans = Math.min(ans, solve(2, 1));
        System.out.println(ans);
    }
    static void input() throws IOException {
        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
            check[i][0] = Integer.parseInt(st.nextToken());
            check[i][1] = Integer.parseInt(st.nextToken());
            check[i][2] = Integer.parseInt(st.nextToken());
        }
    }

    static int solve(int start, int end){
        int[][] dp = new int[n+1][3];
        dp[1][0] = start == 0 ? check[1][start] : 999999;
        dp[1][1] = start == 1 ? check[1][start] : 999999;
        dp[1][2] = start == 2 ? check[1][start] : 999999;
        for(int i = 2; i <= n; i++){
            dp[i][0] = Math.min(check[i][0] + dp[i-1][1], check[i][0] + dp[i-1][2]);
            dp[i][1] = Math.min(check[i][1] + dp[i-1][0], check[i][1] + dp[i-1][2]);
            dp[i][2] = Math.min(check[i][2] + dp[i-1][0], check[i][2] + dp[i-1][1]);
        }
        return dp[n][end];
    }
}
