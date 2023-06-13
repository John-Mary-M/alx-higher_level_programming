#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks for palindrome in a list
 * @head: double pointer to head of the list
 * Return: True 1 or False 0
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *temp;
	int Ts[1000];

	temp = *head;
	if ((*head) == NULL)
		return (1);
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}
	if (len == 1)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		Ts[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (i = 0; i <= len / 2; i++)
	{
		if (Ts[i] != Ts[len - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
