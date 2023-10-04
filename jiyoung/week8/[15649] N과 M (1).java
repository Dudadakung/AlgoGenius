import java.util.*;
import java.io.*;

public class Main {

    static int N;
    static int M;
    static Boolean[] visited;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new Boolean[N+1];
        arr = new int[N+1];
        Arrays.fill(visited, false);

        findAllSeq(0);

        System.out.println(sb);
    }

    public static void findAllSeq(int index){
        if(index == M){
            for(int i=0; i<M; i++){
                sb.append(arr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for(int i=1; i<N+1; i++){
            if(visited[i]) continue;
            visited[i] = true;
            arr[index] = i;
            findAllSeq(index+1);
            visited[i] = false;
        }
    }
}