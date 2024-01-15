#!/usr/bin/env python3

"""
This module just defines a function
that takes a list and returns the
sum of all items in the list as float
and this function has annotations
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This function adds items in list and returns a float"""
    sum_of_items = sum(item for item in mxd_lst)
    return (sum_of_items)
