def frange(start, stop, step=1.0, endpoint=False):
    """
    BLABLABLA

    Arguments:
     - start (float): the start value of the list
     - stop (float): the stop value of the list
     - step (float): the steps between the elements of the list
     - endpoint (bool): 
    
    Returns:
     A list with floats
    """
    numbers = []
    while True:
        numbers.append(start)

        start += step # start = start + step

        if start > stop and endpoint or start >= stop and not endpoint:
            break
        
        # Zelfde als hiervoor alleen dan in leesbaardere regels
        if endpoint:
            if start > stop:
                break
        else:
            if start >= stop:
                break
    
    return numbers

print(frange(1, 2, 0.1, True))
