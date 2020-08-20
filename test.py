#def f_then_g(f, g, n):
#    """Inverse of cascade"""
#    if n:
#        f(n)
#        g(n)
#
#grow = lambda n: f_then_g(grow, print, n//10)
#shrink = lambda n: f_then_g(print, shrink, n//10)
#
#
#def can_win(number):
#    """Determine if can win."""
#    if number <= 0:
#        return False
#    action = 1
#    while action <= 3:
#        new_state = number - action
#        if not can_win ( new_state ):
#            return True
#        action += 1
#    return False
#
#
#def count_leaves(tree):
#    """Count the number of leaves of a tree."""
#    if is_leaf(tree):
#        return 1
#    else:
#        branch_counts = [count_leaves(b) for b in branches(tree)]
#        return sum(branch_counts)
#
#
#def increment_leaves(t):
#    """Return a tree like t but with leaf values incremented."""
#    if is_leaf(t):
#        return tree(label(t) + 1)
#    else:
#        bs = [increment_leaves(b) for b in branches(t)]
#        return tree(label(t), bs)
#
#
#def leaves(tree):
#    """Return a list of the leaves of a tree."""
#    if is_leaf(tree):
#        return [label(tree)]
#    else:
#        lst_of_leaves = sum([leaves(b) for b in branches(t)], [])
#        return lst_of_leaves
#
#
#def increment(t):
#    """Return a tree like t but with all node values incremented."""
#    if is_leaf(t):
#        return tree(label(t) + 1)
#    else:
#        return tree(label(t)+1, [increment(b) for b in branches(t)])
#
#
#def couple(s1, s2):
#    """Return a list that contains lists with i-th elements of two sequences coupled together.
#        >>> s1 = [1, 2, 3]
#        >>> s2 = [4, 5, 6]
#        >>> couple(s1, s2)
#        [[1, 4], [2, 5], [3, 6]]
#        """
#    assert len(s1) == len(s2)
#    return [[s1[i], s2[i]] for i in range(len(s1))]
#
#
#def generate_paths(t, x):
#    """Yields all possible paths from the root of t to a node with the label x
#        as a list.
#    """
#    if t.label == x:
#        yield [t.label]
#    for b in t.branches:
#        for y in generate_paths(b, x):
#            yield [t.label] + y
#
#
#def splink(a, b, k):
#    """Return a list of all k suh that splicing b into a at position k gives c.
#    """
#    if b is Link.empty:
#        return a
#    elif k == 0:
#        return Link(b.label, splink(a, b.rest, k))
#    return Link(a.label, slink(a.label, b, k-1))
#
#
#def both(a, b):
#    """Return True if there is a same value in the two linked lists"""
#    if a is Link.empty or b is Link.empty:
#        return False
#    if a.first > b.first:
#        a, b = b, a
#    return a.first == b.first or both(a.rest, b)
#
#
#def ways(start, end, k, ations):
#    """Return the number of ways of reahing end from start by taking up to k ations."""
#    if start == end:
#        return 1
#    elif k == 0:
#        return 0
#    return sum([ways(f(start), end, k-1, actions for f in actions)])
#
#
#def pile(t):
#    """Return a dict that contains every path from a leaf to the root of tree t."""
#    p = {}
#    def gather(u, parent_node):
#        if is_leaf(u):
#            p[label(u)] = parent_node
#        for b in branches(u):
#            gather(b, (label(u), parent_node))
#
#
#    return gather(t, ())
#    return p
#
#
#class Path:
#"""A path through a tree from the ro ot to a leaf, identified by its leaf label.
#    >>> a = tree(5, [tree(3, [tree(1), tree(2)℄), tree(6, [tree(7)℄)℄)
#    >>> print(Path(a, 7), Path(a, 2))
#    5-6-7 5-3-2
#    """
#    def __init__(self, t, leaf_label):
#        self.pile, self.end = pile(t), leaf_label
#    def __str__(self):
#        path, s = self.pile(self.end), str(self.end)
#        while path:
#            path, s = path[1], str(path[0]) + '-' + s
#        return s
#
##tree recursion
#def combo(a, b):
#"""Return the smallest integer with all of the digits of a and b (in order).
#    >>> combo(531, 432) # 45312 contains both _531_ and 4_3_2.
#    45312
#    >>> combo(531, 4321) # 45321 contains both _53_1 and 4_321.
#    45321
#    >>> combo(1234, 9123) # 91234 contains both _1234 and 9123_.
#    91234
#    >>> combo(0, 321) # The number 0 has no digits, so 0 is not in the result.
#    321
#    """
#    if min(a, b) == 0:
#        return a + b
#    elif a%10 == b%10:
#        return combo(a//10, b//10)*10 + a%10
#
#    return min(combo(a//10, b)*10 + a%10, combo(a, b//10)*10 + b%10)
#
##Linked list
#def insert(link, value, index):
#    """Insert a value into a Link at the given index.
#
#        >>> link = Link(1, Link(2, Link(3)))
#        >>> print(link)
#        <1 2 3>
#        >>> insert(link, 9001, 0)
#        >>> print(link)
#        <9001 1 2 3>
#        >>> insert(link, 100, 2)
#        >>> print(link)
#        <9001 1 100 2 3>
#        >>> insert(link, 4, 5)
#        IndexError
#        """
#    if index == 0:
#        link.rest = link
#        link.first = value
#    elif link.rest is Link.empty:
#        raise IndexError
#    else:
#    insert(link.rest, value, index-1)

