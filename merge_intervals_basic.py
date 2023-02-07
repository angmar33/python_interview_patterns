def merge_intervals(v: list) -> list:
    result: list = [v[0]]
    for val in v:
        if val[0] in range(result[-1][0], result[-1][1]) or val[0] in range(
            result[-1][1], result[-1][1]
        ):
            result[-1][1] = max(result[-1][1], val[1])
        else:
            result.append(val)
    return result
