#!/usr/bin/env python3

"""
This module just defines a function
that takes a list and returns the
sum of all items in the list as float
and this function has annotations
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ This function adds items in list and returns a float"""
    sum_of_items = sum(item for item in input_list)
    return (sum_of_items)
