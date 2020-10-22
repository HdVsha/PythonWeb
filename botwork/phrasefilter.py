

def phrase_cleaner(file):
    old_file = open(file, 'r')
    old_info = []

    for line in old_file:
        old_info.append(line)

    cleaned_info = old_info.copy()  # what we will be changing and returning as a result

    # to remove non-quote posts(bc they are too long)
    for phrase in cleaned_info:
        if len(phrase) > 300:
            cleaned_info.remove(phrase)

    # to split by '#' and select first bc it's the quote:
    #     'Это нельзя не решить, это статья уже\n\n#Бурмистров_mipt'
    for i in range(len(cleaned_info)):
        divlist = list(map(str, cleaned_info[i].split('#')))
        post = divlist[0]
        post = post[:-1]
        cleaned_info[i] = post

    # using this cycle in order to use NewlineText instead of Text in Markovifying
    # (bc they are mostly lines ending with "\n" - if not, then make them such)
    for i in range(len(cleaned_info)):
        try:
            if cleaned_info[i][-1] == '!' or cleaned_info[i][-1] == '.' or cleaned_info[i][-1] == '?' or \
                    cleaned_info[i][-1] == '*':
                cleaned_info[i] = cleaned_info[i] + '\n'
        except: pass

    # to get rid of empty lines
    for phrase in cleaned_info:
        if len(phrase) == 0 or phrase[0] == "#":
            cleaned_info.remove(phrase)

    old_file.close()

    return cleaned_info


