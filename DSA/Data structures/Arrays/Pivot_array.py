def pivot_array(arr:list, num:int) -> list:
    """returns an array rotated by num"""
    return arr[num:] + arr[:num]
