const word = prompt("Verificação de palíndromos"+"\n"+"Digite uma palavra para verificação")
let wordInvert = ""
for(let i =0; i < word.length; i++){
     wordInvert += word[word.length-1-i]    
}
if( word === wordInvert){
    alert(`A palavra ${word} é um palíndromo!`)
}else{
    alert(`A palavra ${word} não é um palíndromo!`)
}