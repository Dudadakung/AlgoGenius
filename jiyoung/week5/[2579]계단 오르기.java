import java.util.*;
import java.io.*;

class Main {
  static int[] dp;
  static int[] arr;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());
    arr = new int[t+1];
    dp = new int[t+1];

    if(t==1){
      int n = Integer.parseInt(br.readLine());
      System.out.println(n);
      System.exit(0);
    }

    for(int i=1; i<t+1; i++){
      arr[i] = Integer.parseInt(br.readLine());
    }

    dp[1] = arr[1];
    dp[2] = dp[1] + arr[2];
    System.out.println(stareUp(t));
  }

  static int stareUp(int t){
    for(int i=3; i<t+1; i++){
      dp[i] = arr[i] + Math.max(dp[i-2], arr[i-1]+dp[i-3]);
    }
    return dp[t];
  }
}