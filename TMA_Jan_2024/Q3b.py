
# define a function that returns the highest number of the repeating letter in the given word
def countRepeatingChar(word):
    # initialize the variables for the occurences to zero 
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0

    # iterate through each letter in the word, count occurences
    for letter in word.lower():
        if letter == 'a':
            a+=1
        elif letter == 'b':
            b+=1
        elif letter == 'c':
            c+=1
        elif letter == 'd':
            d+=1
        elif letter == 'e':
            e+=1
        elif letter == 'f':
            f+=1
        elif letter == 'g':
            g+=1
        elif letter == 'h':
            h+=1
        elif letter == 'i':
            i+=1
        elif letter == 'j':
            j+=1
        elif letter == 'k':
            k+=1
        elif letter == 'l':
            l+=1
        elif letter == 'm':
            m+=1
        elif letter == 'n':
            n+=1
        elif letter == 'o':
            o+=1
        elif letter == 'p':
            p+=1
        elif letter == 'q':
            q+=1
        elif letter == 'r':
            r+=1
        elif letter == 's':
            s+=1
        elif letter == 't':
            t+=1
        elif letter == 'u':
            u+=1
        elif letter == 'v':
            v+=1
        elif letter == 'w':
            w+=1
        elif letter == 'x':
            x+=1
        elif letter == 'y':
            y+=1
        elif letter == 'z':
            z+=1

    # create a list of counts for each letter
    res = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

    # find the highest number of the repeating letter in the given word
    highest_number = max(res)
    return highest_number

def digest(words):
    # create an empty list to store results 
    words_repeat_count = list()
    # split the words into individual words
    words_list = words.split(",") 
    # iterate through every word in the given list
    for word in words_list:
        # get the highest count of a repeating character
        highest_repeat_count = countRepeatingChar(word)
        # if there is 1 instance of any character, set count to 0
        if highest_repeat_count == 1:
            highest_repeat_count = 0
        # store the word and its highest repeat count
        words_repeat_count.append([word, highest_repeat_count])
    
    # find the maximum repetition count 
    max_repeat_count = 0
    for entry in words_repeat_count:
        if entry[1] > max_repeat_count:
            max_repeat_count = entry[1]
    
    # initialize the empty list to store the list of words with the same number of repeating letters
    words_by_repeat_count = list()
    final_list_for_words_by_repeat_count = list()
    # iterate through to store the list of words with the same number of repeating letters
    for i in range(max_repeat_count+1):
        for j in range(len(words_repeat_count)):
            if i == words_repeat_count[j][1]:
                words_by_repeat_count.append(words_repeat_count[j][0])
        final_list_for_words_by_repeat_count.append(words_by_repeat_count)
        words_by_repeat_count = list()
    # filter off the empty list
    filtered_words_list = [word_list for word_list in final_list_for_words_by_repeat_count if word_list]
    return filtered_words_list

words = "assistants,repeated,that,function,count,letters,suss,business,word"
print(digest(words))

    


