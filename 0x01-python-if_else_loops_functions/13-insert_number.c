#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert a number into a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(*new_node));
	if (new_node == NULL)
		return (NULL);

	new_node->next = NULL;
	new_node->n = number;

	if ((*head) == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	temp = *head;

	while (temp->next && temp->next->n < number)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
