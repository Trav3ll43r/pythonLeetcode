import random


class Solution(object):

    def __init__(self, nums):
        self.original = nums[:]

    def reset(self):
        return self.original

    def shuffle(self):
        results = self.original[:]
        random.shuffle(results)
        return results


if __name__ == "__main__":

    operations = ["Solution", "shuffle", "reset", "shuffle"]
    arguments  = [[[1, 2, 3]], [], [], []]

    output = []
    obj = None

    for op, args in zip(operations, arguments):
        if op == "Solution":
            obj = Solution(*args)
            output.append(None)
        elif op == "shuffle":
            output.append(obj.shuffle())
        elif op == "reset":
            output.append(obj.reset())

    print(output)
