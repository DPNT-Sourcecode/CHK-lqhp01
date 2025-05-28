
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
        }

        ACount = 0
        BCount = 0

        for item in skus:
            if item not in ItemPriceMapping:
                return -1
            
            if item == "A":
                ACount += 1
            elif item == "B":
                BCount += 1

            totalCheckout += ItemPriceMapping[item]

        totalCheckout -= (ACount // 3) * 20
        totalCheckout -= (BCount // 2) * 15

        return totalCheckout


        




