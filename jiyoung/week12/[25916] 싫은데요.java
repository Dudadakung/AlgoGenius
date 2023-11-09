import java.io.*;
import java.util.*;

public class Main {

    static int[] lecture;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int arr[] = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = 0;
        int sum = 0;
        int summary = arr[0];

        while(start<N){
            if(sum<=summary && summary<=M){
                sum = summary;
            }
            if(summary < M && end < N-1){
                end++;
                summary += arr[end];
                continue;
            }
            if(summary > M){
                summary -= arr[start];
                start++;
                continue;
            }
            else{
                break;
            }
        }

        System.out.println(sum);
    }
}