public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) {this.val = val;};
    ListNode(int val, ListNode next) {this.val = val; this.next = next;}
    public ListNode addNode(ListNode head, int val) {
        ListNode current = head;
        while(current.next != null) {
            System.out.println(current.next);
            current = current.next;
        }
        current.next = new ListNode(val);
        
        return head;
    }
    public ListNode addFront(ListNode head, int val) {
        if(val <= head.val) {
            ListNode newHead = new ListNode(val, head);
            return newHead;
        }
        while(val > head.next.val) {
            head = head.next;
            if(head == null) {
                return null;
            }
        }
        head.next = new ListNode(val, head.next);
        return head;
    }
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode runner1 = list1;
        while(list1 != null) {
            while(list2 != null) {
                if(list2.val <= list1.val) {
                    ListNode temp = list2.next;
                    list2.next = list1;
                    System.out.println("before");
                    ListNode.display(list2);
                    list2 = temp;
                    System.out.println("change");
                    ListNode.display(list1);
                    ListNode.display(list2);
                    break;
                }
                list2 = list2.next;
                System.out.println(list2.val);
            }
            list1 = list1.next;
        }
        ListNode.display(runner1);
        System.out.println("here");
        return list1;
    }
    public static void display(ListNode head) {
        while(head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }
}