let stop = 0
        
do{
     
     let opt = parseFloat(prompt("Escolha uma opção de 1 à 4"+"\nA opção 5 é de finalizar o programa."))
    
     switch(opt){
         case 1:
             alert("Opção 1")
             break
         case 2:
             alert("Opção 2")
             break
         case 3:
             alert("Opção 3")
             break
         case 4:
             alert("Opção 4")
             break
         case 5:
             stop = 1
             alert("O programa está sendo finalizado...")
             break
     }     
 }while(stop === 0) 