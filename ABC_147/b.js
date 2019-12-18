// inputに入力データ全体が入る
function Main(input) {
	input = input.split('');
  var len_half = Math.floor(input.length/2)
  var count = 0
  for (var i = 0; i< len_half; i++){
    if(input[i] != input[input.length - i - 1]){
      count++
    }
  }
  console.log(count)
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
