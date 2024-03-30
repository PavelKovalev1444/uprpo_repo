import wikipedia
def is_page_valid(page):
    try:
        wikipedia.page(page)
    except Exception:
        return False
    return True
pagesAndlanguage = input().split(', ')
#Point1
def language_settle(pagesAndlanguage):
    flag = 0                                                                    
    if pagesAndlanguage[-1] in wikipedia.languages():                           
        wikipedia.set_lang(pagesAndlanguage[-1])                                
        flag=1                                                                  
    else:                                                                       
        print('no results')                                                     
    return flag
#Point2
if language_settle(pagesAndlanguage) == 1:
    def max_words_and_title(pagesAndlanguage):
        maximum_words = 0
        maximum_title = ''
        for i in range(len(pagesAndlanguage)-1):
            words = wikipedia.page(pagesAndlanguage[i]).summary.split()
            words = len(words)
            if words > maximum_words:
                maximum_words = words
                maximum_title=wikipedia.page(pagesAndlanguage[i]).title
        return str(maximum_words)+' '+str(maximum_title)
#Point3 
    def output_spisok(pagesAndlanguage):
        output = [pagesAndlanguage[0]]
        for i in range(len(pagesAndlanguage)-1):
            link = wikipedia.page(pagesAndlanguage[i]).links
            if (str(pagesAndlanguage[i+1]) in link) and (pagesAndlanguage[i+1] != len(pagesAndlanguage)-1):
                output.append(pagesAndlanguage[i+1])
            else:
                for j in link:
                    if is_page_valid(j) and (pagesAndlanguage[i+1] in wikipedia.page(j).links):
                        output.append(j)
                        output.append(pagesAndlanguage[i+1])
        return(output)
    print(max_words_and_title(pagesAndlanguage))
    print(output_spisok(pagesAndlanguage))