import java.util.*;
import java.io.*;

public class Main {

    static int cnt = 0;
    static int N;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        visited = new boolean[N+1];
        for(int i=0; i<=N; i++){
            graph.add(new ArrayList<Integer>());
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        for(int i=1; i<=N; i++){
            Collections.sort(graph.get(i));
        }

        for(int i=0; i<N; i++){
            if(cnt == 0){
                findDepthFive(i, 1);
            }
        }

        System.out.println(cnt);

    }

    public static void findDepthFive(int node, int depth) {
        if(depth==5){
            cnt = 1;
            return;
        }

        for(int i=0; i<graph.get(node).size(); i++){
            int next = graph.get(node).get(i);
            visited[node] = true;
            if(!visited[next]) findDepthFive(next, depth+1);
            visited[node] = false;
        }
    }
}