import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int E = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int e = 0;
        int s = 0;
        int m = 0;

        int cnt = 0;

        while(true){
            e++;
            s++;
            m++;
            if(e>15) e=e-15;
            if(s>28) s=s-28;
            if(m>19) m=m-19;
            cnt++;
            if(e==E && s==S && m==M){
                break;
            }
        }
        System.out.println(cnt);
    }
}