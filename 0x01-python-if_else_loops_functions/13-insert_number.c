#include"lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else if (current->n > number)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next->n < number && current->next != NULL)
			current = current->next;
	new->next = current->next;
	current->next = new;
	}

	return (new);
}
