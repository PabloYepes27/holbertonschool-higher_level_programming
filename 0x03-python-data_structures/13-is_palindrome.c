#include "lists.h"
void reverse_listint(listint_t **head);
size_t listint_len(const listint_t *h);

/**
	* is_palindrome - checks if a singly linked list is a palindrome
	* @head: the first node
	* Return: 0 if it is not a palindrome, 1 if it is a palindrome
**/

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0, len = 0;
	
	if (head == NULL || (*head)->next == NULL)
		return (1);
	len = listint_len(*head);
	printf("\nlen before %d\n", len);
	if (len % 2 != 0)
		len = len / 2;
	else
	{
		len = len / 2;
		len -= 1;
	}
	printf("len after %d\n", len);
	while (i <= len)
	{
		tmp = tmp->next;
		i++;
	}
	printf("list before reverse\n");
	print_listint(*head);
	reverse_listint(&tmp);
	printf("list after reverse\n");
	print_listint(*head);
	while (tmp)
	{

		if (tmp->n != (*head)->n)
			return (0);
		*head = (*head)->next;
		tmp = tmp->next;
	}
	return (1);
}

/**
	* reverse_listint - function that reverses a listint_t linked list.
	* @head: the first node
	* Return: A pointer to the first node of the reversed list
**/

void reverse_listint(listint_t **head)
{
	listint_t *first, *rest;

	first = NULL;
	while (*head)
	{
		rest = (*head)->next;
		(*head)->next = first;
		first = *head;
		*head = rest;
	}
	*head = first;
}

/**
  * listint_len - function that returns the number of elements in a linked list
  * @h: the first node
  * Return: The number of elements
**/

size_t listint_len(const listint_t *h)
{
	size_t i;

	for (i = 0; h; i++)
		h = h->next;/*move towards the next thing the actual node is pointing*/
	return (i);
}