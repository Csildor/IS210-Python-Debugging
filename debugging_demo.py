#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Demonstrate debugging with Python's built-in pdb module."""


def calculate_average(scores):
    """Calculate the average of a nonempty list of scores."""
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def main():
    """Run a simple example that can be inspected with pdb."""
    scores = [80, 90, 100]
    average = calculate_average(scores)
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")


if __name__ == "__main__":
    main()
