"""
Tähän jotain
tietoa
ohjelmasta ja sen tekijästä
"""
def todennakoisyys(pallo, maara):
    """
    Laskee todennäköisyyden voitolle
    :param pallo:
    :param maara:
    :return:
    """
    tulos = 1
    for i in range(maara):
        tulos *= (pallo - i)
        tulos //= (i + 1)
    return tulos

def vertailu(luku1, luku2):
    """
    Vertaa onko luku positiivinen
    :param luku1:
    :param luku2:
    :return:
    """
    if luku1 <= 0 or luku2 <= 0:
        print("The number of balls must be a positive number.")
        return False
    elif luku1 < luku2:
        print("At most the total number of balls can be drawn.")
        return False

    return True


def main():
    lottopallo = int(input("Enter the total number of lottery balls: "))
    arvonta_maara = int(input("Enter the number of the drawn balls: "))

    if vertailu(lottopallo, arvonta_maara):
        tulos = todennakoisyys(lottopallo, arvonta_maara)
        print(f"The probability of guessing all {arvonta_maara} "
              f"balls correctly is 1/{tulos}")


if __name__ == "__main__":
    main()