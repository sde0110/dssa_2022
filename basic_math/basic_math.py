#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    max_num = number_list[0]
    for i in number_list :
        if i > max_num :
            max_num = i

    greatest_number = max_num
    # Write your code
    return greatest_number

def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    min_num = number_list[0]
    for j in number_list :
        if j < min_num :
            min_num = j
    smallest_number = min_num
    # Write your code
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    mean = sum(number_list)/len(number_list)

    # Write your code
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """    

    number_list.sort()
    ls_count = len(number_list)

    if ls_count % 2==0 :   
        a = ls_count // 2
        median = (number_list[a-1]+number_list[a])/2

    else :
        a = ls_count // 2
        median = number_list[a]
    
    # Write your code
    return median

if __name__ == "__main__":
    ex = [10, 33, 22, 99, 33 ,34]
    result = get_greatest(ex)
    print("max : ",result)

    result = get_smallest(ex)
    print("min : ",result)

    result = get_mean(ex)
    print("mean : ",result)

    result = get_median(ex)
    print("median : ",result)