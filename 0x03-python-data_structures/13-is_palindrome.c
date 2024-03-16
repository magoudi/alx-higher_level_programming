#include"lists.h"
#include<stdio.h>
#include<stdlib.h>

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * is_palindrome - fsdbjbdfkjbgjdnfsfd
 * @head: pointersfagsrg
 * Return: wrejgnwjeng
 */


int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *opposite = *head;
	int n = 0;

	if (*head == NULL)
		return (1);
	while (opposite->next != NULL)
	{
		opposite = opposite->next;
		n++;
	}
	if (current->n == opposite->n)
	{
		for (int i = 1; i < n / 2; i++)
		{
			current = current->next;
			opposite = *head;
			for (int j = 0; j < n - i; j++)
				opposite = opposite->next;
			if (current->n == opposite->n)
				continue;
			else
				return (0);
		}
		return (1);
	}
	return (0);
}
