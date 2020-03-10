public class Solution {
    /*
     * @param s: A string
     * @return: A string
     */
    public String reverseWords(String s) {
        // write your code here
        ArrayList<String> words = new ArrayList<String>();
        boolean readingWord = false;
        int number_words = 0;
        int start_word = -1;
        for (int i = 0; i < s.length(); i++){
            /* found a space */
            if (s.charAt(i) == ' '){
                if (readingWord){
                    words.add(s.substring(start_word,i));
                    readingWord = false;
                    number_words+=1;
                }
            } 
            else if (readingWord == false){
                readingWord = true;
                start_word = i;
            }
        }
        if (readingWord) {
            words.add(s.substring(start_word,s.length()));
            number_words +=1;
        }
        
        StringBuilder builder = new StringBuilder();
        /* form the new string */
        for (int i = number_words - 1; i>= 0; i--){
            builder.append(words.get(i));
            if (i != 0){
                builder.append(" ");
            }
        }
        return builder.toString();
    }
}