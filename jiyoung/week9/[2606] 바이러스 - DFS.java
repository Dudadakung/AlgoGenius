import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static boolean arr[][];
    static boolean visited[];
    static int N, M;
    static int cnt;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        arr = new boolean[N+1][N+1];
        visited = new boolean[N+1];

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = true;
            arr[b][a] = true;
        }

        dfs(1);

        System.out.println(cnt);
    }

    public static void dfs(int n){
        visited[n] = true;

        for(int i=1; i<N+1; i++){
            if(arr[n][i] == true && visited[i] == false){
                cnt++;
                dfs(i);
            }
        }
    }
}