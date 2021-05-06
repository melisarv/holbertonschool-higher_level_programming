#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse_list - reverse a singly linked list
 * @head: pointer of first node of listint_t list
 * Return: pointer of node of listint_t list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: integer 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	slow_ptr = reverse_list(slow_ptr);

	while (slow_ptr)
	{
		if ((*head)->n != slow_ptr->n)
			return (0);
		*head = (*head)->next;
		slow_ptr = slow_ptr->next;
	}

	return (1);
}
