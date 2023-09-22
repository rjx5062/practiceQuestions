import java.util.*;

public class Foobar {

   private Map<String, Integer> map;

   public Foobar() {
      map = new HashMap<>();
      map.put("foo", 1);
      map.put("bar", 3);
   }

   public int getValue(String input, int numRetries) throws Exception {

      System.out.println("getValue function being executed...");

      try {
         return map.get(input);
      } catch (Exception e) {
         if (numRetries > 3) {
            throw e;
         }
         return getValue(input, numRetries + 1);
      }
   }

   public static void main(String[] args) {
      System.out.println("Hello, World!");
      var inst = new Foobar();
      try {
         System.out.println(inst.getValue("fubar", 0));
      } catch (Exception E) {
         System.out.println("Caught the exception");
      }
      // getValue("bar", 2);
      // getValue("baz", 0);
      // getValue("fubar", 1);
   }
}