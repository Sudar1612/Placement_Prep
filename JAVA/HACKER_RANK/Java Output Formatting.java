import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int ind=0;ind<3;ind++){
            String word=sc.next();
            int num=sc.nextInt();
            System.out.printf("%-15s",word);
            System.out.printf("%03d%n",num);
        }
        System.out.println("================================");
    }
}
