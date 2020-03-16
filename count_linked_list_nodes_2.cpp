/**
 * Definition of singly-linked-list:
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *        this->val = val;
 *        this->next = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param head: 
     * @return: nothing
     */
    int countNodesII(ListNode * head) {
        // 
        int odd_nodes = 0;
        ListNode *node;
        if (head){
            node = head;
            while (node) {
                if (node->val % 2 == 1 && node->val > 0){
                    odd_nodes++;
                }
                node = node->next;
            }
        }
        return odd_nodes;
    }
};