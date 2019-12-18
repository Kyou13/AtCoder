// inputに入力データ全体が入る
function Main(input) {
  input = input.split(' ').map(n => parseInt(n, 10))
  var N = input[0]
  var A = input[1]
  var B = input[2]
  var ans = 0
  for(n=1;n<=N;n++){
    var sum = 0
    var tmp = n
    while(tmp>0){
      sum += tmp % 10
      tmp = Math.floor(tmp / 10)
    }
    if(sum >= A && sum <= B) {ans = ans + n}
  }
  console.log(ans)
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main('20 2 5')
// Main(require("fs").readFileSync("/dev/stdin", "utf8"));
