def concurso_cocina():
    rounds = [
    {
    'theme': 'Entrada',
    'scores': {
    'Valentina': {'judge_1': 8, 'judge_2': 7,
    'judge_3': 9},
    'Mateo':
    {'judge_1': 7, 'judge_2': 8,
    'judge_3': 7},
    'Camila':
    {'judge_1': 9, 'judge_2': 9,
    'judge_3': 8},
    'Santiago': {'judge_1': 6, 'judge_2': 7,
    'judge_3': 6},
    'Lucía':
    {'judge_1': 8, 'judge_2': 8,
    'judge_3': 8},
    }
    },
    {
    'theme': 'Plato principal',
    'scores': {
    'Valentina': {'judge_1': 9, 'judge_2': 9,
    'judge_3': 8},
    'Mateo':
    {'judge_1': 8, 'judge_2': 7,
    'judge_3': 9},
    'Camila':
    {'judge_1': 7, 'judge_2': 6,
    'judge_3': 7},
    'Santiago': {'judge_1': 9, 'judge_2': 8,
    'judge_3': 8},
    'Lucía':
    {'judge_1': 7, 'judge_2': 8,
    'judge_3': 7},
    }
    },
    {
    'theme': 'Postre','scores': {
    'Valentina': {'judge_1': 7, 'judge_2': 8,
    'judge_3': 7},
    'Mateo':
    {'judge_1': 9, 'judge_2': 9,
    'judge_3': 8},
    'Camila':
    {'judge_1': 8, 'judge_2': 7,
    'judge_3': 9},
    'Santiago': {'judge_1': 7, 'judge_2': 7,
    'judge_3': 6},
    'Lucía':
    {'judge_1': 9, 'judge_2': 9,
    'judge_3': 9},
    }
    },
    {
    'theme': 'Cocina internacional',
    'scores': {
    'Valentina': {'judge_1': 8, 'judge_2': 9,
    'judge_3': 9},
    'Mateo':
    {'judge_1': 7, 'judge_2': 6,
    'judge_3': 7},
    'Camila':
    {'judge_1': 9, 'judge_2': 8,
    'judge_3': 8},
    'Santiago': {'judge_1': 8, 'judge_2': 9,
    'judge_3': 7},
    'Lucía':
    {'judge_1': 7, 'judge_2': 7,
    'judge_3': 8},
    }
    },
    {
    'theme': 'Final libre',
    'scores': {
    'Valentina': {'judge_1': 9, 'judge_2': 8,
    'judge_3': 9},
    'Mateo':
    {'judge_1': 8, 'judge_2': 9,
    'judge_3': 8},
    'Camila':
    {'judge_1': 7, 'judge_2': 7,
    'judge_3': 7},
    'Santiago': {'judge_1': 9, 'judge_2': 9,
    'judge_3': 9},
    'Lucía':
    {'judge_1': 8, 'judge_2': 8,
    'judge_3': 7},
    }
    }
    ]

    ranking = {
        "Valentina" : {
            "puntos": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "promedio": 0
        },
        "Mateo" : {
            "puntos": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "promedio": 0
        },
        "Camila" : {
            "puntos": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "promedio": 0
        },
        "Santiago" : {
            "puntos": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "promedio": 0
        },
        "Lucía" : {
            "puntos": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "promedio": 0
        }
        }

    c_rondas = 0
    for ronda in rounds:

        ganador = None
        puntaje_mayor = -999
        c_rondas += 1

        for cocinero, puntajes in ronda["scores"].items():

            total_puntos = sum(puntajes.values())
            ranking[cocinero]["puntos"] += total_puntos

            if (total_puntos > ranking[cocinero]["mejor_ronda"]):
                ranking[cocinero]["mejor_ronda"] = total_puntos


            if (total_puntos > puntaje_mayor):
                ganador = cocinero
                puntaje_mayor = total_puntos

            ranking[cocinero]["promedio"] = ranking[cocinero]["puntos"] / c_rondas



        ranking[ganador]["rondas_ganadas"] += 1



        print(f"Ronda {c_rondas} - {ronda['theme']}")
        print(f"Ganador {ganador} ({puntaje_mayor})")

        for cocinero, puntos in ranking.items():
            print(f"{cocinero}:")
            print(f" - Total puntos {puntos['puntos']}")

            print(f" - Rondas ganadas {puntos['rondas_ganadas']}")

            print(f" - Mejor ronda {puntos['mejor_ronda']}")
            print(f" - Promedio {puntos['promedio']}")






