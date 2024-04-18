#!/usr/bin/env python3
""" Type-annotated function make_multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated implementation for make_multiplier"""

    def multiply(floaty: float) -> float:
        """Type-annotated function multiply"""
        return float(floaty * multiplier)

    return multiply
