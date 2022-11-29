let stop = 0
let vagas = []


do {
    let resp = parseFloat(prompt("-- Sistema de vagas de emprego --" +
        "\nDigite a opção que você deseja acessar:"+
        "\n1 - Listar vagas disponiveis\n2 - Criar uma nova vaga\n3 - Visualizar uma vaga\n4 - Inscrever um candidato em uma vaga\n5 - Excluir uma vaga\n6 - Sair"))
    switch (resp) {
        case 1:
            //listar vagas disponiveis
            if (vagas.length == 0){
                alert("Não existe vaga disponivel no momento.")
            }else{
                const Vagas = vagas.reduce(function(final, vaga, ind){
                    final += ind + ", "
                    final += vaga.name
                    final += " | " + vaga.candidatos.length + " candidatos \n"
                    return final
                }, "")
                alert(Vagas)
            }
            break
        case 2:
            // criar uma nova vaga
            let vaga = {
                name: prompt("Digite o nome da vaga que será oferecida"),
                description: prompt("Digite a descrição da vaga"),
                dataLimit: prompt("Digite o prazo limite da vaga"),
                candidatos:[]
            }
           
            let conf = confirm("Deseja confirmar as informações salvas?")
            if (conf === true){
                vagas.push(vaga)
            }
            break
        case 3:
            if (vagas.length == 0){
                alert("Não existe vaga disponivel no momento.")
            }else{
                let indice = prompt("Digite o índice da vaga")
                if(indice < vagas.length){
                alert("O índice da vaga digitado foi: "+indice+
                "\nNome da vaga: "+vagas[indice].name+
                "\nDescrição da vaga: "+vagas[indice].description+
                "\nData limite: "+vagas[indice].dataLimit+
                "\nA quantidade de candidatos: "+vagas[indice].candidatos.length+
                "\nOs candidatos são: "+vagas[indice].candidatos
                )}else{alert("Vaga não existe")}
            }
            break    
        
        case 4:
            if (vagas.length == 0){
                alert("Não existe vaga disponivel no momento.")
            }else{
                let nome = prompt("Digite seu nome")
                let indice = parseFloat(prompt("Digite o índice da vaga"))
                let conf2 = confirm("Deseja confirmar as informações salvas?"+
                "\nVaga: "+ vagas[indice])
                if (conf2 === true){
                    vagas[indice].candidatos.push(nome)
                }
            }
           
            break
        case 5:
            // excluir uma vaga
            let i = parseFloat(prompt("Qual índice da vaga para remover?"))
            let conf3 = confirm("Deseja remover o curso: "+vagas[i])
            if (conf3 === true){
                vagas.slice(i,1)
            }
            break
        case 6:
            stop = 1
            break
    }
} while (stop === 0)