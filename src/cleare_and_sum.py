import math


def clear_and_sum():
    with open("nums.txt") as file:
        rows = (row.split("#")[0].rstrip() for row in file)
        nums = (float(n) for n in rows if n)
        nums = (n for n in nums if math.isfinite(n))
        nums = (max(0., n) for n in nums)
        total_sum = sum(nums)
        return f'the sum is {total_sum}'


if __name__ == "__main__":
    print(clear_and_sum())