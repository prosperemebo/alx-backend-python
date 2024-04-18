#!/usr/bin/env python3
""" Type-annotated function sum_mixed_list """

from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """Type-annotated implementation for sum_mixed_list"""
    return sum(mxd_lst)
