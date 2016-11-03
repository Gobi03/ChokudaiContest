import java.util.Scanner

object MakeArray {
  def main (args: Array[String]){
    val sc = new Scanner(System.in)

    print("Array(")
    for(i <- 1 to 3400){
      val tmp = sc.nextInt()
      print(tmp + ", ")
    }

    val tmp = sc.nextInt()
    println(tmp + ")")
  }
}
