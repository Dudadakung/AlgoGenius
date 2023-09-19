import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf;
    static int n, m, r, cnt;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
    static int[] visit;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        visit = new int[n+1];
        for (int i = 0; i <= n; i++) {
            adjList.add(new ArrayList<Integer>());
            visit[i] = -1;
        }
        input();
        for (int i = 1; i <= n; i++) {
            Collections.sort(adjList.get(i));
        }
        visit[r] = 0;
        bfs(r);
        for (int i = 1; i < visit.length; i++) {
            sb.append(visit[i]).append("\n");
        }
        System.out.println(sb);
    }
    static void input() throws IOException {
        for (int i = 1; i <= m; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            adjList.get(start).add(end);
            adjList.get(end).add(start);
        }
    }

    static void bfs(int start){
        for (int i = 0; i < adjList.get(start).size(); i++){
            int value = adjList.get(start).get(i);
            if(visit[adjList.get(start).get(i)] == -1){
                visit[adjList.get(start).get(i)] = visit[start] + 1;
                bfs(value);
            }
        }
    }

}
