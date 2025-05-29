
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
            "K": 70,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 20,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 17,
            "Y": 20,
            "Z": 21
        }

        # Count the occurrences of each item
        itemCount = Counter(skus)

        groupDiscountItems = ['S', 'T', 'X', 'Y', 'Z']
        groupDiscountCosts = []

        for item in skus:
            if item not in ItemPriceMapping:
                return -1
            
            if item in groupDiscountItems:
                groupDiscountCosts.append(ItemPriceMapping[item])

            totalCheckout += ItemPriceMapping[item]

        # Apply A dicounts
        ACountRemaining = itemCount["A"] % 5
        totalCheckout -= (itemCount["A"] // 5) * 50
        totalCheckout -= (ACountRemaining // 3) * 20

        # Apply B/E discounts
        freeBs = min(itemCount["B"], itemCount["E"] // 2)
        totalCheckout -= freeBs * ItemPriceMapping["B"]
        itemCount["B"] -= freeBs
        totalCheckout -= (itemCount["B"] // 2) * 15

        # Apply F discounts
        totalCheckout -= (itemCount["F"] // 3) * 10

        # Apply H discounts
        HCountRemaining = itemCount["H"] % 10
        totalCheckout -= (itemCount["H"] // 10) * 20
        totalCheckout -= (HCountRemaining // 5) * 5

        # Apply K discounts
        totalCheckout -= (itemCount["K"] // 2) * 20

        # Apply N discounts
        freeMs = min(itemCount["M"], itemCount["N"] // 3)
        totalCheckout -= freeMs * ItemPriceMapping["M"]

        # Apply P discounts
        totalCheckout -= (itemCount["P"] // 5) * 50

        # Apply Q/R discounts
        freeQs = min(itemCount["Q"], itemCount["R"] // 3)
        totalCheckout -= freeQs * ItemPriceMapping["Q"]
        itemCount["Q"] -= freeQs
        totalCheckout -= (itemCount["Q"] // 3) * 10

        # Apply U discounts
        totalCheckout -= (itemCount["U"] // 4) * 40

        # Apply V discounts
        VCountRemaining = itemCount["V"] % 3
        totalCheckout -= (itemCount["V"] // 3) * 20
        totalCheckout -= (VCountRemaining // 2) * 10

        # Apply group discounts
        groupDiscountCosts.sort(reverse=True)
        while len(groupDiscountCosts) >= 3:
            groupDiscount = sum(groupDiscountCosts[:3]) - 45
            totalCheckout -= groupDiscount
            groupDiscountCosts = groupDiscountCosts[3:]

        return totalCheckout


        

