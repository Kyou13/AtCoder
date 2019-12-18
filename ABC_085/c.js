// inputに入力データ全体が入る
function Main(input) {
  input = input.split(' ').map(n => parseInt(n, 10))
  var N = input[0]
  var Y = input[1]
  var result = '-1 -1 -1'
  outer: for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      k = N - i - j
      if (i * 10000 + j * 5000 + k * 1000 === Y) {
        result = `${i} ${j} ${k}`
        break outer
      }
    }
  }
  console.log(result)
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require('fs').readFileSync('/dev/stdin', 'utf8'))