import numpy as np
import base64

"""
By Ellek Linton

Keep in mind that your self-grade written homework scores may not
necessarily be reflective of your actual written hw grades.

This doesn't include separate extra credit assignments like project contests

This is just preliminary and accuracy cannot be guarenteed (but it should
provide at least an accurate lower-bound on your grade).

This DOES account for the homework drops in this course.
"""

project_scores = {
    "p1 - Search" : 25/25, # https://www.gradescope.com/courses/82897/assignments/340525
    "p2 - MultiAgent Search" : 25/25, #https://www.gradescope.com/courses/82897/assignments/354608
    "p3 - RL" : 25/25, #https://www.gradescope.com/courses/82897/assignments/368877
    "p4 - Ghostbusters" : 25/25, #https://www.gradescope.com/courses/82897/assignments/403950
    "p5 - Machine Learning" : 25/25 #https://www.gradescope.com/courses/82897/assignments/448267
}

electronic_scores = {
    "hw1" : 100/100, #https://www.gradescope.com/courses/82897/assignments/345528
    "hw2" : 100/100, #https://www.gradescope.com/courses/82897/assignments/351751
    "hw3" : 100/100, #https://www.gradescope.com/courses/82897/assignments/367181
    "hw4" : 100/100, #https://www.gradescope.com/courses/82897/assignments/372881
    "hw5" : 100/100, #https://www.gradescope.com/courses/82897/assignments/389569
    "hw6" : 100/100, #https://www.gradescope.com/courses/82897/assignments/446299
    "hw7" : 100/100, #https://www.gradescope.com/courses/82897/assignments/457863
    "hw8" : 0/100, #https://www.gradescope.com/courses/82897/assignments/484757
}

written_scores = {
    "written hw1" : 70/70, #https://www.gradescope.com/courses/82897/assignments/368715
    "written hw2" : 70/70, #https://www.gradescope.com/courses/82897/assignments/391894
    "written hw3" : 0/60, #https://www.gradescope.com/courses/82897/assignments/448217
    "written hw4" : 70/70, #https://www.gradescope.com/courses/82897/assignments/487027
}

midterm_score = 0/100 #https://www.gradescope.com/courses/82897




### Don't edit anything below! ###

grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
gradesPNP = ["P", "P", "P", "P", "P", "P", "P", "P", "NP", "NP", "NP", "F"]
gradeBins = [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 0]


def cumulative_score():
    project_component = np.average(list(project_scores.values())) * 0.25

    electronic_to_include = list(electronic_scores.values())
    electronic_to_include.pop(np.argmin(electronic_to_include))
    electronic_to_include.pop(np.argmin(electronic_to_include))
    electronic_component = np.average(electronic_to_include) * 0.10

    written_to_include = list(written_scores.values())
    written_to_include.pop(np.argmin(written_to_include))
    written_component = np.average(written_to_include) * 0.10

    midterm_component = midterm_score * 0.20

    return (project_component + electronic_component + written_component + midterm_component) * 100

def gradeBin(score = cumulative_score()):
    bin = 0
    while score < gradeBins[bin]:
        bin += 1
    return bin

def currentStatus():
    bin = gradeBin()
    if gradesPNP[bin] == "P":
        print("Congrats! You already have enough points to pass CS188 EVEN IF you got a zero on the final!")
        print("Now relax and unwind because you will pass even if you literally bomb the final.")
        print(f"EVEN IF you score ZERO on the final, your cumulative grade would be {grades[bin]} ({gradesPNP[bin]}) in CS188.")
    else:
        print(f"You currently have a {grades[bin]} ({gradesPNP[bin]}) in CS188. You still have the potential to pass though!")
    print("-"*50)
    m = 'SW4gdGhlIHdvcmRzIG9mIEthbnllLCAiS2VlcCB5b3VyIG5vc2Ugb3V0IHRvIHRoZSBza3ksIGtlZXAgeW91ciBoZWFydCB0byBnb2QsIGFuZCBrZWVwIHlvdXIgZmFjZSB0byB0aGUgcmlzaW5nIHN1bi4i'
    print(str(base64.b64decode(m))[2:-1])

def possibleFinalGrades():
    curr_score = cumulative_score()
    for i in list(range(len(grades) - 1))[::-1]:
        binCutoff = gradeBins[i]
        binGrade = grades[i]
        binPassing = gradesPNP[i]
        final_percent_needed = max(0, (binCutoff - curr_score) / .35)
        if final_percent_needed > 0:
            print(f"To get a {binGrade} ({binPassing}) in CS188, you need to get {round(final_percent_needed, 2)}% on the final exam!")


currentStatus()
print("-"*50)
print("Now, here is what you need to do on the final to get the following final course grades:\n")
possibleFinalGrades()
m = 'WW91IGdvdCBkaXMsIGRvbid0IGxvc2UgaG9wZS4gSnVzdCByZW1lbWJlciB5b3UgZ28gdG8gZmtuIEJFUktFTEVZIHdoaWNoIGlzIHRoZSBncmVhdGVzdCBzY2hvb2wgaW4gdGhlIHdvcmxkIGFuZCB5b3UgYXJlIEtJTExJTkcgSVQh'
print("\n")
print(str(base64.b64decode(m))[2:-1])
