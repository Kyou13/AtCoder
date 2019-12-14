// inputに入力データ全体が入る
function Main(input) {
  const args = input.split(' ')
  const a_1 = parseInt(args[0], 10)
  const a_2 = parseInt(args[1], 10)
  const a_3 = parseInt(args[2], 10)
  if(a_1+a_2+a_3 >= 22){
    console.log('bust')
  }else{
    console.log('win')
  }
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
