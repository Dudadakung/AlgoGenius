import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 접시의 수
        int d = Integer.parseInt(st.nextToken()); // 초밥의 가짓수
        int k = Integer.parseInt(st.nextToken()); // 연속해서 먹는 접시 수
        int c = Integer.parseInt(st.nextToken()); // 쿠폰 번호

        int sushi[] = new int[N]; // 초밥 벨트 배열
        int cnt = 0; // 초밥 종류 수
        int type[] = new int[d+1]; // 종류 별 개수
        int start = 0;
        int max = 0;

        for(int i=0; i<N; i++){
            sushi[i] = Integer.parseInt(br.readLine());
        }

        for(int i=0; i<k; i++){
            if(type[sushi[i]]==0) cnt++;
            type[sushi[i]]++;
        }

        while (start<=N) {
            if(type[sushi[start%N]]==1) cnt--;
            type[sushi[start%N]]--;

            if(type[sushi[(start+k)%N]]==0) cnt++;
            type[sushi[(start+k)%N]]++;

            if(type[c]==0) cnt++;

            start++;
            if(cnt>max) {
                max = cnt;
            }
            if(type[c]==0) cnt--;
        }
        System.out.println(max);
    }
}