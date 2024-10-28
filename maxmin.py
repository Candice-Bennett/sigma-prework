def minmax(numbers: [int]) -> [int]:
    ordered_numbers = sorted(numbers)
    return [ordered_numbers[0],ordered_numbers[-1]]

print(minmax([2,4,1,0,2,-1]))
print(minmax([20,50,12,6,14,8]))
print(minmax([100,-100]))
