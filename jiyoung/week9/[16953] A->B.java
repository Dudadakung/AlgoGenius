import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static Queue<Long> q = new LinkedList<>();
    static long A, B;
    static int cnt;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());

        System.out.println(bfs());
    }

    public static int bfs(){
        q.offer(A);

        while(!q.isEmpty()){

            int size = q.size();
            for(int i=0; i<size; i++){
                long node = q.poll();

                if(node == B){
                    return cnt+1;
                }
                long n = node*2;
                long m = node*10+1;
                if(n<=B) q.offer(n);
                if(m<=B) q.offer(m);
            }
            cnt++;
        }
        return -1;
    }
}