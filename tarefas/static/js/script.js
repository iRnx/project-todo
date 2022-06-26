var inputFiltro = document.querySelector('#search')

inputFiltro.addEventListener('input', function(){
    var array_cards = document.querySelectorAll('.card-array')

    if(this.value.length > 0){
        for(i = 0; i < array_cards.length; i++){
            var array_card = array_cards[i]
            var tituloH5 = array_card.querySelector('.titulo')
            var titulo = tituloH5.textContent
            var expressao = new RegExp(this.value, 'i')
            console.log(expressao)
            if(!expressao.test(titulo)){
                array_card.classList.add('invisivel')
            }else{
                array_card.classList.remove('invisivel')
            }
        }
    }else{
        for(i = 0; i < array_cards.length; i++){
            var array_card = array_cards[i]
            array_card.classList.remove('invisivel')
        }
    }
})
