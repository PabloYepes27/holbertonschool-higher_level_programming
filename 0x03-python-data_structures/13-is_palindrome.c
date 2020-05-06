#include "lists.h"
listint_t *reverse_listint(listint_t **head);

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: the first node
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
**/

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *reversed;
    int i = 1;

	if (head == NULL)
		return (1);
    reversed = reverse_listint(head);
	while (reversed)
	{
        if (reversed->n == tmp->n)
        {
		    reversed = reversed->next;
            tmp= tmp->next;
            i = 0;
        }
        else
        {
            i = 1;
            break;
        }
    }
    if (i == 0)
        return (1);
	return (0);
}


/**
  * reverse_listint - function that reverses a listint_t linked list.
  * @head: the first node
  * Return: A pointer to the first node of the reversed list
**/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *first, *rest;

	if (*head == NULL)
		return (NULL);
	first = NULL;
	while (*head)
	{
		rest = (*head)->next;
		(*head)->next = first;
		first = *head;
		*head = rest;
	}
	*head = first;
	return (*head);
}