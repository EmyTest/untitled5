import pairofdice
# def main():
#     dice = pairofdice.PairOfDice()
#     dice.roll()
#
#     print("red die:",dice.getRedDie())
#     print("blue die:",dice.getBlueDie())
#     print("sum: ",dice.sum())
# main()
def main():
    numberOfServers = 0
    for i in range(100000):
        dice = pairofdice.PairOfDice()
        dice.roll()
        if dice.sum() == 7:
            numberOfServers += 1
    print("7 occurred {0:.2%} of the time".format(numberOfServers/100000))
main()