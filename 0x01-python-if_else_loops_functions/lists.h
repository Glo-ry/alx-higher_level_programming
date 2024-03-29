#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - for singly linked list
 * @g: this is for integer
 * @next: This should point to the next node
 *
 * Description: this is a singly linked list node structure
 *
 */
typedef struct listint_s
{
	int g;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int g);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
