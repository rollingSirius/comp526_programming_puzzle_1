import panda
plot = panda.BambooPlot(
    'Power',
    [16, 8, 4, 2, 1, 1]
)

# Don't change anything above this line
# ===================================

from solution import harvest_queue
queue = harvest_queue(plot.growthRates)

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
