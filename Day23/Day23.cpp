#include <iostream>
#include <algorithm> // for std::find
#include <iterator> // for std::begin, std::end
// #include <fstream>
// #include <string>
// #include <vector>

struct node 
{
    int data;
    node *next;
};

class linked_list
{
    private:
    node *head,*tail,*current_node;
    int maximum{0};
    public:
    linked_list()
    {
        head = NULL;
        tail = NULL;
    }
    void add_node(int n)
    {
        node *tmp = new node;
        tmp->data = n;
        tmp->next = NULL;

        if(head==NULL)
        {
            head = tmp;
            tail = tmp;
        }
        else
        {
            tail->next = tmp;
            tail = tail->next;
            tail->next = head;
        }
        if (tmp->data > maximum)
        {
            maximum = tmp->data;
        }
        
    }
    void insertNode(node *place, node *insert)
    {
        node *tmp = place->next;
        place->next = insert;
        insert->next->next->next = tmp;
    }
    void move()
    {
        # Splice three cups to the right
        node *spliced_start = current_node->next;
        int spliced_values {spliced_start->data,spliced_start->next->data, spliced_start}
        // spliced_stop = current_cup.right.right.right
        // spliced_values = [spliced_start.val, spliced_start.right.val, spliced_stop.val]
        // #Connect the current cup to the cup after the splice
        current_node->next = spliced_start->next->next->next;

        node *next_cup = current_node->next;
        int value {};
        for(int i=current_node->data-1; current_node->data-4;i--)
        {
            bool exists = std::find(std::begin(a), std::end(a), x) != std::end(a);
        } 
    }
    void display()
    {
        node *tmp;
        tmp = head;
        std::cout << tmp->data << std::endl;
        tmp = tmp->next;
        while (tmp->data != head->data)
        {
            std::cout << tmp->data << std::endl;
            tmp = tmp->next;
        }
    }
};

int main() 
{
    int input[] {8,5,3,1,9,2,6,4,7};
    linked_list a;
    for(int i : input){
        a.add_node(i);
    }
    // a.add_node(1);
    // a.add_node(2);
    a.display();
    return 0;
}