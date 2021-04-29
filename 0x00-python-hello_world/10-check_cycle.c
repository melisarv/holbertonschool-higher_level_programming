#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a listint_t list has a cycle
 * @list: pointer to list
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1;
	listint_t *temp2;

	if (list == NULL)
		return (0);

	temp1 = list;
	temp2 = list->next;
	while (temp2 && temp2->next)
	{
		if (temp1 == temp2)
			return (1);

		temp1 = temp1->next;
		temp2 = temp2->next->next;
	}

	return (0);
}
