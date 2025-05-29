
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
        }

        ACount = 0
        BCount = 0
        ECount = 0
        FCount = 0

        for item in skus:
            if item not in ItemPriceMapping:
                return -1
            
            if item == "A":
                ACount += 1
            elif item == "B":
                BCount += 1
            elif item == "E":
                ECount += 1
            elif item == "F":
                FCount += 1

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


        



