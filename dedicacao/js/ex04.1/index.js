const name = prompt("Digite seu nome")
let resposta = prompt("Você já visitou alguma cidade?")
let contador = 0
let visitou = ""
while(resposta ==="sim"){
    contador += 1
    let cidade = prompt("Nome da cidade visitada")
    visitou += ", "+cidade
    resposta = prompt("Você visitou alguma outra cidade?")
    }
alert(`${name}, você visitou ${contador} cidades. Elas são: ${visitou}`)