__author__ = 'atlas'
# Given an array of strings containing three types of braces: round (), square [] and curly {}
# Your task is to write a function that checks whether the braces in each string are correctly matched
# Prints 1 to standard output if the braces in each string are matched and 0 if they're not (one result per line)
# Note that your function will receive the following arguments:
# Expressions which is an array of strings containing braces
# Data constraints
# The length of the array will not exceed 100
# The length of any string will not exceed 5000
# Efficiency constraints
# Your function is expected to print the result in less than 2 seconds
# Example:
# input: expressions: [ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ]
# output: 0 1 1 1 0

import time

# Approach 1
def validate(element):
    for i, char in enumerate(element):
        if i == 0:
            if char == ")":
                return False
            elif char == "]":
                return False
            elif char == "}":
                return False

        if char == "[":
            if "]" not in element:
                return False
        if char == "{":
            if "}" not in element:
                return False
        if char == "(":
            if ")" not in element:
                return False
        else:
            return True


# Approach 2
def count(element):
    if len(element) <= 5000:
        if element.count("{") == element.count("}"):
            if element.count("[") == element.count("]"):
                if element.count("(") == element.count(")"):
                    return True
    return False


def read(expressions):
    if len(expressions) > 100:
        print "The length of the array should not be more than 100"
    else:
        for element in expressions:
            print element
            if count(element):
                print 1
            else:
                print 0


startTime = time.time()
read([")(){}", "[]({})", "([])", "{()[]}", "([)]", "([{[(])}])"])
print("--- %s seconds ---" % (time.time() - startTime))
