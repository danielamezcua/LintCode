import java.util.*;

public class Solution {
    /**
     * @param str: str: the given string
     * @return: char: the first unique character in a given string
     */
    public char firstUniqChar(String str) {
        // Write your code here
        HashSet<char> set1 = new HashSet<char>();
        HashSet<char> set2 = new HashSet<char>();
        
        for (char c : str){
        	if (set2.contains(c)){
        		if (set1.contains(c)){
        			set1.remove(c);
        		}
        	} else {
        		set1.add(c);
        		set2.add(c);
        	}
        }
        Iterator<char> i = set1.iterator();
        return i.next();
    }
}