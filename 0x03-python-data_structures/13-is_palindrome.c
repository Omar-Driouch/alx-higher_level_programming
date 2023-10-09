#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *first_half = *head;
	listint_t *second_half = NULL;

	int is_palin = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	second_half = reverse_list(&slow);

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			is_palin = 0;
			break;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return is_palin;
}

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev; 
	return (prev);  
}