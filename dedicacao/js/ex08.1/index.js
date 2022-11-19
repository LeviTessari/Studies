let imoveis = []
let stop = 0
let mostraImoveis = []
do{
    let resp=parseFloat(prompt("Bem vindo ao cadastro de imóveis"+"\nNo momento temos: "+imoveis.length+" imóveis cadastrados."+"\nO que deseja fazer?"+"\n1 - Cadastrar imóveis \n2 - Ver todos os imóveis \n3 - Sair"))

 switch(resp){
    case 1:
            let colocando = {
            name: prompt("Digite nome do proprietário"),
            bedroom: prompt("Digite a quantidade de quartos"),
            restroom: prompt("Digite a quantidade de banheiros"),
            garage: confirm("Possui garagem?")
        }
        imoveis.push(colocando)
        break
    case 2:
        if( imoveis.length === 0){
            alert("Não possui imóveis cadastrados")
        }else{
            for(i=0; i< imoveis.length; i++){
                mostraImoveis +="Nome: "+ imoveis[i].name+", Quarto: "+ imoveis[i].bedroom+", Banheiros: "+imoveis[i].restroom+", Possui garagem: "+imoveis[i].garage+". \n"
            }
            alert(mostraImoveis)
            console.log(mostraImoveis)
        }
        break
    case 3:
        stop = 1
        break
    default:
        alert("Comando inválido")
        break
    
 }

}while( stop === 0)