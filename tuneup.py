#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment
Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Justin Phillips"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        c_profile = cProfile.Profile()
        c_profile.enable()
        result = func(*args, **kwargs)
        c_profile.disable()
        sortby = 'cumulative'
        p_stats = pstats.Stats(c_profile).sort_stats(sortby)
        p_stats.print_stats()
        return result
    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    movies_obj = {}
    for movie in movies:
        if movies_obj.get(movie):
            movies_obj[movie] += 1
        else:
            movies_obj[movie] = 1
    return [movie for movie, c in movies_obj.items() if c > 1]


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    # YOUR CODE GOES HERE
    t = timeit.Timer(stmt="main()", setup="from __main__ import main")
    result = t.repeat(repeat=7, number=5) / 5
    fastest = min(result)
    print(f'Best time across 7 repeats of 5 runs per repeat: {fastest} sec')


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))
    


if __name__ == '__main__':
    main()
