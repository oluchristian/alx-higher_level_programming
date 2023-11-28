#include "lists.h"
/**
 * check_cycle - checks if a linked list is a cycle
 * @list: head node
 * Return: returns 1 if a cycle is detected. Else 0
 * */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list; 
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
