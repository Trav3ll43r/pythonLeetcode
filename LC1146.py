import bisect


class SnapshotArray(object):

    def __init__(self, length):
        self.array = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        self.array[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.array[index], [snap_id + 1]) - 1
        return self.array[index][i][1]


if __name__ == "__main__":

    operations = ["SnapshotArray", "set", "snap", "set", "get"]
    arguments  = [[3], [0, 5], [], [0, 6], [0, 0]]

    output = []
    obj = None

    for op, args in zip(operations, arguments):
        if op == "SnapshotArray":
            obj = SnapshotArray(*args)
            output.append(None)
        elif op == "set":
            obj.set(*args)
            output.append(None)
        elif op == "snap":
            output.append(obj.snap())
        elif op == "get":
            output.append(obj.get(*args))

    print(output)
