function escalar(){
    const players = document.getElementById('scale')
    const ul = document.createElement('ul')
    
    const titulo = document.createElement('h3')
    titulo.innerText = 'Jogador'
   players.append(titulo)

    const position = document.createElement('li')
    position.innerText = 'Posição do jogador: '
    const positionInput = document.createElement('input')
    positionInput.type = 'text'
    positionInput.name = 'posicao'
    positionInput.id = 'posicao'
    position.appendChild(positionInput)
    ul.appendChild(position)
    
    ul.appendChild(document.createElement('br'))

    const name = document.createElement('li')
    name.innerText= 'Nome do jogador: '
    const nameInput = document.createElement('input')
    nameInput.type = 'text'
    nameInput.name = 'name'
    nameInput.id = 'name'
    name.appendChild(nameInput)
    ul.appendChild(name)

    ul.appendChild(document.createElement('br'))

    const number = document.createElement('li')
    number.innerText = 'Número da camisa: '
    const numberInput = document.createElement('input')
    numberInput.type = 'text'
    numberInput.name = 'number'
    numberInput.id = 'number'
    number.appendChild(numberInput)
    ul.appendChild(number)    

    ul.appendChild(document.createElement('br'))

    players.append(ul)

}
function remover(){

    const players = document.getElementById('scale')

   const title = document.getElementsByTagName('h3')
   const player = document.getElementsByTagName('ul')

   players.removeChild(title[title.length-1])
   players.removeChild(player[player.length-1])
}