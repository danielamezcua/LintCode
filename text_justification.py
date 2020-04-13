class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        def format_line():
            extra_spaces = maxWidth - length_line
            slots = number_of_words - 1
            if number_of_words == 1:
                return words[i] + " "*extra_spaces
            else:
                remainder_spaces = extra_spaces % slots
                spaces_pslot = 1  + (extra_spaces//slots)
            
                line = []
                #check if its the last line
                if j >n_words - 1:
                    for k in range(number_of_words):
                        if k == number_of_words-1:
                            line.append(words[i+k])
                        else:
                            line.append(words[i+k] + " ")
                    line.append(" " * extra_spaces)
                else:
                    for k in range(number_of_words):
                        #check if it's the last word
                        if k == number_of_words-1:
                            line.append(words[i + k])
                        else:
                            if remainder_spaces > 0:
                                line.append(words[i + k] + " "*spaces_pslot + " ")
                                remainder_spaces -= 1
                            else:
                                line.append(words[i + k] + " "*spaces_pslot)
                return ''.join(line)
        
        # write your code here
        n_words = len(words)
        len_words = [len(word) for word in words]
        i = 0
        j = 0
        result = []
        while j < n_words:
            number_of_words = 0
            length_line = 0
            can_add_words = True
            first_word = 0
            
            #select the words that are going to be in the new line
            while can_add_words and j < n_words:
                #check if we can add a space and the next word
                if length_line + len_words[j] + first_word > maxWidth:
                    can_add_words = False
                else:
                    length_line += first_word + len_words[j]
                    number_of_words += 1
                    #remove the space if it is the first word of the line
                    if first_word == 0:
                        first_word = 1
                    j+=1
            
            result.append(format_line())
            #construct the line
            
            i = j
        return result
                
            
                
            
                
                
            
