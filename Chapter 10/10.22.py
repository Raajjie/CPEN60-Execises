def find_solutions():
    for starfruits in range(21):
        for mangoes in range(34):
            oranges = 100 - starfruits - mangoes
            if oranges % 3 == 0:
                price = 5 * starfruits + 3 * mangoes + (oranges // 3)
                if price == 100:
                    print(f"{starfruits} starfruits, {mangoes} mangoes, {oranges} oranges")

find_solutions()
