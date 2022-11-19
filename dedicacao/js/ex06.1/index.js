const number = parseFloat(prompt("Digite um numero"))
let tabuada =""
for(let i = 1; i <=20; i++){
   tabuada += number+" x "+i+" = "+ i*number+" \n "
}
alert(tabuada)