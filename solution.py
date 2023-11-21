from typing import List

# Generated solution.
def harvest_queue(growthRates: List[int]):
    growthRates_sum = sum(growthRates)
    rate_percentage = []
    solution = []

    # Calculate the growth rate percentage of every bamboo.
    for growthRate in growthRates:
        rate_percentage.append(growthRate / growthRates_sum)

    # Calculate solution.
    for i, rate in enumerate(rate_percentage):
    # Calculate the growth rate percentage of every bamboo. If rate <= 0,08, drop it.
        if rate > 0.08:
            if i >= 1:
                for j in range(i):
                    # If (current growthRate / its previous rates < 7/12), and they are not equal, put its previous growthRates in the solution.
                    if (growthRates[i] / growthRates[j] < 7/12) and growthRates[i] != growthRates[i-1]:
                        solution.append(j)
                solution.append(i)
            else:
                # If it is the first element, put it in soulution.
                solution.append(i)

    return solution