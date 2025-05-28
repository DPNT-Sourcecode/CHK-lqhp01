
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

        for item in skus:
            if item not in ItemPriceMapping:
                return -1
            
            totalCheckout += ItemPriceMapping[item]
            
        return totalCheckout


        



