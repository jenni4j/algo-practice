
from typing import List 

def organizingContainers(container: List[int]) -> str:
    container_capacity = []
    color_totals = [0] * len(container[0])
    
    for c in container:
        capacity = sum(c)
        container_capacity.append(capacity)
        for i in range(len(container[0])):
            color_totals[i] += c[i]
    
    container_capacity.sort()
    color_totals.sort()
    
    if container_capacity == color_totals:
        return 'Possible'
    else:
        return 'Impossible'
    

if __name__ == 'main':
    res = organizingContainers([[1,4], [2,3]])
    print(res)