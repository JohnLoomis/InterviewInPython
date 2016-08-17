from functools import reduce


# Sort in O(n log(n)) time and O(n) space
def sort_high_to_low(integers):
    result = None
    for i in range(len(integers)):
        if result is None:
            result = [integers[i]]
            continue
        for j in range(len(result)):
            if integers[i] <= result[len(result)-1]:
                result += integers[i:i+1]
                break
            if integers[i] > result[j]:
                result = result[0:j] + integers[i:i+1] + result[j:]
                break

    return result


# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.
def get_highest_product(integers):
    if len(integers) < 3:
        raise IndexError("Input integers needs to be at least three integers")
    if len(integers) == 3:
        return reduce(lambda x, y: x*y, integers)

    highest = lowest = highest_product_of_2 = lowest_product_of_2 = highest_product_of_3 = None
    for i in range(len(integers)):
        if highest is None:
            highest = lowest = integers[i]
            continue
        else:
            if highest_product_of_2 is None:
                highest_product_of_2 = lowest_product_of_2 = reduce(lambda x, y: x*y, integers[:2])
            else:
                if highest_product_of_3 is None:
                    highest_product_of_3 = reduce(lambda x, y: x * y, integers[:3])
                else:
                    # High Product of 3
                    if integers[i] * highest_product_of_2 > highest_product_of_3:
                        highest_product_of_3 = integers[i] * highest_product_of_2
                    if integers[i] * lowest_product_of_2 > highest_product_of_3:
                        highest_product_of_3 = integers[i] * highest_product_of_2

                # High/Low Product of 2
                if integers[i] * highest > highest_product_of_2:
                    highest_product_of_2 = integers[i] * highest
                if integers[i] * lowest > highest_product_of_2:
                    highest_product_of_2 = integers[i] * lowest
                if integers[i] * lowest < lowest_product_of_2:
                    lowest_product_of_2 = integers[i] * lowest
                if integers[i] * highest < lowest_product_of_2:
                    lowest_product_of_2 = integers[i] * highest

        # Highest/Lowest
        if integers[i] > highest:
            highest = integers[i]
        if integers[i] < lowest:
            lowest = integers[i]

    return highest_product_of_3
