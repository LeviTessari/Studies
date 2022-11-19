function triangulo(base, altura){
    return (base*altura)/2
}
function retangulo(base, altura){
    return base*altura
}
function quadrado(lado){
    return lado*lado
}
function trapezio(baseMenor, baseMaior, altura){
    return (baseMenor+baseMaior)*altura/2
}
function circulo(raio){
    return raio*raio*3.14
}
function msg(){
    alert("A área escolhida vale: "+area)
}

let stop = 0
let area
do{
    let resp = parseFloat(prompt("Vams cálcular as áreas das figuras. \nQual área você deseja calcular?"+
    "\n1 - Triângulo\n2 - Retângulo\n3 - Quadrado\n4 - Trapézio\n5 - Círculo\n6 - Sair"))
    switch(resp){
        case 1:
            area = triangulo(parseFloat(prompt("Digite o valor da base")) , parseFloat(prompt("Digite valor da altura")))
            msg()
            break
        case 2:
            area = retangulo(parseFloat(prompt("Digite o valor da base")), parseFloat(prompt("Digite valor da altura")))
            msg()
            break
        case 3:
             area = quadrado(parseFloat(prompt("Digite valor do lado")))
             msg()
             break
        case 4:
            area = trapezio(parseFloat(prompt("Digite valor da base menor")),parseFloat(prompt("Digite valor da base maior")),parseFloat(prompt("Digite valor da altura")))
            msg()
            break
        case 5:
            area = circulo(parseFloat(prompt("Digite valor do raio")))
            msg()
            break
        case 6:
            stop = 1
            alert("Finalizando...")
            break
        default:
            alert("Comando inválido")
            break
    }   
    
}while(stop === 0)