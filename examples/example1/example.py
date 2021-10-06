from typing import List

def top_level() -> List[int]:
    result = []
    for i in range(15000):
        l = lower_level(i)
        s = sum(l)
        result.append(s)

    return result



def lower_level(i: int) -> List[int]:
    result = []

    for j in range(i):
        result.append(j)

    return result


if __name__ == "__main__":
    result = top_level()
