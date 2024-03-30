import wikipedia


def is_valid(page):
    try:
        wikipedia.page(page)
    except Exception:
        return False
    return True


pages = input().split(', ')


# Point1
def language_settle(pages):
    flag = 0
    if pages[-1] in wikipedia.languages():
        wikipedia.set_lang(pages[-1])
        flag = 1
    else:
        print('no results')
    return flag


# Point2
if language_settle(pages) == 1:
    def max_words_and_title(pages):
        maximum_words = 0
        maximum_title = ''
        for i in range(len(pages)-1):
            words = wikipedia.page(pages[i]).summary.split()
            words = len(words)
            if words > maximum_words:
                maximum_words = words
                maximum_title = wikipedia.page(pages[i]).title
        return str(maximum_words)+' '+str(maximum_title)


# Point3
def output_spisok(pages):
    output = [pages[0]]
    for i in range(len(pages)-1):
        link = wikipedia.page(pages[i]).links
        if (str(pages[i+1]) in link) and (pages[i+1] != len(pages)-1):
            output.append(pages[i+1])
        else:
            for j in link:
                if is_valid(j) and (pages[i+1] in wikipedia.page(j).links):
                    output.append(j)
                    output.append(pages[i+1])
    return (output)


print(max_words_and_title(pages))
print(output_spisok(pages))
