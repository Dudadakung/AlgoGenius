import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int t = Integer.parseInt(br.readLine());

    while(t-->0){
      int k = Integer.parseInt(br.readLine());
      int[] files = new int[k+1]; // 파일 누적합
      int[][] dp = new int[k+1][k+1];

      st = new StringTokenizer(br.readLine(), " ");
      for(int i=1; i<k+1; i++){
        int temp = Integer.parseInt(st.nextToken());
        files[i] = temp + files[i-1];
      }

      for(int i=1; i<k; i++){ // 파일의 조각 길이
        for(int start=1; start+i<=k; start++){
          int end = start + i;
          dp[start][end] = Integer.MAX_VALUE;
          for(int m=start; m<end; m++){ // 파일을 나눌 지점
            dp[start][end] = Math.min(dp[start][end], dp[start][m]+dp[m+1][end]+files[end]-files[start-1]);
          }
        }
      }
      System.out.println(dp[1][k]);
    }
  }
}
