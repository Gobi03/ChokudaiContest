import Primes._

object Main{
  val b = new scala.util.control.Breaks
  // b.breakable {
  //   while(true) {
  //     b.break
  //   }
  // }

  val base = 1441440
  def test(n: Int): Long = {
    val prime = primes(n + 3)
    var res = base.toLong
    while(res * prime <= 1e9.toLong)
      res *= prime
    return res
  }

  // 素因数分解したそれぞれの値の指数＋１の掛け算
  // def countPrimefactor(n: Int): Long = {
  //   var now = n
  //   var res: Long = 1
  //   b.breakable {
  //     for(e <- ar){
  //       if(now % e == 0){
  //         res *= now
  //       }
  //     }
  //   }
  // }


  def main (args: Array[String]){
    // println(primes.length)
    for(i <- 1 to 100){
      println(test(i))
    }
  }
}



