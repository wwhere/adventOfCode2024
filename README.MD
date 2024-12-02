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