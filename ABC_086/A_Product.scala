object A_Product{
  def main(args: Array[String]) =
    println(solve(args))
  def solve(input: Array[String]): String =
    if((input(0).toInt*input(1).toInt)%2==0){"Even"}else{"Odd"}
}
