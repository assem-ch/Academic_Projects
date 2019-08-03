/*
  Compare two linked lists A and B
  Return 1 if they are identical and 0 if they are not.
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int CompareLists(Node *headA, Node* headB)
{
  Node *p = headA;
  Node *q = headB;
    while(p && q){
        if (p->data != q->data){
            return 0;
        }
        p=p->next;
        q=q->next;
    }
    if ((p && !q) || (!p && q)) {
        return 0;
    }
    return 1;
}