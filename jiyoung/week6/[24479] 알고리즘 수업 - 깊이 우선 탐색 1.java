import java.util.*;
import java.io.*;

public class algo {

    static int cnt;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static int[] checked; // 방문

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        checked = new int[n+1];
        for(int i=0; i<=n; i++){
            graph.add(new ArrayList<Integer>());
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph.get(u).add(v);
            graph.get(v).add(u); // 양방향이니까 둘 다 담아줌
        }

        for(int i=1; i<=n; i++){
            Collections.sort(graph.get(i)); // 정렬
        }

        cnt = 1; // 시작 정점도 순서에 포함
        dfs(r);

        for (int i = 1; i < checked.length; i++) {
			sb.append(checked[i]).append("\n");
		}
		System.out.println(sb);
    }

    private static void dfs(int node) {
        checked[node] = cnt;

        for(int i=0; i<graph.get(node).size(); i++){
            int nextNode = graph.get(node).get(i);
            if(checked[nextNode] == 0){
                cnt++;
                dfs(nextNode);
            }
        }
    }
}