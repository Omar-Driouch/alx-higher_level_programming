#include "lists.h"


/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: head of linked list
 * @number: index to insert
 * Return: the address of the new node, or NULL if it fails
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *slow;
	listint_t *fast;


	slow = *head;
	fast = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (fast->next != NULL && fast->n < number)
		{
			slow = slow->next;
			fast = slow->next->next;
		}

		slow = slow->next;
		new->next = slow->next;
		slow->next = new;


		
	}

	return (new);
}