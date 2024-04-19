def escolher_dia_semana(numero_dia):
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }

    return dias_semana.get(numero_dia, "Dia inválido")

if __name__ == "__main__":
    numero_dia = int(input("Escolha o dia da semana (1 a 7): "))
    dia_semana = escolher_dia_semana(numero_dia)
    print("Você escolheu:", dia_semana)
