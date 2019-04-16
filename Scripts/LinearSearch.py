#! Python 3
# You have a vector of N integers and there is an element that
# appears more than N/2 times. Find that element in linear time
# O(N) and constant space O(1).

def linear_search(int_list, searched_value):
    temp_list = sorted(int_list)
    item_index = (len(temp_list)-1)//2
    if temp_list[item_index] == searched_value:
        return print("The searched value {} has been found as the {} item of\
                     the list".format(searched_value, item_index))

test_list = [1,2,4,3,2,2,4,5,6,2,2,2]
searched_value = 2

linear_search(test_list, searched_value)
