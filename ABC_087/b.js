// inputに入力データ全体が入る
function Main(input) {
  input = input.split('\n').map(n => parseInt(n, 10))
  var A = input[0]
  var B = input[1]
  var C = input[2]
  var X = input[3]
  var count = 0
  for(a=0;a<=A;a++){
    for(b=0;b<=B;b++){
      for(c=0;c<=C;c++){
        var sum = (a * 500) + (b * 100) + (c * 50)
        if(X == sum) count++
      }
    }
  }
  console.log(count)
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
