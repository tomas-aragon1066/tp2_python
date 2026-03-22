
def duracion_playlist():
	
	playlist = [
	{"title": "Bohemian Rhapsody", "duration": "5:55"},
	{"title": "Hotel California", "duration": "6:30"},
	{"title": "Stairway to Heaven", "duration": "8:02"},
	{"title": "Imagine", "duration": "3:07"},
	{"title": "Smells Like Teen Spirit", "duration": "5:01"},
	{"title": "Billie Jean", "duration": "4:54"},
	{"title": "Hey Jude", "duration": "7:11"},
	{"title": "Like a Rolling Stone", "duration": "6:13"},
	]



	minutos = 0
	seg = 0

	for item in playlist:
		minutos += int(item["duration"].split(":")[0])
		seg += int(item["duration"].split(":")[1])



	minutos += seg // 60

	seg = seg % 60

	print(f"Duracion total: {minutos}m {seg}s")

	mas_larga = ""
	mas_corta = ""


	duracion = []

	maximo = -1
	minimo = 999

	total_seg = 0

	for item in playlist:
		duracion  = item["duration"].split(":")
		total_seg = int(duracion[0]) * 60 + int(duracion[1])

		if total_seg > maximo:
			mas_larga = item["title"]
			maximo = total_seg

		if total_seg < minimo:
			mas_corta = item["title"]
			minimo = total_seg

	print(f"cancion mas corta {mas_corta}")
	print(f"cancion mas larga {mas_larga}")
