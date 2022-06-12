function oi(){
    oi.innerHTML = 'oi'
}
function carregar() {
    let msg = window.document.getElementById('msg')
    let paisagem = window.document.getElementById('imagem')
    let data = new Date()
    let hora = data.getHours()
    msg.innerHTML = `Agora são ${hora}.`

    if (hora > 0 && hora < 12){
        //bom dia!
        paisagem.src = 'manha.jpg'
    }else if (hora >= 12 && hora < 18){
        //boa tarde!
        paisagem.src = 'tarde.jpg'

    }else{
        //boa noite!
        paisagem.src = 'noite.jpg'
    }

}



