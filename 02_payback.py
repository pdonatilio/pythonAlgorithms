# Greedy Payback

coins = [100, 50, 5, 1]
selectedCoins = []
sumCoins = 0
payback = 66
i = 0

while i < len(coins) and sumCoins != payback:

    if sumCoins + coins[i] <= payback:
        selectedCoins.append(coins[i])
        sumCoins += coins[i]
    else:
        i += 1  # Only increment when the payback not be useful

print(selectedCoins)
