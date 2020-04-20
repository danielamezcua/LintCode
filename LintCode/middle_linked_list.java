/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param head: the head of linked list.
     * @return: a middle node of the linked list
     */
    public ListNode middleNode(ListNode head) {
        // write your code here
        ListNode slow = head;
        ListNode fast = head;
        if (head == null){
            return null;
        }
        while (true){
            if (fast.next == null || fast.next.next == null){
                return slow;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
    }
}