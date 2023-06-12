#include "lists.h"

/**
 * reverse_listint - Should reverses a singly-linked listint_t list.
 * @head: Points to the starting node of the list to reverse.
 *
 * Return: Points to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return *head;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Points to the head of the linked list.
 *
 * Return: 0 - If the linked list is not a palindrome
 *         1 - If the linked list is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp, *second_half;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast)
	{
		second_half = slow->next;
	}
	else
	{
		second_half = slow;
	}

	while (prev && second_half)
	{
		if (prev->n != second_half->n)
		{
			palindrome = 0;
			break;
		}
		prev = prev->next;
		second_half = second_half->next;
	}

	reverse_listint(&slow);
	temp = *head;

	while (temp->next != NULL)
		temp = temp->next;

	temp->next = slow;

	return (palindrome);
}
