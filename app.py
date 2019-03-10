# import calculation
#
# if __name__ == '__main__':
#     nums = [1, 2, 3]
#     total = calculation.calculation_sum(nums)
#
#     print(total)


# calculation.pyからcalculation_sumをもってくる
from calculation import calculation_sum

if __name__ == '__main__':
    nums = [1, 2, 3]
    total = calculation_sum(nums)

    print(total)