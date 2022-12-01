let mapa = {
  'A' : ['B', 'CB', 'D', 'E', 'F', 'GD', 'H', 'IE'],
  'B' : ['A', 'C', 'D', 'E', 'F', 'G', 'HE', 'I'],
  'C' : ['B', 'AB', 'D', 'E', 'F', 'GE', 'H', 'IF'],
  'D' : ['A', 'B', 'C', 'E', 'FE', 'G', 'H', 'I'],
  'E' : ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'],
  'F' : ['A', 'B', 'C', 'DE', 'E', 'G', 'H', 'I'],
  'G' : ['AD', 'B', 'CE', 'D', 'E', 'F', 'H', 'IH'],
  'H' : ['A', 'BE', 'C', 'D', 'E', 'F', 'G', 'I'],
  'I' : ['AE', 'B', 'CF', 'D', 'E', 'F', 'GH', 'H']
}
 

const posiblesPatrones = (punto, visitado) => {

  console.log(punto, visitado)
  return mapa[punto].reduce( (resultado, posicion) => {

      let [destino, sobre] = posicion.split("")

      if (visitado.indexOf(destino) === -1 &&
        (!sobre || visitado.indexOf(sobre) !== -1)) resultado.push(destino)

        return resultado
        
  }, [])
}

const patrones = (punto_inicio, longitud) => {
  
  let total = 0
  
  if (punto_inicio.length > longitud) return total
  if (punto_inicio.length === longitud) return total + 1
  
  let ultimoVisitado = punto_inicio.slice(-1)
  
  let posible = posiblesPatrones(ultimoVisitado, punto_inicio)
  
  if (punto_inicio.length + 1 === longitud) return posible.length
  
  for (nuevaPosicion of posible) {
    total += patrones(punto_inicio + nuevaPosicion, longitud)
  }

  return total
} 

patrones('C', 2)

