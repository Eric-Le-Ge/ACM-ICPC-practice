import java.util.*;
import java.io.*;
public class A2018RoundF {
  public static void main(String[] args) {
    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
    int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
    for (int i = 1; i <= t; ++i) {
      int l = in.nextInt();
      int res = 0;
      in.nextLine();
      char[] A = in.nextLine().toCharArray();
      char[] B = in.nextLine().toCharArray();

      Set<String> s = new HashSet();
      for (int j=0;j<l;j++){
        for (int k=j+1;k<=l;k++){
          char[] tmp = Arrays.copyOfRange(B, j, k);
          Arrays.sort(tmp);
          s.add(new String(tmp));
        }
      }
      //System.out.println(s);
      for (int j=0;j<l;j++){
        for (int k=j+1;k<=l;k++){
          char[] tmp = Arrays.copyOfRange(A, j, k);
          Arrays.sort(tmp);
          if (s.contains(new String(tmp))){
            res++;
          }
        }
      }
      System.out.println("Case #" + i + ": " + res);
    }
  }
}
