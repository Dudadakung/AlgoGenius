import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader bf;
    static int n, m;
    static boolean check;
    static ArrayList<ArrayList<Integer>> map = new ArrayList<>();
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) map.add(new ArrayList<Integer>());
        inputMap();
        for (int i = 0; i < n; i++) {
            if (check) break;
            visited = new boolean[n];
            backtracking(0, i);
        }
        if (check) System.out.println('1');
        System.out.println('0');
    }

    static public void inputMap() throws IOException {
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map.get(a).add(b);
            map.get(b).add(a);
        }
    }

    static public void backtracking(int currentDepth, int current) {
        if (currentDepth == 4) check = true;
        if (check) return;
        for (int i = 0; i < map.get(current).size(); i++) {
            int next = map.get(current).get(i);
            if(visited[next]) continue;
            visited[current] = true;
            backtracking(currentDepth + 1, next);
            visited[current] = false;
        }
    }
}
