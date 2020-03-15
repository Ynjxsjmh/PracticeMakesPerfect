/**
 * Description
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 *
 * Example
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-03-11 04:02
 * @tag    Linked List
 * @repeat 精简代码
 */


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode(0);
        ListNode* l = result;
        int carry = 0;

        while (l1 != nullptr && l2 != nullptr) {
            int cur_val = l1->val + l2->val + carry;
            carry = (cur_val >= 10) ? 1 : 0;
            cur_val = (cur_val >= 10) ? (cur_val-10) : cur_val;
            ListNode* cur = new ListNode(cur_val);
            l->next = cur;
            l = l->next;
            l1 = l1->next;
            l2 = l2->next;
        }

        while (l1 != nullptr) {
            int cur_val = l1->val + carry;
            carry = (cur_val >= 10) ? 1 : 0;
            cur_val = (cur_val >= 10) ? (cur_val-10) : cur_val;
            ListNode* cur = new ListNode(cur_val);
            l->next = cur;
            l = l->next;
            l1 = l1->next;
        }

        while (l2 != nullptr) {
            int cur_val = l2->val + carry;
            carry = (cur_val >= 10) ? 1 : 0;
            cur_val = (cur_val >= 10) ? (cur_val-10) : cur_val;
            ListNode* cur = new ListNode(cur_val);
            l->next = cur;
            l = l->next;
            l2 = l2->next;
        }

        if (carry) {
            ListNode* cur = new ListNode(carry);
            l->next = cur;
            l = l->next;
        }

        return result->next;
    }
};