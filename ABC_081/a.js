// inputに入力データ全体が入る
function Main(input) {
  const args = input.split('')
  var count = 0
  args.forEach(s => {
    if(s == '1') count++
  })
  console.log(count)
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
