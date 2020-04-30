/**
 * Description
 *
 *
 * Example
 * Input:
 * Output:
 * Explanation:
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-04-30 19:55
 * @tag    Linked List
 * @repeat
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* p = dummy;

        while (l1 != nullptr && l2 != nullptr) {
            int val1 = l1->val;
            int val2 = l2->val;
            ListNode* cur = new ListNode(val1 > val2 ? val2 : val1); // 小的那个
            p->next = cur;
            p = p->next;
            if (val1 > val2) {
                l2 = l2->next;
            } else {
                l1 = l1->next;
            }
        }

        p->next = l1 ? l1 : l2;

        return dummy->next;
    }
};
