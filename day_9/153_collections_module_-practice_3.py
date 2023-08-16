# A doubly terminated queue or deque (from English double ended queue) is a linear data structure that allows elements to be inserted and deleted at both ends.

# Do more research on this on any documentation site, and then implement a deque from the collections module. The initial items on the list are given below.

# ["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"]

# The list must have the ability to incorporate elements from the left, and receive the name cities_list.

from collections import deque

cities_list=deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])
print(cities_list)