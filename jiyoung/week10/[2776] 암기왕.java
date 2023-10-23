import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        StringBuilder res = new StringBuilder();

        while(num>0){
            int N = Integer.parseInt(br.readLine());
            int book[] = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for(int i=0; i<N; i++){
                book[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(book);

            int M = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine(), " ");
            for(int i=0; i<M; i++){
                int findNum = Integer.parseInt(st.nextToken());
                boolean find = false;

                int start = 0;
                int end = book.length-1;

                while(start<=end){
                    int mid = (start + end) / 2;
                    int midValue = book[mid];

                    if(midValue > findNum){
                        end = mid-1;
                    }
                    else if(midValue < findNum){
                        start = mid+1;
                    }
                    else{
                        find = true;
                        break;
                    }
                }

                if(find) {
                    res.append("1\n");
                }
                else {
                    res.append("0\n");
                }
            }
            num--;
        }
        System.out.println(res);
    }
}