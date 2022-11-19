let fila =["Vanessa", "Luana", "Roger"]
let stop = 0
do{
    let Fila = ""
    for(let i =0; i< fila.length; i++){
        Fila +=`${i+1}º `+ fila[i]+", "
    }
    let resp = parseFloat(prompt(`Pacientes na espera: ${Fila}.`+
    `\nQual opção você deseja?`+
    `\n1 - Novo paciente`+
    `\n2 - Consulta paciente`+
    `\n3 - Sair`))
    console.log(resp)
    switch(resp){
        case 1:
            let novo = prompt("Nome do paciente")
            fila.push(novo)
            break
        case 2:
            let nome = fila.shift()
            alert(`O paciente ${nome} será o próximo`)
            break
        case 3:
            stop = 1
            break
    }
}while( stop === 0)