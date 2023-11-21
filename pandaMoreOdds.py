import panda
plot = panda.BambooPlot(
    'MoreOdds',
    [9, 7, 7, 5, 5, 3, 3, 3]
)

# Don't change anything above this line
# ===================================

from solution import harvest_queue
queue = harvest_queue(plot.growthRates)

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
