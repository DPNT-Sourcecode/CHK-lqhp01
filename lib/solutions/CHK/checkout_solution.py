
from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):

        # skus: e.g. "AABBA"
        totalCheckout = 0

        ItemPriceMapping = { 
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 80,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 30,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 90,
            "Y": 10,
            "Z": 50
        }

        # Count the occurrences of each item
        itemCount = Counter(skus);

        ACount = 0
        BCount = 0
        ECount = 0
        FCount = 0

        for item in skus:
            if item not in ItemPriceMapping:
                return -1

            totalCheckout += ItemPriceMapping[item]

        ACountRemaining = ACount % 5
        totalCheckout -= (ACount // 5) * 50
        totalCheckout -= (ACountRemaining // 3) * 20

        freeBs = min(BCount, ECount // 2)
        totalCheckout -= freeBs * ItemPriceMapping["B"]
        BCount -= freeBs

        totalCheckout -= (BCount // 2) * 15

        # 3 F's give 10 discount
        totalCheckout -= (FCount // 3) * 10

        return totalCheckout


        

