grid = [
	['A','B','C'],
	['D','E','F'],
	['G','H','I'],
]

# funcion: char -> (int, int)
# convertir una letra a su representación en coordenadas. 
# ejemplo: 'C' -> (2,0)
def letter_to_coordinates(letter):
	if letter == 'A':
		return (0,0)
	elif letter == 'B':
		return (1,0)
	elif letter == 'C':
		return (2,0)
	elif letter == 'D':
		return (0,1)
	elif letter == 'E':
		return (1,1)
	elif letter == 'F':
		return (2,1)
	elif letter == 'G':
		return (0,2)
	elif letter == 'H':
		return (1,2)
	elif letter == 'I':
		return (2,2)


# funcion: (int, int) -> char
# convertir una letra a su representación en coordenadas. 
# ejemplo: (1,2) -> 'H'
def coordinates_to_letter(coordinates):
	if coordinates == (0,0):
		return 'A'
	elif coordinates == (1,0):
		return 'B'
	elif coordinates == (2,0):
		return 'C'
	elif coordinates == (0,1):
		return 'D'
	elif coordinates == (1,1):
		return 'E'
	elif coordinates == (2,1):
		return 'F'
	elif coordinates == (0,2):
		return 'G'
	elif coordinates == (1,2):
		return 'H'
	elif coordinates == (2,2):
		return 'I'


# funcion: char -> char -> bool
# verificar si dos puntos son un puente, es decir, si entre dos puntos hay un punto entre medio
# ejemplo: 'A' -> 'C' -> True
def is_bridge(pointA, pointB):
	if (letter_to_coordinates(pointB)[0] + 2, letter_to_coordinates(pointB)[1]) == letter_to_coordinates(pointA):
		return True
	if (letter_to_coordinates(pointB)[0] - 2, letter_to_coordinates(pointB)[1]) == letter_to_coordinates(pointA):
		return True
	if (letter_to_coordinates(pointB)[0], letter_to_coordinates(pointB)[1] + 2) == letter_to_coordinates(pointA):
		return True
	if (letter_to_coordinates(pointB)[0], letter_to_coordinates(pointB)[1] - 2) == letter_to_coordinates(pointA):
		return True
	if (letter_to_coordinates(pointB)[0] + 2, letter_to_coordinates(pointB)[1] + 2) == letter_to_coordinates(pointA):
		return True
	if (letter_to_coordinates(pointB)[0] - 2, letter_to_coordinates(pointB)[1] - 2) == letter_to_coordinates(pointA):
		return True
	if (letter_to_coordinates(pointB)[0] + 2, letter_to_coordinates(pointB)[1] - 2) == letter_to_coordinates(pointA):
		return True
	if (letter_to_coordinates(pointB)[0] - 2, letter_to_coordinates(pointB)[1] + 2) == letter_to_coordinates(pointA):
		return True

	return False


# funcion: char -> char -> (int, int)
# devolver el punto entre medio de otros dos puntos en forma de coordenadsa
# ejemplo: 'G' -> 'C' -> (1,1) ('E')
def between_point(pointA, pointB):
	if (letter_to_coordinates(pointB)[0] + 2, letter_to_coordinates(pointB)[1]) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0] + 1, letter_to_coordinates(pointB)[1])
	if (letter_to_coordinates(pointB)[0] - 2, letter_to_coordinates(pointB)[1]) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0] - 1, letter_to_coordinates(pointB)[1])
	if (letter_to_coordinates(pointB)[0], letter_to_coordinates(pointB)[1] + 2) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0], letter_to_coordinates(pointB)[1] + 1) 
	if (letter_to_coordinates(pointB)[0], letter_to_coordinates(pointB)[1] - 2) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0], letter_to_coordinates(pointB)[1] - 1)
	if (letter_to_coordinates(pointB)[0] + 2, letter_to_coordinates(pointB)[1] + 2) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0] + 1, letter_to_coordinates(pointB)[1] + 1)
	if (letter_to_coordinates(pointB)[0] - 2, letter_to_coordinates(pointB)[1] - 2) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0] - 1, letter_to_coordinates(pointB)[1] - 1)
	if (letter_to_coordinates(pointB)[0] + 2, letter_to_coordinates(pointB)[1] - 2) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0] + 1, letter_to_coordinates(pointB)[1] - 1)
	if (letter_to_coordinates(pointB)[0] - 2, letter_to_coordinates(pointB)[1] + 2) == letter_to_coordinates(pointA):
		return (letter_to_coordinates(pointB)[0] - 1, letter_to_coordinates(pointB)[1] + 1)

	return None


# funcion: char -> char -> [char] -> bool
# verificar si se puede conectar de un punto(A) a otro punto(B)
# ejemplo: 'A' -> 'B' -> ['D','E','A'] -> True
def can_connect(pointA, pointB, connected_points):
	for point in connected_points:
		if point == pointB:
			return False

	if is_bridge(pointA,pointB):
		for point in connected_points:
			if point == coordinates_to_letter(between_point(pointA,pointB)):
				return True
		return False

	return True

# funcion: char -> [char] -> [char]
# devolver las posibles conexiones
# ejemplo: 'A' -> ['A','B','C'] -> ['D', 'E', 'F', 'H']
def count_connections(start_point, connected_points):
	connections = []

	for row in grid:
		for point in row:
			if can_connect(start_point, point, connected_points):
				connections.append(point)

	return connections


# funcion: char -> [char] -> int -> int -> int
# devolver el número posible de patrones de una determinada longitud
# ejemplo: 'C' -> [] -> 2 -> 0 -> 5 
def count_connections_forward(start_point, connected_points, length, total_count):
	connected_points_tmp = connected_points.copy()
	connected_points_tmp.append(start_point)
	connections_count = len(connected_points_tmp)
	possible_connections = count_connections(start_point, connected_points_tmp)

	if possible_connections == [] or connections_count >= length:
		#print(connected_points_tmp)
		return total_count + 1
	else:
		for con in possible_connections:
			total_count = count_connections_forward(con, connected_points_tmp, length, total_count)

	return total_count

 
# funcion: char -> int -> int
# devolver el número posible de patrones de una determinada longitud
# ejemplo: 'C' -> 2 -> 5
def count_patterns_from(first_point, length):
	return count_connections_forward(first_point, [], length, 0)


# posibles maneras en las que puedes bloquear tu dispositivo en Android
'''
total_possible_android = 0
for x in range(4,10):
	for row in grid:
		for letter in row:
			total_possible_android += count_patterns_from(letter,x)

print(total_possible_android)
'''


print(count_patterns_from('C', 4))