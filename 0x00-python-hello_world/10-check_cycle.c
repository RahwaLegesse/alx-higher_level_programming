#include "lists.h"
/**
 * check_cycle - singly linked list has a cycle in it
 * @list:checking the list
 * Return:1 if it passes 0 if it fail
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return(1);
	}
	return (0);
}
