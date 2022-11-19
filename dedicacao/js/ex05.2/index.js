const initial = parseFloat(prompt("Quantidade inicial de dinheiro dispoível"))
let valueCurrent = initial
let stop = 0
do{
let opt = prompt("Você possui: "+valueCurrent+".\nDeseja adicionar, remover ou sair?")
switch(opt){
    case "adicionar":
        let add = parseFloat(prompt("Qual a quantidade que deseja adicionar"))
        valueCurrent += add
        break
    case "remover":
        let remove = parseFloat(prompt("Qual a quantidade que deseja remover"))
        valueCurrent -= remove
        break
    case "sair":
        stop = 1
        alert("Programa está sendo finalizado")
}

}while( stop === 0)