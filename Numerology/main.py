def main_menu() -> int:
    option = 0
    option = int(input(
        "Choose an option: \n1. Basic\n2. Name\n3. Complete\n4. Couples\n5. Exit\n"))

    return option


def basic() -> None:
    #* Array of the date
    date = []

    #* Append each item
    date = [int(item) for item in input("Fecha completa : ").split()]
    # print(date)

    #* Formulas and reductions
    day = str(date[0]) + str(date[1])
    day_red = sum_digits(day)

    month = str(date[2]) + str(date[3])
    month_red = sum_digits(month)

    two_year = str(date[6]) + str(date[7])
    two_year_red = sum_digits(two_year)

    year = str(date[4]) + str(date[5]) + str(date[6]) + str(date[7])
    year_red = sum_digits(year)

    proposito = karmas(sum(date))[0]
    proposito_red = sum_digits(proposito)

    destino = sum_digits(day)[-1] + sum_digits(month)[-1] + sum_digits(year)[-1]
    destino_red = sum_digits(destino)

    #* Pinnacles

    etapa1 = sum_digits(month_red[-1] + day_red[-1])
    etapa2 = sum_digits(day_red[-1] + year_red[-1])
    etapa3 = sum_digits(etapa1[-1] + etapa2[-1])
    etapa4 = sum_digits(month_red[-1] + year_red[-1])

    desafio1 = sum_digits(abs((month_red[-1] - day_red[-1])))
    desafio2 = sum_digits(abs((day_red[-1] - year_red[-1])))
    desafio3 = sum_digits(abs((desafio1[-1] - desafio2[-1])))
    desafio4 = sum_digits(abs((month_red[-1] - year_red[-1])))

    sombra1 = sum_digits(desafio1[-1] + desafio2[-1] + desafio3[-1])
    sombra2 = sum_digits(destino_red[-1] + sombra1[-1])

    #* Prints

    print(f"Alma: {day} / {day_red[-1]}")
    print(f"Ego: {month} / {month_red[-1]}")
    print(f"Don: {two_year} / {two_year_red[-1]}")
    print(f"Vidas Pasadas: {year} / {year_red[-1]}")
    print(f"Proposito: {proposito} / {proposito_red[-1]}")
    print(f"Destino: {destino} / {destino_red[-1]}")

    print("-------------------------------------------------------------------------------\nComprobar pinaculo")
    print(f"Month: {month_red}, Day: {day_red}, Year: {year_red}")


    print(f"Etapa1: {etapa1} --> Etapa2: {etapa2} --> Etapa3: {etapa3} --> Etapa4: {etapa4}")
    print(f"Desafio1: {desafio1} --> Desafio2: {desafio2} --> Desafio3: {desafio3} --> Desafio4: {desafio4}")

    print("-------------------------------------------------------------------------------")

    print(f"Sombra1: {sombra1}\nSombra2: {sombra2}\nRelacion Espejo: {sum_digits(destino_red[-1] + etapa4[-1])}")

    print("-------------------------------------------------------------------------------")

    print(f"Coronilla: {etapa4}\n3er Ojo: {etapa3}\nGarganta: {sum_digits((etapa1[-1] + etapa2[-1]))}\nCorazon: {destino_red}\nPlexo: {sum_digits(desafio1[-1] +(desafio2[-1]))}\nSacro: {desafio3}\nRaiz: {desafio4}")

    print("-------------------------------------------------------------------------------")

    print(f"Etapa1: 0 a {36 - destino_red[-1]} -- Etapa2: {36 - destino_red[-1]} a {36 - destino_red[-1] + 9} -- Etapa3: {36 - destino_red[-1] + 9} a {36 - destino_red[-1] + 18} -- Etapa4: {36 - destino_red[-1] + 18} a {36 - destino_red[-1] + 27}")

    return date


