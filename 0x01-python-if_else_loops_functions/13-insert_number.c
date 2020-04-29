#include "lists.h"

/**
 * insert_node - function that inserts a number into sorted singly linked list
 * @head: single linked list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *aux, *new;

	if (head == NULL)
		return (NULL);
	aux = malloc(sizeof(listint_t));
	if (aux == NULL)
		return (NULL);
	aux->n = number;
	aux->next = NULL;
	prev = *head;
	new = *head;

	while (new && new->n < number)
	{
		prev = new;
		new = new->next;
	}
	aux->next = new;
	if (prev)
		prev->next = aux;
	else
		*head = aux;
	return (aux);
}
