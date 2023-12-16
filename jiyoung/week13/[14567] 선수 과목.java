import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 과목의 수
        int M = Integer.parseInt(st.nextToken()); // 선수 조건의 수

        ArrayList<Integer> arr[] = new ArrayList[N + 1];
        int preSemiCnt[] = new int[N + 1]; // 선수과목 수
        Queue<Integer> que = new LinkedList<Integer>();

        for(int i=1; i<=N; i++){
            arr[i] = new ArrayList<Integer>();
        }

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            arr[start].add(end);
            preSemiCnt[end]++;
        }

        // 선수과목이 없는 과목들 추가
        for(int i=1; i<=N; i++){
            if(preSemiCnt[i]==0){
                que.add(i);
            }
        }

        int ans[] = new int[N + 1];
        int semi = 1;
        while(!que.isEmpty()) {
            int size = que.size();
            while(size-- != 0) {
                int now = que.poll();
                ans[now] = semi; // 이수
                for(int child : arr[now])
                    if(--preSemiCnt[child] == 0)
                        que.add(child);
            }
            semi++;
        }

        for(int i=1; i<=N; i++){
            System.out.print(ans[i]+" ");
        }

    }
}