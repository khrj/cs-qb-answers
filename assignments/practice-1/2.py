(nums := input("Enter numbers separated by commas: ").split(',')) and print([[num1, num2, num3] for num1 in nums for num2 in [n for n in nums if n != num1] for num3 in [n for n in nums if n != num1 and n != num2]])