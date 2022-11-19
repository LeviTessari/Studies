let baralho = []
let stop=0
do{
    let resp = prompt(`Cartas no baralho ${baralho.length}.`+`\n1 - Adicione uma carta`+`\n2 - Puxar uma carta`+`\n3- Sair`)
    switch(resp){
        case 1:
            let card = prompt("Qual carta será adicionada?")
            baralho.unshift(card)
            break
        case 2:
            alert(`A carta puxada é a ${baralho[baralho.length-1]}`)
            baralho.pop()
            break
        case 3:
            stop = 1
    }
}while(stop === 0)