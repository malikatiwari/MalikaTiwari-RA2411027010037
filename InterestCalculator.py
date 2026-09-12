class InterestCalculator:

    # Warm-up: Adding a 4th account type would require changing this method's
    # if/else chain and adding another account-type condition and rate here.
    # Every new type would also require editing the same calculation method,
    # making this class a repeated change point for new products.

    def calculate(self, balance, account_type):
        if account_type == "Savings":
            return balance * 0.04
        elif account_type == "Current":
            return balance * 0.01
        else:
            return 0.0
