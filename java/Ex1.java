// Source code is decompiled from a .class file using FernFlower decompiler (from Intellij IDEA).
public class Ex1 {
   public Ex1() {
   }

   public static void main(String[] var0) {
      int[] var1 = new int[]{10, 25, 3, 42, 18};
      int var2 = var1[0];
      int var3 = var1[0];
      int var4 = 0;

      for(int var8 : var1) {
         if (var8 > var2) {
            var2 = var8;
         }

         if (var8 < var3) {
            var3 = var8;
         }

         var4 += var8;
      }

      System.out.println("Largest: " + var2);
      System.out.println("Smallest: " + var3);
      System.out.println("Sum: " + var4);
   }
}
