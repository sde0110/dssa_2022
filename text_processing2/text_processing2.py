#######################
# Test Processing II  #
#######################

#문자열 길이 측정 함수-------------------------------------------------
def list_len(SampleList):
    count = 0
    for element in SampleList :
        count += 1
    return count

   


##################################
#스트링에서 숫자 추출해 영단어로 바꾸는 함수#
##################################

def digits_to_words(input_string):
    
    #---딕셔너리 포함 초기 세팅---
    num_dic ={"0": 'zero', "1" : 'one', "2" : 'two', "3" : 'three', "4" : 'four', "5" : 'five', "6" : 'six', "7": 'seven', "8" : 'eight', "9" :'nine'}
    stc = input_string
    res = []
    
    for i in stc :
        if(ord(i) >= 48 and ord(i) <= 57) :
        #---아스키코드에서 숫자부분에 해당하는 문자열 빼내기---

            if i in num_dic:
                res.append(num_dic.get(i))
        #---stc를 읽어가며 딕셔너리에서 key로 value값 가져오기---
    result = ' '.join(res)
    return result

###########################
#camelCase로 문자열 고치는 함수#
###########################

def to_camel_case(input_string):

    stc = input_string
    stc = stc.lstrip('_') #글자 앞 '_' 제거
    stc = stc.replace('__','_') #다중 '_' 하나로 줄이기
    list_stc = stc.split("_")
    
    
    #---'_'가 없는 문자열---
    if list_len(list_stc) == 1 :
        ''.join(list_stc)
        
    #---'_'가 있는 문자열---  
    else :
        stc = '_'.join(list_stc)
    #---소문자로 만들기--- 
        stc = stc.lower()
        list_stc = stc.split("_")
    #---리스트 요소를 2번째부터 첫글자 대문자로 만들기---
        for i in range(1, list_len(list_stc)) :
            list_stc[i] = list_stc[i].capitalize()
        
    stc = ''.join(list_stc)
    return stc



#output-------------------------------------------------

input_string1 = "Zip Code: 19104"
input_string2 = "Pi is 3.1415..."
print(digits_to_words(input_string1))
print(digits_to_words(input_string2))

input_string1 = "to_camel_case"
input_string2 = "__EXAMPLE__NAME__"
input_string3 = "alreadyCamel"
print(to_camel_case(input_string1))
print(to_camel_case(input_string2))
print(to_camel_case(input_string3))
