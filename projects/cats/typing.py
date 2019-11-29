"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
#    if k >= len(paragraphs):
#        return ''
#    elif select(paragraphs[k]):
#        return paragraphs[k]
#    else:
#        choose(paragraphs, select, k + 1)
    def helper_choose(count, i):
        if i == len(paragraphs):
            return ''
        elif select(paragraphs[i]):
            if count == k:
                return paragraphs[i]
            else:
                return helper_choose(count+1, i+1)
        else:
            return helper_choose(count, i+1)
    return helper_choose(0, 0)
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def helper_about(s):
        s = split(lower(remove_punctuation(s)))
        for x in topic:
            if x in s:
                return True
        return False
    return helper_about
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    typed_length = len(typed_words)
    reference_length = len(reference_words)
    percentage = 0.0
    for x in range(min(typed_length, reference_length)):
        if typed_words[x] == reference_words[x]:
            percentage += 1/typed_length
    return percentage*100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    length = len(typed)
    time_elapsed = elapsed/60
    return (length/5)/time_elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        smallest = limit
        best_option = 0
        for x in range(len(valid_words)):
            determine = diff_function(user_word, valid_words[x], limit)
            if determine < smallest:
                smallest = determine
                best_option = x
        if smallest == limit:
            for x in range(len(valid_words)):
                equal_determine = diff_function(user_word, valid_words[x], limit)
                if equal_determine == smallest:
                    if equal_determine > limit:
                        return user_word
                    return valid_words[x]
        if diff_function(user_word, valid_words[best_option], limit) > limit:
            return user_word
        return valid_words[best_option]
#    def helper_autocorrect_smallest():
#        smallest = limit
#        best_option = 0
#        for x in range(len(valid_words)):
#            determine = diff_function(user_word, valid_words[x], limit)
#            if determine <= limit:
#                if determine < smallest:
#                    smallest = determine
#                    best_option = x
#        return best_option
#
#    def helper_autocorrect_equal():
#        for x in range(len(valid_words)):
#            determine = diff_function(user_word, valid_words[x], limit)
#            if determine == limit:
#                return x
#        return 0
#
#    smallest = helper_autocorrect_smallest()
#    equal = helper_autocorrect_equal()
#    if diff_function(user_word, valid_words[smallest], limit) > limit and diff_function(user_word, valid_words[equal], limit) > limit:
#        return user_word
#    else:
#        if diff_function(user_word, valid_words[smallest], limit) < diff_function(user_word, valid_words[equal], limit):
#            return valid_words[smallest]
#        else:
#            return valid_words[equal]
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    total_errors = abs(len(start) - len(goal))
    def helper_swapp_diff(count, i):
        if i == min(len(start), len(goal)):
            return count
        elif count > limit:
            return limit + 1
        else:
            if start[i] != goal[i]:
                return helper_swapp_diff(count+1, i+1)
            else:
                return helper_swapp_diff(count, i+1)
    return helper_swapp_diff(total_errors, 0)
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if len(start) == 0: # Fill in the condition
        # BEGIN
        return len(goal)
        # END

    elif len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        return len(start)
        # END

    def helper_edit_diff(x, y, total, len_start):
        if total > limit:
            return limit + 1
        elif x == len(start) or y == len(goal):
            return total + abs(len_start - len(goal))
        elif start[x] == goal[y]:
            return helper_edit_diff(x+1, y+1, total, len_start)
        else:
            add_diff = helper_edit_diff(x, y+1, total+1, len_start + 1)
            remove_diff = helper_edit_diff(x+1, y, total+1, len_start-1)
            substitute_diff = helper_edit_diff(x+1, y+1, total+1, len_start)
            return min(add_diff, remove_diff, substitute_diff)

    return helper_edit_diff(0, 0, 0, len(start))
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    def helper_progress():
        count = 0
        for x in range(min(len(typed), len(prompt))):
            if typed[x] == prompt[x]:
                count += 1
            else:
                return count/len(prompt)
        return count/len(prompt)
    info = {'id': id, 'progress': helper_progress()}
    send(info)
    return helper_progress()
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)      #number of players
    n_words = len(word_times[0]) - 1 #number of words
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    def helper_compute_time(nth_player, nth_word):
        return elapsed_time(word_times[nth_player][nth_word]) - elapsed_time(word_times[nth_player][nth_word-1])

    lst = [0] * n_players
    for x in range(1, n_words+1):
#        shortest = helper_compute_time(0, x)
        shortest = min([helper_compute_time(y, x) for y in range(0, n_players)])

        
#        for y in range(1, n_players):
#            if helper_compute_time(y, x) < shortest:
#                shortest = helper_compute_time(y, x)
        for z in range(0, n_players):
            if helper_compute_time(z, x) == shortest or (helper_compute_time(z, x) - shortest) < margin:
                if lst[z] == 0:
                    lst[z] = [word(word_times[z][x])]
                else:
                    lst[z] += [word(word_times[z][x])]
    for k in range(0, n_players):
        if lst[k] == 0:
            lst[k] = []
    return lst
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
