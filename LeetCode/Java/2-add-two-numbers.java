// 标签：链表，相加

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode p = result;
        int carry = 0;

        while (l1 != null && l2 != null) {
            int sum = l1.val + l2.val + carry;

            if (sum >= 10) {
                sum -= 10;
                carry = 1;
            } else {
                carry = 0;
            }

            ListNode cur = new ListNode(sum);
            p.next = cur;
            p = p.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        


        while (l1 != null) {
            int sum = l1.val + carry;

            if (sum >= 10) {
                sum -= 10;
                carry = 1;
            } else {
                carry = 0;
            }

            ListNode cur = new ListNode(sum);
            p.next = cur;
            p = p.next;
            l1 = l1.next;
        }

        while (l2 != null) {
            int sum = l2.val + carry;

            if (sum >= 10) {
                sum -= 10;
                carry = 1;
            } else {
                carry = 0;
            }

            ListNode cur = new ListNode(sum);
            p.next = cur;
            p = p.next;
            l2 = l2.next;
        }

        if (carry == 1) {
            p.next = new ListNode(1);
        }


        return result.next;
    }
}
