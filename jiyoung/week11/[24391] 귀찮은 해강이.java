import java.io.*;
import java.util.*;

public class Main {

    static int[] lecture;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int cnt = 0;
        lecture = new int[N+1];
        for (int i=1; i<=N; i++) {
            lecture[i] = i;
        }

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        for (int i=1; i<N; i++) {
            int b = Integer.parseInt(st.nextToken());
            if(find(a) != find(b)) cnt++;
            a = b;
        }

        System.out.println(cnt);

    }

    public static void union(int a, int b){
        int ap = find(a);
        int bp = find(b);
        if(ap==bp) return;
        lecture[bp] = ap;
    }

    public static int find(int num){
        if(lecture[num]==num) return num;
        return lecture[num] = find(lecture[num]);
    }
}