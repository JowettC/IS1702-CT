def to_binary(d):
    if d <= 1:
        return d
    return str(to_binary(d//2)) + str(d%2)

