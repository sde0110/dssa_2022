#######################
# Basic Math          #
#######################

#문자열 길이 측정 함수————————————————————————
def list_len(SampleList):
    count = 0
    for element in SampleList :
        count += 1
    return count

#######################
# 가장 큰 숫자 반환       #
#######################
def get_greatest(number_list):
    max_num = number_list[0]
    for i in number_list :
        if i > max_num :
            max_num = i
    return max_num

#######################
# 가장 작은 숫자 반환     #
#######################
def get_smallest(number_list):
    min_num = number_list[0]
    for j in number_list :
        if j < min_num :
            min_num = j
    return min_num

#######################
# 평균 반환             #
#######################
def get_mean(number_list):
    mean = sum(number_list)/list_len(number_list)
    return mean


#######################
# 중앙값 반환            #
#######################
def get_median(number_list):

    number_list.sort()
    ls_count = list_len(number_list)

    if ls_count % 2==0 :   
        a = ls_count // 2
        median = (number_list[a-1]+number_list[a])/2

    else :
        a = ls_count // 2
        median = number_list[a]

    return median
#input---------------------------------------------
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