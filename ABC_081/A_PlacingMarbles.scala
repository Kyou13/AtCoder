object A_Product{
  def main(args: Array[String]): Unit = {
    val strAry = io.StdIn.readLine()
    println(solve(strAry))
    
  }
  def solve(input: String): Int =
    input.split("").map(_.toInt).filter(_==1).size
}
