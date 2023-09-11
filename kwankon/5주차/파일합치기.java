import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf;
    static int n;
    static int s;
    static int[] input;
    static int[][] check;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());
        for (int i = 0; i < n; i++) {
            s = Integer.parseInt(bf.readLine());
            input = new int[s];
            check = new int[s][s];
            saveNumberList();
            solve();
        }
        System.out.println(sb);
    }

    static void saveNumberList() throws IOException {
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        for (int i = 0; i < s; i++) {
            if (i == 0) {
                input[i] = Integer.parseInt(st.nextToken());
            } else {
                input[i] = input[i - 1] + Integer.parseInt(st.nextToken());
            }
            check[i][i] = input[i];
        }
    }

    static void solve() {
        for (int i = 1; i < s; i++) {
            for (int start = 0; start + i < s; start++) {
                int end = start + i;
                int temp = 0;
                if (start == 0) temp = input[end];
                else temp = input[end] - input[start - 1];
                check[start][end] = Integer.MAX_VALUE;
                for (int mid = start; mid < end; mid++) {
                    int left = start == mid ? 0 : check[start][mid];
                    int right = mid+1 == end ? 0 : check[mid+1][end];
                    check[start][end] = Math.min(check[start][end], temp + left + right);
                }
            }
        }
        sb.append(check[0][s-1]);
        sb.append('\n');
    }
}
