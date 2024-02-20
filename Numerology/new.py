def main_menu():
    option = int(input("Choose an option: \n1. Basic\n2. Name\n3. All\n4. Exit\n"))

    if option == 1:
        basic()
    elif option == 2:
        name()
    elif option == 3:
        together()
    else:
        exit()


def basic():
    date = [int(item) for item in input("Fecha completa : ").split()]

    day = str(date[0]) + str(date[1])
    day_red = sum_digits(day)
    print(f"Alma: {day} / {day_red}")

    month = str(date[2]) + str(date[3])
    month_red = sum_digits(month)
    print(f"Ego: {month} / {month_red}")

    two_year = str(date[6]) + str(date[7])
    two_year_red = sum_digits(two_year)
    print(f"Don: {two_year} / {two_year_red}")

    year = str(date[4]) + str(date[5]) + str(date[6]) + str(date[7])
    year_red = sum_digits(year)
    print(f"Vidas Pasadas: {year} / {year_red}")

    proposito = karmas(sum(date))[0]
    proposito_red = sum_digits(proposito)
    print(f"Proposito: {proposito} / {proposito_red}")

    destino = karmas(day)[-1] + karmas(month)[-1] + karmas(year)[-1]
    destino_red = sum_digits(destino)
    print(f"Destino: {destino} / {destino_red}\n\n")

    main_menu()


def name():
    letter_to_number = {
        "a": 1, "j": 1, "s": 1,
        "b": 2, "k": 2, "t": 2,
        "c": 3, "l": 3, "u": 3,
        "d": 4, "m": 4, "v": 4,
        "e": 5, "n": 5, "w": 5, "ñ": 5,
        "f": 6, "o": 6, "x": 6,
        "g": 7, "p": 7, "y": 7,
        "h": 8, "q": 8, "z": 8,
        "i": 9, "r": 9
    }

    vowels = "aeiou"
    vowels_name = []
    consontants_name = []

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

    vowels_num = [letter_to_number[vowel] for vowel in vowels_name if vowel in letter_to_number]
    consontants_num = [letter_to_number[consontant] for consontant in consontants_name if consontant in letter_to_number]

    vowels_total = sum(vowels_num)
    consontants_total = sum(consontants_num)

    both = [vowels_total, consontants_total]
    both_total = sum(both)
    both_count = count_numbers(both)
    val1 = both.count(1)
    val2 = both.count(2)
    val3 = both.count(3)
    val4 = both.count(4)
    val5 = both.count(5)
    val6 = both.count(6)
    val7 = both.count(7)
    val8 = both.count(8)
    val9 = both.count(9)

    vowels_total_sum = sum_digits(vowels_total)
    vowels_total = vowels_total_sum[0]
    vowels_sum = vowels_total_sum[1]

    consontants_total_sum = sum_digits(consontants_total)
    consontants_total = consontants_total_sum[0]
    consontants_sum = consontants_total_sum[1]

    both_total_sum = sum_digits(both_total)
    both_total = both_total_sum[0]
    both_sum = both_total_sum[1]

    print(f"Escencia: {vowels_total} / {vowels_sum}")
    print(f"Imagen: {consontants_total} / {consontants_sum}")
    print(f"Mision: {both_total} / {both_sum}")
    print(f"1: {val1} / 2: {val2} / 3: {val3} / 4: {val4} / 5: {val5} / 6: {val6} / 7: {val7} / 8: {val8} / 9: {val9}")
    print(f"Fisico: {val4 + val5}\nMental: {val1 + val8}\nEmocional: {val2 + val3+ val6}\nEspiritual: {val7 + val9}")

    main_menu()


def together():
    basic()
    name()


def karmas(value) -> tuple:
    masters = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    if int(value) >= 9 and int(value) not in masters:
        return int(value), int(sum_digits(value))
    else:
        return int(value),


def sum_digits(num) -> tuple:
    return num, sum(int(digit) for digit in str(num))



def count_numbers(n):
    counts = {}
    for num in n:
        while num:
            digit = num % 10
            counts[digit] = counts.get(digit, 0) + 1
            num //= 10
    return counts


def exit():
    print("Exiting program...")


main_menu()
