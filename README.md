# Patrones de desbloqueo de pantalla

Podrás ver como muchos smartphones usan el patrón geométrico como una medida de seguridad.
Para desbloquear el dispositivo, debes conectar una secuencia de puntos en una cuadrícula deslizando el dedo **sin levantar** mientras trazas el patrón en la pantalla.

La imagen inferior muestra un ejemplo de patrón de 7 puntos: (A -> B -> I -> E -> D -> G -> C).

![zmPNYdv](https://user-images.githubusercontent.com/95478521/148540311-11675ed1-3f77-4489-99e0-539ebb555930.png)

Implementa una función que devuelva **el número posible de patrones, empezando desde cualquier punto de la cuadrícula, dada una longitud de patrón específica**.

Más concretamente, para una función count_patterns_from(first_point, length), el parámetro 'first_point' es un carácter correspondiente al punto de la cuadrícula (ejemplo: 'A') donde el patrón empieza,
y el parámetro 'length' es un número entero que indica el número de puntos (longitud) que cada patrón debe tener.

Por ejemplo, count_patterns_from("C", 2), debería devolver el número de patrones posibles empezando desde el punto inicial 'C' que tengan 2 puntos de longitud. El valor devuelto en este caso sería 5, porque hay 5 patrones posibles:

(C -> B), (C -> D), (C -> E), (C -> F) and (C -> H).

Ten en cuenta que esta función debe devolver el **número** de patrones, **no los patrones en sí mismos**, así que solo debes contarlos.

## Reglas

1. En un patrón, los puntos **no se pueden repetir**: solo se deben usar una vez, como máximo.
2. En un patrón, dos puntos consecutivos solo se pueden conectar con **líneas rectas directas** de cualquiera de las siguientes maneras:
- **Horizontalmente**: Como (A -> B) en el ejemplo de la imagen.
- **Verticalmente**: Como (D -> G) en el ejemplo de la imagen.
- **Diagonalmente**: Como (I -> E), o (B -> I), en el ejemplo de la imagen.
3. **Pasando a través de un punto que ya ha sido usado**: como (G -> C) pasando a través de E, en el ejemplo de la imagen. Esta es la regla más complicada.
Normalmente, no deberías poder conectar G con C, porque E está entre ellas, pero como E ya ha sido usado como parte del patrón que estás trazando, puedes conectar G con C pasando a través de E, porque E es ignorada.

## Anécdota

Por curiosidad, el patrón de desbloqueo de la pantalla de bloqueo de Android debe tener una longitud de entre 4 y 9 puntos. Es decir, que hay 389112 posibles maneras en las que puedes bloquear tu dispositivo en Android.
