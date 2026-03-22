text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
def estadisticas_texto():
	c1 = len(text.split('\n'))
	print(f'cantidad total de lineas {c1}')

	c2 = len(text.split())

	print(f"cant de palabras {c2}")


	lineas = text.split('\n')

	suma = 0

	for linea in lineas:
		suma += len(linea.split(' '))

	prom = suma/c1
	print(f"el promedio de palabras por linea es {prom}")

	total = 0
	for linea in lineas:
		if len(linea.split(' ')) > prom:
			total += 1
	print(f"el total de lineas con mas palabras que el promedio es {total}")


	lista_lineas_largas = [linea for linea in lineas if len(linea.split()) > prom]

	print(lista_lineas_largas)
	print(len(lista_lineas_largas))
