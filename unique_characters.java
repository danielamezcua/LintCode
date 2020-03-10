import java.util.*;  

public class Solution {
    static final int INT_SIZE = 31;
    /*
     * @param str: A string
     * @return: a boolean
     */
    public boolean isUnique(String str) {
        // write your code here
        /* solution 1: using HashSet 
        HashSet<Character> set = new HashSet<Character>();
        int n = str.length();
        for (int i=0; i<n; i++){
            if (set.contains(str.charAt(i))){
                return false;
            }
            set.add(str.charAt(i));
        }
        return true;
        */
        
        /* Solution two: without using other data structures */
        /* We will use 5 integers (4 bytes each) as bit vectors */
        int[] characters = new int[]{0,0,0,0,0,0,0};
        int n = str.length();
        for (int i = 0; i < n; i++){
            int c = (int) str.charAt(i);
            int bit = 1 << c%INT_SIZE;
            if ((characters[c/INT_SIZE] & bit) > 0){
                return false;
            }
            characters[c/INT_SIZE] = characters[c/INT_SIZE] | bit;
        }
        return true;
    }
    
    
}