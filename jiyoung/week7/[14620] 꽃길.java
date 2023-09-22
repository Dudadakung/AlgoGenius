import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int[][] garden = new int[N][N];
        int[][] visited = new int[N][N];
        int cost = 0;

        int min = Integer.MAX_VALUE;

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<N; j++){
                garden[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=1; i<N-1; i++){
            for(int j=1; j<N-1; j++){
                for(int e=0; e<N; e++){
                    for(int f=0; f<N; f++){
                        visited[e][f] = 0;
                    }
                }

                visited[i][j] = 1;
                visited[i-1][j] = 1;
                visited[i+1][j] = 1;
                visited[i][j-1] = 1;
                visited[i][j+1] = 1;

                for(int a=1; a<N-1; a++){
                    for(int b=1; b<N-1; b++){

                        if(visited[a][b]==1 || visited[a-1][b]==1 || visited[a+1][b]==1 || visited[a][b-1]==1|| visited[a][b+1]==1){
                            continue;
                        }
                        visited[a][b] = 1;
                        visited[a-1][b] = 1;
                        visited[a+1][b] = 1;
                        visited[a][b-1] = 1;
                        visited[a][b+1] = 1;

                        for(int c=1; c<N-1; c++){
                            for(int d=1; d<N-1; d++){
                                if(visited[c][d]==1 || visited[c-1][d]==1 || visited[c+1][d]==1 || visited[c][d-1]==1|| visited[c][d+1]==1){
                                    continue;
                                }

                                cost = garden[i][j] + garden[i-1][j] + garden[i+1][j] + garden[i][j-1] + garden[i][j+1];
                                cost += garden[a][b] + garden[a-1][b] + garden[a+1][b] + garden[a][b-1] + garden[a][b+1];
                                cost += garden[c][d] + garden[c-1][d] + garden[c+1][d] + garden[c][d-1] + garden[c][d+1];

                                if(cost<min){
                                    min = cost;
                                }
                            }
                        }
                        visited[a][b] = 0;
                        visited[a-1][b] = 0;
                        visited[a+1][b] = 0;
                        visited[a][b-1] = 0;
                        visited[a][b+1] = 0;
                    }
                }
            }
        }
        System.out.println(min);
    }
}