def parejas() -> list:

    date = []

    date = [int(item) for item in input("Fecha completa de la primer persona: ").split()]
    # print(date)

    day = str(date[0]) + str(date[1])
    day_red = sum_digits(day)

    month = str(date[2]) + str(date[3])
    month_red = sum_digits(month)

    two_year = str(date[6]) + str(date[7])
    two_year_red = sum_digits(two_year)

    year = str(date[4]) + str(date[5]) + str(date[6]) + str(date[7])
    year_red = sum_digits(year)

    proposito = karmas(sum(date))[0]
    proposito_red = sum_digits(proposito)

    destino = sum_digits(day)[-1] + sum_digits(month)[-1] + sum_digits(year)[-1]
    destino_red = sum_digits(destino)

    date1 = []

    date1 = [int(item1) for item1 in input(
        "Fecha completa de la segunda persona: ").split()]
    # print(date)

    day1 = str(date1[0]) + str(date1[1])
    day_red1 = sum_digits(day1)

    month1 = str(date1[2]) + str(date1[3])
    month_red1 = sum_digits(month1)

    two_year1 = str(date1[6]) + str(date1[7])
    two_year_red1 = sum_digits(two_year1)

    year1 = str(date1[4]) + str(date1[5]) + str(date1[6]) + str(date1[7])
    year_red1 = sum_digits(year1)

    proposito1 = karmas(sum(date1))[0]
    proposito_red1 = sum_digits(proposito1)

    destino1 = sum_digits(day1)[-1] +  sum_digits(month1)[-1] + sum_digits(year1)[-1]
    destino_red1 = sum_digits(destino1)

    print(f"Alma: {day} / {day_red[-1]} -- {day1} / {day_red1[-1]} --> {day_red[-1] + day_red1[-1]}")
    print(f"Ego: {month} / {month_red[-1]} -- {month1} / {month_red1[-1]} --> {month_red[-1] + month_red1[-1]}")
    print(f"Don: {two_year} / {two_year_red[-1]} -- {two_year1} / {two_year_red1[-1]} --> {two_year_red[-1] + two_year_red1[-1]}")
    print(f"Vidas Pasadas: {year} / {year_red[-1]} -- {year1} / {year_red1[-1]} --> {year_red[-1] + year_red1[-1]}")
    print(f"Proposito: {proposito} / {proposito_red[-1]} -- {proposito1} / {proposito_red1[-1]} --> {proposito_red[-1] + proposito_red1[-1]}")
    print(f"Destino: {destino} / {destino_red[-1]} -- {destino1} / {destino_red1[-1]} --> {destino_red[-1] + destino_red1[-1]}\n\n")


def name() -> None:
    # Define the mapping from letters to numbers
    letter_to_number = {
        "a": 1,
        "j": 1,
        "s": 1,
        "b": 2,
        "k": 2,
        "t": 2,
        "c": 3,
        "l": 3,
        "u": 3,
        "d": 4,
        "m": 4,
        "v": 4,
        "e": 5,
        "n": 5,
        "w": 5,
        "ñ": 5,
        "f": 6,
        "o": 6,
        "x": 6,
        "g": 7,
        "p": 7,
        "y": 7,
        "h": 8,
        "q": 8,
        "z": 8,
        "i": 9,
        "r": 9
    }

    vowels = "aeiou"
    # Create cpy_name using list comprehension
    vowels_name = []
    consontants_name = []

    # Get the full name from the user
    full_name = input("Nombre completo: ").lower()

    for letter in full_name:
        if letter in vowels:
            vowels_name.append(letter)
        elif letter == "y":
            opt_sound = input("La Y suena como ll o como i?\n")
            if opt_sound == "ll":
                consontants_name.append(letter)
            else:
                vowels_name.append("i")
        else:
            consontants_name.append(letter)

    vowels_num = [
        letter_to_number[vowel] for vowel in vowels_name
        if vowel in letter_to_number
    ]

    consontants_num = [
        letter_to_number[consontant] for consontant in consontants_name
        if consontant in letter_to_number
    ]

    vowels_total = sum(vowels_num)
    consontants_total = sum(consontants_num)

    both = []
    for each_vowel_num in vowels_num:
        both.append(each_vowel_num)
    for each_consonant_num in consontants_num:
        both.append(each_consonant_num)

    print(both)
    val1 = both.count(1)
    val2 = both.count(2)
    val3 = both.count(3)
    val4 = both.count(4)
    val5 = both.count(5)
    val6 = both.count(6)
    val7 = both.count(7)
    val8 = both.count(8)
    val9 = both.count(9)

    print(f"Escencia: {sum_digits(vowels_total)[0]} / {sum_digits(vowels_total)[1]}")
    print(f"Imagen: {sum_digits(consontants_total)[0]} / {sum_digits(consontants_total)[1]}")
    print(f"Mision: {sum_digits(sum(both))[0]} / {sum_digits(sum(both))[1]}\n")
    print(f"1: {val1} / 4: {val4} / 7: {val7}\n2: {val2} / 5: {val5} / 8: {val8}\n3: {val3} / 6: {val6} / 9: {val9}\n")
    print(f"Fisico: {val4 + val5}\nMental: {val1 +val8}\nEmocional: {val2 + val3 + val6}\nEspiritual: {val7 + val9}")


def together() -> None:
    basic()
    print("-------------------------------------------------------------------------------")
    name()
    print("-------------------------------------------------------------------------------")


def karmas(value) -> tuple:
    masters = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    if int(value) >= 9 and int(value) not in masters:
        return int(value), sum_digits(value)
    else:
        return int(value), int(value)


def sum_digits(num) -> str:
    str(num)
    num2 = sum(int(digit) for digit in str(num))
    str(num2)
    return num, num2, sum(int(digit1) for digit1 in str(num2))


def count_numbers(n) -> list:
    """Count the occurrence of each digit in a number."""
    counts = [0] * 10
    for num in n:
        while num:
            counts[num % 10] += 1
            num //= 10
    return counts


def exit_program() -> None:
    print("Exiting program...")


program_running = True

while program_running:
    option = 0
    option = main_menu()
    if option == 1:
        basic()
    elif option == 2:
        name()
    elif option == 3:
        together()
    elif option == 4:
        parejas()
    else:
        program_running = False
        exit_program()
