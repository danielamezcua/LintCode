def missingWords(s, t):
    s_words = s.split()
    t_words = t.split()
    s_words_length = len(s_words)
    missing_words = []
    s_words_index = 0
    for t_word in t_words:
        while (t_word != s_words[s_words_index]):
            missing_words += [s_words[s_words_index]]
            s_words_index+=1
        s_words_index+=1
    while s_words_index < s_words_length:
        missing_words += [s_words[s_words_index]]
        s_words_index+=1
    
    return missing_words