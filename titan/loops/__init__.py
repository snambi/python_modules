from . import for_loops

def generate(number: int) -> tuple[str, ...]:
    
    y = []
    for a in range(0, number, 1):
         y.append(str(a))
    
    return tuple(y)