def return_coins(money, denominations):
    """
    Return any amount of money in coins of available denominations
    :param money: the amount of money to be returned
    :param list denominations: available denominations of coins
    :rtype list
    :return: the minimum number of coins that sum up to the value of money to be returned
    """
    returned_coins = []
    if isinstance(money, int):
        if money <= 0:
            returned_coins = []


        else:
            denominations = sorted(denominations, reverse=True)
            for mince in denominations:
                while money >= mince:
                    returned_coins.append(mince)
                    money = money - mince
    else:
        returned_coins = []
    return returned_coins


if __name__ == "__main__":
    money = int(input("Zadej castku k vraceni: "))
    denominations = [1, 2, 5, 10, 20, 50]
    coins = return_coins(money, denominations)
    print(f"Vracím mince o hodnotě {coins} Kč.")
