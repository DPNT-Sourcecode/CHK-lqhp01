
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
        }

        ACount = 0
        BCount = 0
        ECount = 0

        for item in skus:
            if item not in ItemPriceMapping:
                return -1
            
            if item == "A":
                ACount += 1
            elif item == "B":
                BCount += 1
            elif item == "E":
                ECount += 1

            totalCheckout += ItemPriceMapping[item]

        ACountRemaining = ACount % 5
        totalCheckout -= (ACount // 5) * 50
        totalCheckout -= (ACountRemaining // 3) * 20

        totalCheckout -= ItemPriceMapping["B"] * (ECount // 2) * BCount

        BCount = BCount - ((ECount // 2) * BCount)

        totalCheckout -= (BCount // 2) * 15

        return totalCheckout


        

