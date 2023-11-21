### Solution
The first element of Unequal Pair [99, 1] is much bigger than the second one. The minimal guaranteed harvest is 99, and the best solution is always cut on the first one. 

Oversupply has three elements. The first and the second elements are equal, and the third element does not have so much difference. So, the strategy is to cut the first and second elements in order and cut the third one when it is high enough.

After many times of trying, [0,1,0,1,2] is the best solution, and the minimal guaranteed harvest is 20. We can see some pattern on this one，the growth list is ordered from high to low, so we should cut the elements in front, and the rate of an element to the previous element should also be considered.

After considering others' growth rates, we can find an algorithm as below.

1. **Calculate Growth Rate Proportion for Each Bamboo**: Iterate through each bamboo, compute its growth rate as a proportion of the total growth rate of all bamboo.
2. **Filter Growth Rate Proportions**: Remove proportions from the list that are less than a certain value.
3. **Create a Solution List**: Iterate through the list of growth rate proportions and add index based on the following rules:
   - If it's the first element, add it directly.
   - Otherwise, compare the current proportion with all its previous values:
     - If the ratio is less than a certain value and the growth rate is not equal, add the index of the previous proportion.
     - If the ratio is greater than a certain value, add the current index.
4. **Continuous Optimization**:
   - Continuously try and adjust the values used in the second and third steps.
   - After each adjustment, evaluate the results and optimize.

### Code

### 1. Add solution.py
In the solution.py, add a function to generate a solution list, which will generate a solution list for every growthRates list. Every step has a detailed explanation in the code.

```python
def harvest_queue(growthRates: List[int]):
    ......
    return solution
```

### 2. Changes in panda*.py
In every panda*.py file, import solution and call the harvest_queue.

```python
from solution import harvest_queue
queue = harvest_queue(plot.growthRates)
```


