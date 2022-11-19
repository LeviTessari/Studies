const nome = prompt("Digite seu nome")
        let velocidade1 = parseFloat(prompt("Digite a velocidade do primeiro veiculo"))
        let velocidade2 = parseFloat(prompt("Digite a velocidade do segundo veiculo"))

        const resltado = (velocidade1 > velocidade2) ? alert("O carro 1 possui maior velocidade") : (velocidade2 > velocidade1)? alert("Carro 2 possui maior velocidade") : alert("Possuem mesma velocidade")