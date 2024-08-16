from functools import cache

N = 1_000_000


@cache
def get_mirror(n: int):
    s = str(n)
    s_mirror = s[::-1]
    return int(s_mirror)


@cache
def is_double_mirror(n):
    mirror_n = get_mirror(n)
    if n >= mirror_n:
        return False

    if len(str(n)) != len(str(mirror_n)):
        return False

    n2 = n**2
    mirror_n2 = mirror_n**2

    return mirror_n2 == get_mirror(n2)


def main():
    for n in range(N):
        if is_double_mirror(n):
            mirror_n = get_mirror(n)
            n2 = n**2
            mirror_n2 = mirror_n**2

            print(f'√{n2} = {n}')
            print(f'√{mirror_n2} = {mirror_n}')
            print("")


if __name__ == '__main__':
    main()
