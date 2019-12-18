function Main(input) {
  const args = input.split('\n')
  const N = parseInt(args[0], 10)
  const a = args[1].split(' ').map(n => parseInt(n, 10))
  const compareFunc = (a, b) => {
    return b - a
  }
  // 解放1
  // a = a.sort(compareFunc)
  // var sumA = a
  // .filter((value, index) => index % 2 == 0)
  // .reduce((prev, current) => prev + current)
  // var sumB = a
  // .filter((value, index) => index % 2 == 1)
  // .reduce((prev, current) => prev + current)
  // 解放2
  var sumA = 0,
    sumB = 0
  a.sort(compareFunc).forEach((value, index) => {
    index % 2 == 0 ? (sumA += value) : (sumB += value)
  })

  console.log(sumA - sumB)
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require('fs').readFileSync('/dev/stdin', 'utf8'))
