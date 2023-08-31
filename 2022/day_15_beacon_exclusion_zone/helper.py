#! /usr/bin/python3


from typing import List, Tuple


def gets_slope(a: Tuple[int], b: Tuple[int]) -> int:
    '''
    returns int rather than float
    '''
    return (b[1] - a[1]) // (b[0] - a[0])


def gets_line_intersection(line1: List[Tuple[int]], line2: List[Tuple[int]]) -> Tuple[int]:
    '''
    returns Tuple[int] rather than Tuple[float]
    '''
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) // div
    y = det(d, ydiff) // div
    return (x, y)


def calculates_the_distance(a: Tuple[int], b: Tuple[int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_within_distance(a: Tuple[int], b: Tuple[int], distance: int) -> bool:
    return calculates_the_distance(a, b) <= distance