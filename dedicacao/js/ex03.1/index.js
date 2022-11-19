let value = parseFloat(prompt("Digite o valor em metros"))
const unidade = prompt("Digite unidade")



switch(unidade){
    case "mm":
        alert(`O valor de ${value} m, convertendo é: ${value*1000} mm`)
        break
    case "cm":
        alert(`O valor de ${value} m, convertendo é: ${value*100} cm`)
        break
    case "dm":
        alert(`O valor de ${value} m, convertendo é: ${value/10} dm`)
        break
    case "km":
        alert(`O valor de ${value} m, convertendo é: ${value/1000} km`)
        break
    case "hm":
        alert(`O valor de ${value} m, convertendo é: ${value/100} hm`)
        break
   default:
        alert("Opção inválida")
        break
}