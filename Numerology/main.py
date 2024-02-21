numbers = {
        "number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55],

        "positive": ["Individualidad, Independencia, Energia masculina, Iniciativa, pionero, lider, trabaja mejor solo, dificil de convencer, guia de otros, hace todo por si mismo, confianza, fuerza", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla"],

        "negative": ["Egoista, no le gusta que lo aconsejen, orgulloso, temperamental, rechaza la critica, busca salirse con la sua, protagonista, perezoso, posterga los impulsos, necesita reconocimiento, caprichoso, arrogante, autroritario, narcisista, fanfarronea, falta de empatia, manipulador, dominante, agresivo", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla"],

        "extra": ["bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla", "bla bla"]
    }

def main_menu() -> int:
    option = 0
    option = int(input("Choose an option: \n1. Basic\n2. Name\n3. All\n4. Exit\n"))

    return option


def basic(numbers) -> None:

    date = []

    date = [int(item) for item in input("Fecha completa : ").split()]
    print(date)

    day = str(date[0]) + str(date[1])
    day_red = sum_digits(day)
    print(f"Alma: {day} / {day_red[-1]}")

    month = str(date[2]) + str(date[3])
    month_red = sum_digits(month)
    print(f"Ego: {month} / {month_red[-1]}")

    two_year = str(date[6]) + str(date[7])
    two_year_red = sum_digits(two_year)
    print(f"Don: {two_year} / {two_year_red[-1]}")

    year = str(date[4]) + str(date[5]) + str(date[6]) + str(date[7])
    year_red = sum_digits(year)
    print(f"Vidas Pasadas: {year} / {year_red[-1]}")

    proposito = karmas(sum(date))[0]
    proposito_red = sum_digits(proposito)
    print(f"Proposito: {proposito} / {proposito_red[-1]}")

    destino = sum_digits(day)[-1] + sum_digits(month)[-1] + sum_digits(
        year)[-1]
    destino_red = sum_digits(destino)
    print(f"Destino: {destino} / {destino_red[-1]}\n\n")


def name(numbers) -> None:
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

    print(
        f"Escencia: {sum_digits(vowels_total)[0]} / {sum_digits(vowels_total)[1]}"
    )
    print(
        f"Imagen: {sum_digits(consontants_total)[0]} / {sum_digits(consontants_total)[1]}"
    )
    print(f"Mision: {sum_digits(sum(both))[0]} / {sum_digits(sum(both))[1]}\n")
    print(
        f"1: {val1} / 2: {val2} / 3: {val3}\n4: {val4} / 5: {val5} / 6: {val6}\n7: {val7} / 8: {val8} / 9: {val9}\n"
    )
    print(
        f"Fisico: {val4 + val5}\nMental: {val1 + val8}\nEmocional: {val2 + val3+ val6}\nEspiritual: {val7 + val9}\n\n"
    )


def together(numbers) -> None:
    basic(numbers)
    name(numbers)


def karmas(value) -> tuple:
    masters = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    if int(value) >= 9 and int(value) not in masters:
        return int(value), sum_digits(value)
    else:
        return int(value),


def sum_digits(num) -> str:
    return str(num), sum(int(digit) for digit in str(num))


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
        basic(numbers)
    elif option == 2:
        name(numbers)
    elif option == 3:
        together(numbers)
    else:
        program_running = False
        exit_program()

