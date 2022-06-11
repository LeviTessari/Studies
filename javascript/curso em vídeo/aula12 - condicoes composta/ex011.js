let idade = 68
console.log(`Você tem ${idade}. Seu voto é:`)
if (idade < 16){
    console.log('Não vota!')
}else if(idade <18 || idade > 65){
            console.log('Voto opcional!')
}else{
    console.log('Voto é obrigatório')
}

