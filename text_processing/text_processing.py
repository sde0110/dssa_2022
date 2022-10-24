#######################
# Test Processing I   #
#######################

#문자열 길이 측정 함수——————————————————
def list_len(SampleList):
    count = 0
    for element in SampleList :
        count += 1
    return count

############################################
#문자열 소문자, 사이 띄어쓰기는 한칸, 앞뒤 띄어쓰기 제거#
############################################
def normalize(input_string):
    normalized_string = input_string
    normalized_string = normalized_string.lower() #소문자 변환
    normalized_string = normalized_string.strip() #양쪽 띄어쓰기 자르기
    double_space = "  " # 두번 띄어쓰기
    for double_space in normalized_string :
            normalized_string = normalized_string.replace("  "," ")
            #띄어쓰기 하나로 변환
    
    return normalized_string 

####################
#모든 모음 제거 한 문자열#
#####################

def no_vowels(input_string):
    no_vowel_string = input_string

    for vowel in no_vowel_string :
        if vowel in "aeiouAEIOU" :
        #해당 문자열에 있는 문자 삭제
            no_vowel_string = no_vowel_string.replace(vowel,'')
    return no_vowel_string

#output-------------------------------------------------

input_string1 = "This is an example."
input_string2 = "We love Python!"
result1 = no_vowels(input_string1)
result2 = no_vowels(input_string2)
print(result1)
print(result2)

input_string1 = "   EXTRA   SPACE   "
input_string2 = "We love Python!"
result1 = normalize(input_string1)
result2 = normalize(input_string2)
print(result1)
print(result2)
