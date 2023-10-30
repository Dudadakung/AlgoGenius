import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int seoksoon[] = new int[N/2];
        int jongyu[] = new int[N/2];

        for(int i=0; i<N/2; i++){
            seoksoon[i] = Integer.parseInt(br.readLine());
            jongyu[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(seoksoon);
        Arrays.sort(jongyu);

        int min = N;
        int cnt = 0;
        for(int i=0; i<M; i++){
            int num = binarySearch(0, N/2, i, seoksoon) + binarySearch(0, N/2, M-i+1, jongyu);
            if(min == num) {
                cnt++;
                continue;
            }
            if(min > num) {
                min = num;
                cnt=1;
            }
        }
        System.out.println(min + " " + cnt);
    }

    static int binarySearch(int start, int end, int h, int[] arr) {
        while(start<end){
            int mid = (start+end)/2;
            if(arr[mid]>=h){
                end=mid;
            }
            else{
                start=mid+1;
            }
        }
        return arr.length-end;
    }
}