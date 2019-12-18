// inputに入力データ全体が入る
function Main(input) {
  var A = input.split('\n')[1].split(' ').map(n => parseInt(n, 10))
  var count = 0
  while(A.every(a => (a % 2) == 0)){
    count++
    A = A.map(a => a / 2)
  }
  console.log(count)
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
