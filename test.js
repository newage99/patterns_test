/* Implementa una función que devuelva 
*  el número posible de patrones, empezando desde cualquier 
*  punto de la cuadrícula,
*  dada una longitud de patrón específica**.
*/

const count_patterns_from = (first_point, length) => {
    // al empezar lo primero que pense es en la estructura de la mecanica del patron entre filas y
    // columnas ya que el patron solo se une por lines rectas 
   const movementList = [{
       punto : "A",
       fila : 1,
       columna : 1,
       usado : false,
       posibilidad : 5
   },
    {
       punto : "B",
       fila : 1,
       columna : 2,
       usado : false,
       posibilidad : 7
   },
    {
       punto : "C",
       fila : 1,
       columna : 3,
       usado : false,
       posibilidad : 5
   },
    {
       punto : "D",
       fila : 2,
       columna : 1,
       usado : false,
       posibilidad :7
   },
    {
       punto : "E",
       fila : 2,
       columna : 2,
       usado : false,
       posibilidad : 8
   },
    {
       punto : "F",
       fila : 2,
       columna : 3,
       usado : false,
       posibilidad : 7
   },
    {
       punto : "G",
       fila : 3,
       columna : 1,
       usado : false,
       posibilidad : 5
   },
    {
       punto : "H",
       fila : 3,
       columna : 2,
       usado : false,
       posibilidad : 7
   },
    {
       punto : "I",
       fila : 3,
       columna : 3,
       usado : false,
       posibilidad : 5
   }]

   let acumulacion = 0
   //  console.log("llegamos")
   // ya hechos los objetos de la lista de movimientos hacer un for que cuente o prediga posibles patrones 
   for ( let i = 1; i < length; i++ ) { // viendo que length es la catidad de movimientos a realizar
       let primeraPrem = 0
       // console.log("llegamos dentro el primer for")
     switch (first_point) {
       case 'A':
           movementList[0].usado = true
           primeraPrem = 5
           break;
           case 'B':
               movementList[1].usado = true
               primeraPrem = 7
           break;
           case 'C':
               movementList[2].usado = true
               primeraPrem = 5
               // console.log("dentro del sw",primeraPrem )
           break;
           case 'D':
               movementList[3].usado = true
               primeraPrem = 7
           break;
           case 'E':
               movementList[4].usado = true
               primeraPrem = 8
           break;
           case 'F':
               movementList[5].usado = true
               primeraPrem = 7
           break;
           case 'G':
               movementList[6].usado = true
               primeraPrem = 5
           break;
           case 'H':
               movementList[7].usado = true
               primeraPrem = 7
           break;
           case 'I':
               movementList[8].usado = true
               primeraPrem = 5
           break;    
       default:
           break;
     }
//    console.log("estetette", acumulacion + primeraPrem )
     acumulacion = acumulacion + primeraPrem
     if ( length > 2){
  // de tener mas de dos posibles intentos de movimientos se abren las posibilidades 
         for (let e = 0; e < primeraPrem; e++) {
           let random;let max = 8
            function findRandom() {
            random = Math.floor(Math.random()* max)//Finds number between 0 - max
           //  console.log(random, "aleatorio")
            return random
         }
           // acumulando las posibilidades del segundo movimiento comienza a crecer exponencial mente a donde nos podriamos mover 
           // aumentado las posibilidades claro esta 
           acumulacion = movementList[findRandom()].posibilidad * movementList[findRandom()].posibilidad + acumulacion
           console.log("aproximado", acumulacion * length)
         }
     }
   }

return acumulacion
  
}



console.log(count_patterns_from("C", 4))