
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        print("skus: ", skus)
        totalCheckout = 0
        for i in skus:
            totalCheckout += 1
        return totalCheckout


        


