def sub_sets(sset):
    return subsetsRecur([], sorted(sset))


def subsetsRecur( current, sset):
    if sset:
        return subsetsRecur(current, sset[1:]) + subsetsRecur(current + [sset[0]], sset[1:])
    return [current]

print(sub_sets([4,5,6]))

