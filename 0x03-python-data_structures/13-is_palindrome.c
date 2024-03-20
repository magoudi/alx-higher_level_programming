#include"lists.h"

/**
 * is_palindrome - fsdbjbdfkjbgjdnfsfd
 * @head: pointersfagsrg
 * Return: wrejgnwjeng
 */


int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *opposite = *head;
	int n = 1, i, j;

	if (*head == NULL || current->next == NULL)
		return (1);
	while (opposite->next != NULL)
	{
		opposite = opposite->next;
		n++;
	}
	if (current->n == opposite->n)
	{
		for (i = 1; i < n / 2; i++)
		{
			current = current->next;
			opposite = *head;
			for (j = 1; j < n - i; j++)
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
