import java.io.*;
import java.util.*;

public class Main {

    static int[] parents;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        parents = new int[N+1];
        for (int i=1; i<=N; i++) {
            parents[i] = i;
        }

        for (int i=0; i<N-2; i++) {
            st = new StringTokenizer(br.readLine());
            union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        for (int i=1; i<=N; i++) {
            if(find(i) == i)
                sb.append(i).append(' ');
        }

        System.out.println(sb);

    }

    public static void union(int a, int b){
        int ap = find(a);
        int bp = find(b);
        if(ap==bp) return;
        parents[bp] = ap;
    }

    public static int find(int num){
        if(parents[num]==num) return num;
        return parents[num] = find(parents[num]);
    }
}