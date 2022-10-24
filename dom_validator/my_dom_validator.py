################################################
# Validate mark up language using python stack #
################################################

def is_validate_dom(dom_text : str) -> bool:
    
    #Declararaion
    judge = True
    tags = first_tag = last_tag = []

    # *first tag, last tag is stack
    # *first tag form : '< >'
    # *last tag form : '</ >'
    #---------------------------------------------------#
    #Clean up the string
    #Classify first_tag and last_tag
    dom_text = dom_text.replace('</', ' </')
    dom_text = dom_text.replace('<', ' <')
    dom_text = dom_text.replace('=', '= ')
    dom_text = dom_text.replace('>', ' ')
    dom_text = dom_text.replace('\n','')
    tags = dom_text.split(' ')
    last_tag = [i for i in tags if "</" in i]

    #To classify '<' and '</'
    for j in tags :
        if j not in last_tag :
            first_tag.append(j)
    first_tag = [j for j in first_tag if "<" in j]
    dom_text = ' '.join(last_tag)
    dom_text = dom_text.replace('/','')
    last_tag = dom_text.split(' ')
    
    #---------------------------------------------------#
    
    # Return false if tag stack is empty
    if len(first_tag) == 0 or len(last_tag) == 0 :
        judge = False

    # Pop values after comparing first tag and last tag value
    for i in range(len(first_tag)) : 
        if first_tag[0] == last_tag[-1] :
            first_tag.pop(0)
            last_tag.pop()

    # Return false if tag stack is not empty
    if len(first_tag) != 0 or len(last_tag) != 0 :
        judge = False
        
    return judge

################################################
# -----------------test field -----------------#
################################################

if __name__ == "__main__":
    example1 ="""<data>
            <items>
                <item name="item1">item1abc</item>
                <item name="item2">item2abc</item>
            </items>
        </data>
        """.strip()
    print(is_validate_dom(example1))
    # True

    example2 ="""<items>
             <data>
                 <items name="item1">item1abc</items>
                 <item name="item2">item2abc</item>
             </items>
         </data>
         """.strip()
    print(is_validate_dom(example2))
    # False

    example3 = "<a>ddd</a>"
    print(is_validate_dom(example3))
    # True


