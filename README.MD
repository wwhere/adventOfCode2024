Advent of Code 2024.

Starting in Python to learn about the language.

I'll try and document my main learnings here as the days go by.

# Day 1

`zip` is very nice, exactly the kind of nice-to-have I expect from Python. It accepts any number of `iterables`, and returns a list of tuples with an element from each in order.

When dealing with dictionaries, found two different ways of setting default values if a key doesn't exist. First, using `.get(key, default)`. Didn't like it here because it made this particular code too verbose without any need. Looking more, I found the `defaultdict` in `collections` which allows to specify defaults on dictionary creation, which I liked much more for this particular case.

# Day 2

Day 2 causing unexpected problems already!  Ugly code this time, might try to refactor it later a bit. 

Regarding what I've learned about Python...

A better understanding of its iterators, and in particular learnt about `enumerate`, which I'm sure will come handy more than once on this Advent of Code.

I've now created a simple template for each day to save some time on the initial boiler plate.

# Day 3

Regular expression day. Raw string literals, `split`, `search` and `findall` functions around regular expressions. Also looked into lambda definition in Python.

# Day 4

A bit to learn today around arrays. `strings` are `arrays`, which makes this easy. Also some more lambda, and some more practice with `in`.  

# Day 5

First day of graphs with Python. I messed this one quite a bit in part 1, not realising the actual ask didn't care about transitive relationships between pages. Just got lucky my way of solving it actually worked. By part 2, I realised, which made the solution much simpler. I am not going to refactor this, rather leave the overcomplicated solution.

Regarding learnings... new for me have been the use of `list()` `dict()` `set()` `intersection()` and `sorted()`. All pretty basic stuff, but still useful. I am however feeling my code is very much not Pythonic. Not sure if I'll manage to improve that during this advent of code. 

# Day 6

Quite bad and ugly code today, with lot of bad code duplication. Not proud of this one.

Specific new things I've used this day: `match` expression.

# Day 7

Quite a simple one today, hasn't given me the chance of using anything stricitly new to me in Python.

# Day 8

Another surprisingly straightforward day. Has let me take an initial look into classes in Python, defining operator behaviours and making them hashable. Also, how to use `__name__` to know if a file is the main file being executed or if it is imported as a module.

# Day 9 

Worst day so far, took me very long to correct my totally wrong approach to part B. 

In Python learnings, mostly more dealing with classes.

# Day 10

Solution for part B required just a couple of small changes from the solution to part A, which is always nice. 

In learnings, I've used `list comprehension` and `list generators`.