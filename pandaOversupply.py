import panda
plot = panda.BambooPlot(
    'Oversupply',
    [10, 10, 5]
)

# Don't change anything above this line
# ===================================

from solution import harvest_queue
queue = harvest_queue(plot.growthRates)

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
