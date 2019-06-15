#include <stdio.h>      /* printf, scanf, puts */
#include <stdlib.h>     /* realloc, free, exit, NULL */

// gcc linked_list.c -o linked_list -g
// valgrind --leak-check=full --show-leak-kinds=all -v ./linked_list

/*********************************************************************************/
/********************************** STRUCTURES ***********************************/
/*********************************************************************************/

typedef struct SinglyLinkedListNode
{
	int data;
	struct SinglyLinkedListNode *next;
} SinglyLinkedListNode;

typedef struct SinglyLinkedList
{
	SinglyLinkedListNode *head;
} SinglyLinkedList;

typedef struct DoublyLinkedListNode
{
	int data;
	struct DoublyLinkedListNode *prev;
	struct DoublyLinkedListNode *next;
} DoublyLinkedListNode;

typedef struct HashTableNode
{
	int key;
	int value;
	struct HashTableNode *next;
} HashTableNode;

typedef struct HashTableSinglyLinkedList
{
	HashTableNode *head;
} HashTableSinglyLinkedList;

typedef struct HashTable
{
	int size;
	HashTableSinglyLinkedList **linked_lists;
} HashTable;

/*********************************************************************************/
/********************************** PROTOTYPES ***********************************/
/*********************************************************************************/

/*********************************************************************************/
/********************************* LINKED LISTS **********************************/
/*********************************************************************************/

/* This function creates a singly linked list */
SinglyLinkedList* CreateSinglyLinkedList(SinglyLinkedList* singly_linked_list);

/* This function creates a singly linked list node */
SinglyLinkedListNode* CreateSinglyLinkedListNode(int data, SinglyLinkedListNode* next);

/* This function traverses forward a singly linked list */
void TraverseForwardSinglyLinkedList(SinglyLinkedList* singly_linked_list);

/* This function prepends a new node to the beginning of a singly linked list */
SinglyLinkedList* PrependSinglyLinkedList(SinglyLinkedList* singly_linked_list, int data);

/* This function appends a new node to the end of a singly linked list */
SinglyLinkedList* AppendSinglyLinkedList(SinglyLinkedList* singly_linked_list, int data);

/* This function searches a singly linked list for a node based on its data */
SinglyLinkedListNode* SearchSinglyLinkedList(SinglyLinkedList* singly_linked_list, int data);

/* This function inserts a new node after a node in a singly linked list */
SinglyLinkedList* InsertSinglyLinkedListNodeAfterNode(SinglyLinkedList* singly_linked_list, int data, SinglyLinkedListNode* prev_node);

/* This function inserts a new node before a node in a singly linked list */
SinglyLinkedList* InsertSinglyLinkedListNodeBeforeNode(SinglyLinkedList* singly_linked_list, int data, SinglyLinkedListNode* next_node);

/* This function removes the head node from singly linked list */
SinglyLinkedList* RemoveSinglyLinkedListHeadNode(SinglyLinkedList* singly_linked_list);

/* This function removes the tail node from singly linked list */
SinglyLinkedList* RemoveSinglyLinkedListTailNode(SinglyLinkedList* singly_linked_list);

/* This function removes a node from singly linked list */
SinglyLinkedList* RemoveSinglyLinkedListNode(SinglyLinkedList* singly_linked_list, SinglyLinkedListNode* node);

/* This function insertion sorts a singly linked list */
SinglyLinkedList* InsertionSortSinglyLinkedList(SinglyLinkedList* singly_linked_list);

/* This function reverses a singly linked list */
SinglyLinkedList* ReverseSinglyLinkedList(SinglyLinkedList* singly_linked_list);

/* This function removes duplicates from a singly linked list with a buffer allowed*/
SinglyLinkedList* RemoveDuplicatesFromLinkedListBufferAllowed(SinglyLinkedList* singly_linked_list);

/* This function removes duplicates from a singly linked list with a buffer NOT allowed*/
SinglyLinkedList* RemoveDuplicatesFromLinkedListBufferNotAllowed(SinglyLinkedList* singly_linked_list);

/* This function finds the kth to last node in a singly linked list */
SinglyLinkedListNode* FindKthToLastSinglyLinkedListNode(SinglyLinkedList* singly_linked_list, unsigned int k);

/* This function partitions a linked list about a value with all nodes less than it to the left and greater than or equal to it to the right */
SinglyLinkedList* PartitionSinglyLinkedListByValue(SinglyLinkedList* singly_linked_list, int data);

/* This function checks if linked list is a palindrome */
int CheckPalindromeSinglyLinkedList(SinglyLinkedList* singly_linked_list);

/* This function deletes a singly linked list */
void DeleteSinglyLinkedList(SinglyLinkedList* singly_linked_list);

/*********************************************************************************/
/********************************* HASH TABLES ***********************************/
/*********************************************************************************/

/* Add data to hash table */
HashTable* AddDataToHashTable(HashTable* hash_table, unsigned int size, int key, int value);

/* This function returns the hash of the key */
int HashFunction(int key);

/* This function appends a new node to the end of a hash table singly linked list */
HashTableSinglyLinkedList* AppendHashTableSinglyLinkedList(HashTableSinglyLinkedList* singly_linked_list, int key, int value);

/* This function creates a hash table */
HashTable* CreateHashTable(HashTable* hash_table, unsigned int size);

/* This function creates a singly linked list */
HashTableSinglyLinkedList* CreateHashTableSinglyLinkedList(HashTableSinglyLinkedList* singly_linked_list);

/* This function creates a new hash table node */
HashTableNode* CreateHashTableNode(int key, int value, HashTableNode* next);

/* This function traverses forward a hash table */
void TraverseForwardHashTable(HashTable* hash_table);

/* This function searches a hash table for a node based on its data */
HashTableNode* SearchHashTable(HashTable* hash_table, int key, int value);

/* This function removes the head node from a singly linked list of a hash table */
HashTableSinglyLinkedList* RemoveHashTableHeadNode(HashTableSinglyLinkedList* singly_linked_list);

/* This function removes the tail node from singly linked list of a hash table */
HashTableSinglyLinkedList* RemoveHashTableTailNode(HashTableSinglyLinkedList* singly_linked_list);

/* This function removes a node from a hash table */
HashTable* RemoveHashTableNode(HashTable* hash_table, HashTableNode* node);

/* This function deletes a hash table */
void DeleteHashTable(HashTable* hash_table);

/*********************************************************************************/
/************************************ STACKS *************************************/
/*********************************************************************************/

/* This function pushes a node to the top of a stack */
SinglyLinkedList* StackPush(SinglyLinkedList* stack, int data);

/* This function pops the top node off a stack */
void StackPop(SinglyLinkedList* stack, SinglyLinkedListNode* top);

/* This function peeks at the value at the top of a stack */
SinglyLinkedListNode* StackPeek(SinglyLinkedList* stack);

/* This function checks if stack is empty */
int StackIsEmpty(SinglyLinkedList* stack);

/* This function sorts a stack using another stack */
SinglyLinkedList* SortStackUsingAnotherStack(SinglyLinkedList* stack);

/*********************************************************************************/
/************************************* MENU **************************************/
/*********************************************************************************/

/* This function displays the menu */
void Menu();

/*********************************************************************************/
/************************************* MAIN **************************************/
/*********************************************************************************/

int main(int argc, char *argv[])
{
	int command = 0;
	int data;
	unsigned int k, size;
	int key, value;

	SinglyLinkedList* singly_linked_list = NULL;
	SinglyLinkedListNode* temp_singly_linked_list_node_pointer = NULL;

	HashTable* hash_table = NULL;
	HashTableNode* temp_hash_table_node = NULL;

	SinglyLinkedList* stack = NULL;
	SinglyLinkedListNode temp_stack_node;
	SinglyLinkedListNode* temp_stack_node_pointer = NULL;

	Menu();
	while(1)
	{
		printf("\nEnter a command(0-10, -1 to quit):");
		scanf("%d", &command);

		if (command == -1)
		{
			break;
		}

		switch(command)
		{
		case 0:
			Menu();
			break;
		case 1:
			printf("main: Please enter a number to prepend:");
			scanf("%d", &data);
			singly_linked_list = PrependSinglyLinkedList(singly_linked_list, data);
			TraverseForwardSinglyLinkedList(singly_linked_list);
			break;
		case 2:
			printf("main: Please enter a number to append:");
			scanf("%d", &data);
			singly_linked_list = AppendSinglyLinkedList(singly_linked_list, data);
			TraverseForwardSinglyLinkedList(singly_linked_list);
			break;
		case 3:
			printf("main: Please enter a number to search:");
			scanf("%d", &data);
			temp_singly_linked_list_node_pointer = SearchSinglyLinkedList(singly_linked_list, data);
			if (temp_singly_linked_list_node_pointer != NULL)
			{
				printf("main: Node with value %d found.", data);
			}
			else
			{
				printf("main: Node with value %d not found.", data);
			}
			break;
		case 4:
			printf("main: Enter the node value where you want to insert after:");
			scanf("%d", &data);
			temp_singly_linked_list_node_pointer = SearchSinglyLinkedList(singly_linked_list, data);
			if (temp_singly_linked_list_node_pointer != NULL)
			{
				printf("main: Enter the node value to insert after:");
				scanf("%d", &data);
				singly_linked_list = InsertSinglyLinkedListNodeAfterNode(singly_linked_list, data, temp_singly_linked_list_node_pointer);
				if (singly_linked_list != NULL)
				{
					TraverseForwardSinglyLinkedList(singly_linked_list);
				}
			}
			else
			{
				printf("main: Node with value %d not found.", data);
			}
			break;
		case 5:
			printf("main: Enter the node value where you want to insert before:");
			scanf("%d", &data);
			temp_singly_linked_list_node_pointer = SearchSinglyLinkedList(singly_linked_list, data);
			if (temp_singly_linked_list_node_pointer != NULL)
			{
				printf("main: Enter the node value to insert before:");
				scanf("%d", &data);
				singly_linked_list = InsertSinglyLinkedListNodeBeforeNode(singly_linked_list, data, temp_singly_linked_list_node_pointer);

				if (singly_linked_list != NULL)
				{
					TraverseForwardSinglyLinkedList(singly_linked_list);
				}
			}
			else
			{
				printf("main: Node with value %d not found.", data);
			}
			break;
		case 6:
			singly_linked_list = RemoveSinglyLinkedListHeadNode(singly_linked_list);
			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 7:
			singly_linked_list = RemoveSinglyLinkedListTailNode(singly_linked_list);
			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 8:
			printf("main: Enter the node value to remove:");
			scanf("%d", &data);
			temp_singly_linked_list_node_pointer = SearchSinglyLinkedList(singly_linked_list, data);
			if (temp_singly_linked_list_node_pointer != NULL)
			{
				RemoveSinglyLinkedListNode(singly_linked_list, temp_singly_linked_list_node_pointer);
				if (singly_linked_list != NULL)
				{
					TraverseForwardSinglyLinkedList(singly_linked_list);
				}
			}
			else
			{
				printf("main: Node with value %d not found.", data);
			}
			break;
		case 9:
			singly_linked_list = InsertionSortSinglyLinkedList(singly_linked_list);
			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 10:
			singly_linked_list = ReverseSinglyLinkedList(singly_linked_list);
			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 11:
			singly_linked_list = RemoveDuplicatesFromLinkedListBufferAllowed(singly_linked_list);
			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 12:
			singly_linked_list = RemoveDuplicatesFromLinkedListBufferNotAllowed(singly_linked_list);
			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 13:
			printf("main: Enter the size of hash table:");
			scanf("%u", &size);
			printf("main: Enter the key of hash table:");
			scanf("%d", &key);
			printf("main: Enter the value of hash table:");
			scanf("%d", &value);
			hash_table = AddDataToHashTable(hash_table, size, key, value);
			if (hash_table != NULL)
			{
				TraverseForwardHashTable(hash_table);
			}
			break;
		case 14:
			printf("main: Enter the key to search in hash table:");
			scanf("%d", &key);
			printf("main: Enter the value to search in hash table:");
			scanf("%d", &value);
			temp_hash_table_node = SearchHashTable(hash_table, key, value);
			if (temp_hash_table_node != NULL)
			{
				printf("main: Node with key %d and value %d found.", key, value);
			}
			else
			{
				printf("main: Node with key %d and value %d not found.", key, value);
			}
			break;
		case 15:
			printf("main: Enter k for kth to last value:");
			scanf("%d", &k);
			temp_singly_linked_list_node_pointer = FindKthToLastSinglyLinkedListNode(singly_linked_list, k);
			if (temp_singly_linked_list_node_pointer != NULL)
			{
				printf("main: Node value %d is k = %uth from last of the list\n", temp_singly_linked_list_node_pointer->data, k);
			}
			break;
		case 16:
			printf("main: Enter the node value to partition list by:");
			scanf("%d", &data);
			singly_linked_list = PartitionSinglyLinkedListByValue(singly_linked_list, data);
			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 17:
			printf("main: Enter the value to push to a stack:");
			scanf("%d", &data);
			stack = StackPush(stack, data);
			if (stack != NULL)
			{
				TraverseForwardSinglyLinkedList(stack);
			}
			break;
		case 18:
			StackPop(stack, &temp_stack_node);
			if (&temp_stack_node != NULL)
			{
				TraverseForwardSinglyLinkedList(stack);
			}
			break;
		case 19:
			temp_stack_node_pointer = StackPeek(stack);
			if (temp_stack_node_pointer != NULL)
			{
				printf("main: Value %d is on top of the stack.\n", temp_stack_node_pointer->data);
				TraverseForwardSinglyLinkedList(stack);
			}
			break;
		case 20:
			data = CheckPalindromeSinglyLinkedList(singly_linked_list);
			if (data == 1)
			{
				printf("main: Linked list is a palindrome!\n");
			}
			else
			{
				printf("main: Linked list is NOT a palindrome!\n");
			}

			if (singly_linked_list != NULL)
			{
				TraverseForwardSinglyLinkedList(singly_linked_list);
			}
			break;
		case 21:
			stack = SortStackUsingAnotherStack(stack);
			if (stack != NULL)
			{
				TraverseForwardSinglyLinkedList(stack);
			}
			break;
		}

	}

	/* Free dynamic heap memory */
	DeleteSinglyLinkedList(stack);
	DeleteHashTable(hash_table);
	DeleteSinglyLinkedList(singly_linked_list);

	return 0;
} // end of main

/*********************************************************************************/
/*********************************** FUNCTIONS ***********************************/
/*********************************************************************************/

/*********************************************************************************/
/********************************* LINKED LISTS **********************************/
/*********************************************************************************/

/* This function creates a singly linked list */
SinglyLinkedList* CreateSinglyLinkedList(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("CreateSinglyLinkedList: Making singly linked list!\n");
		singly_linked_list = (SinglyLinkedList*)malloc(sizeof(SinglyLinkedList) * 1);
		if (singly_linked_list == NULL)
		{
			printf("CreateSinglyLinkedList: Error: Unable to make singly linked list!\n");
			exit(0);
		}

		singly_linked_list->head = NULL;
		return singly_linked_list;
	}

	printf("CreateSinglyLinkedList: No need to create singly linked list since it already exists!\n");

	return singly_linked_list;
} // end of CreateSinglyLinkedList function

/* This function creates a singly linked list node */
SinglyLinkedListNode* CreateSinglyLinkedListNode(int data, SinglyLinkedListNode* next)
{
	printf("CreateSinglyLinkedListNode: data = %d\n", data);

	SinglyLinkedListNode* new_node = (SinglyLinkedListNode*)malloc(sizeof(SinglyLinkedListNode));
    if (new_node == NULL)
    {
        printf("CreateSinglyLinkedListNode: Error: Unable to create a new node.\n");
        exit(0);
    }

    new_node->data = data;
    new_node->next = next;

    return new_node;
} // end of CreateSinglyLinkedListNode function

/* This function traverses forward a singly linked list */
void TraverseForwardSinglyLinkedList(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("TraverseForwardSinglyLinkedList: No list to traverse!\n");

		return;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("TraverseForwardSinglyLinkedList: List has no nodes to traverse!\n");

		return;
	}

	SinglyLinkedListNode* cursor = singly_linked_list->head;

	while (cursor != NULL)
	{
		printf("%d ", cursor->data);
		cursor = cursor->next;
	}
	printf("\n");

	return;
} // end of TraverseForwardSinglyLinkedList function

/* This function prepends a new node to the beginning of a singly linked list */
SinglyLinkedList* PrependSinglyLinkedList(SinglyLinkedList* singly_linked_list, int data)
{
	if (singly_linked_list == NULL)
	{
		printf("PrependSinglyLinkedListNode: List doesn't exist!\n");
		singly_linked_list = CreateSinglyLinkedList(singly_linked_list);
	}

	SinglyLinkedListNode* new_node = CreateSinglyLinkedListNode(data, singly_linked_list->head);
	singly_linked_list->head = new_node;

	return singly_linked_list;
} // end of PrependSinglyLinkedList function

/* This function appends a new node to the end of a singly linked list */
SinglyLinkedList* AppendSinglyLinkedList(SinglyLinkedList* singly_linked_list, int data)
{
	if (singly_linked_list == NULL)
	{
		printf("AppendSinglyLinkedList: List doesn't exist!\n");
		singly_linked_list = CreateSinglyLinkedList(singly_linked_list);
	}

	if (singly_linked_list->head == NULL)
	{
		printf("AppendSinglyLinkedList: Head doesn't exist!\n");
		singly_linked_list->head = CreateSinglyLinkedListNode(data, NULL);

		return singly_linked_list;
	}

	/* Find the last node */
	SinglyLinkedListNode* cursor = singly_linked_list->head;

	while (cursor->next != NULL)
	{
		cursor = cursor->next;
	}

	SinglyLinkedListNode* new_node = CreateSinglyLinkedListNode(data, NULL);
	cursor->next = new_node;

	return singly_linked_list;
} // end of AppendSinglyLinkedList function

/* This function searches a singly linked list for a node based on its data */
SinglyLinkedListNode* SearchSinglyLinkedList(SinglyLinkedList* singly_linked_list, int data)
{
	if (singly_linked_list == NULL)
	{
		printf("SearchSinglyLinkedList: List doesn't exist!\n");

		return NULL;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("SearchSinglyLinkedList: List has no nodes!\n");

		return NULL;
	}

	/* Find the node using its data */
	SinglyLinkedListNode* cursor = singly_linked_list->head;

	while (cursor != NULL)
	{
		if (cursor->data == data)
		{
			printf("SearchSinglyLinkedList: Found data = %d!\n", data);
			return cursor;
		}
		cursor = cursor->next;
	}

	return NULL;
} // end of SearchSinglyLinkedList function

/* This function inserts a new node after a node in a singly linked list */
SinglyLinkedList* InsertSinglyLinkedListNodeAfterNode(SinglyLinkedList* singly_linked_list, int data, SinglyLinkedListNode* prev_node)
{
	if (singly_linked_list == NULL)
	{
		printf("InsertSinglyLinkedListNodeAfterNode: List doesn't exist!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("InsertSinglyLinkedListNodeAfterNode: List has no nodes!\n");
		return singly_linked_list;
	}

	SinglyLinkedListNode* new_node = CreateSinglyLinkedListNode(data, prev_node->next);
	prev_node->next = new_node;

	return singly_linked_list;
} // end of InsertSinglyLinkedListNodeAfterNode function

/* This function inserts a new node before a node in a singly linked list */
SinglyLinkedList* InsertSinglyLinkedListNodeBeforeNode(SinglyLinkedList* singly_linked_list, int data, SinglyLinkedListNode* next_node)
{
	if (singly_linked_list == NULL)
	{
		printf("InsertSinglyLinkedListNodeBeforeNode: List doesn't exist!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("InsertSinglyLinkedListNodeBeforeNode: List has no nodes!\n");
		return singly_linked_list;
	}

	if (next_node == NULL)
	{
		printf("InsertSinglyLinkedListNodeBeforeNode: Next node is NULL!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == next_node)
	{
		PrependSinglyLinkedList(singly_linked_list, data);
		return singly_linked_list;
	}

	/* Find previous node */
	SinglyLinkedListNode* cursor = singly_linked_list->head;

	while (cursor != NULL)
	{
		if (cursor->next == next_node)
		{
			break;
		}
		cursor = cursor->next;
	}

	if (cursor != NULL)
	{
		SinglyLinkedListNode* new_node = CreateSinglyLinkedListNode(data, next_node);
		cursor->next = new_node;
	}

	return singly_linked_list;
} // end of InsertSinglyLinkedListNodeBeforeNode function

/* This function removes the head node from singly linked list */
SinglyLinkedList* RemoveSinglyLinkedListHeadNode(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("RemoveSinglyLinkedListHeadNode: No list to delete from!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("RemoveSinglyLinkedListHeadNode: No nodes in list to delete!\n");
		return singly_linked_list;
	}

	SinglyLinkedListNode* head = singly_linked_list->head;
	singly_linked_list->head = singly_linked_list->head->next;
	head->next = NULL;

	/* If the head is also the tail */
	if (head == singly_linked_list->head)
	{
		singly_linked_list->head = NULL;
	}
	free(head);

	return singly_linked_list;
} // end of RemoveSinglyLinkedListHeadNode function

/* This function removes the tail node from singly linked list */
SinglyLinkedList* RemoveSinglyLinkedListTailNode(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("RemoveSinglyLinkedListTailNode: No list to delete from!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("RemoveSinglyLinkedListTailNode: No nodes in list to delete!\n");
		return singly_linked_list;
	}

	/* Find last node */
	SinglyLinkedListNode* cursor = singly_linked_list->head;
	SinglyLinkedListNode* tail = NULL;

	while (cursor->next != NULL)
	{
		tail = cursor;
		cursor = cursor->next;
	}

	if (tail != NULL)
	{
		tail->next = NULL;
	}

	cursor->next = NULL;

	/* If the head is also the tail */
	if (tail == singly_linked_list->head)
	{
		singly_linked_list->head = NULL;
	}

	free(cursor);

	return singly_linked_list;
} // end of RemoveSinglyLinkedListHeadNode function

/* This function removes a node from singly linked list */
SinglyLinkedList* RemoveSinglyLinkedListNode(SinglyLinkedList* singly_linked_list, SinglyLinkedListNode* node)
{
	if (singly_linked_list == NULL)
	{
		printf("RemoveSinglyLinkedListNode: No list to delete from!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("RemoveSinglyLinkedListNode: No nodes in list to delete!\n");
		return singly_linked_list;
	}

	/* If node is head */
	if (node == singly_linked_list->head)
	{
		singly_linked_list = RemoveSinglyLinkedListHeadNode(singly_linked_list);
		return singly_linked_list;
	}

	/* If node is tail */
	if (node->next == NULL) // if there is no next, then it must be the tail node
	{
		singly_linked_list = RemoveSinglyLinkedListTailNode(singly_linked_list);
		return singly_linked_list;
	}

	/* Find node */
	SinglyLinkedListNode* cursor = singly_linked_list->head;
	while (cursor != NULL)
	{
		if (cursor->next == node)
		{
			break;
		}
		cursor = cursor->next;
	}

	if (cursor != NULL)
	{
		SinglyLinkedListNode* temp = cursor->next;
		cursor->next = temp->next;
		temp->next = NULL;
		free(temp);
	}

	return singly_linked_list;
} // end of RemoveSinglyLinkedListNode function

/* This function insertion sorts a singly linked list */
SinglyLinkedList* InsertionSortSinglyLinkedList(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("ReverseSinglyLinkedList: No list to insertion sort!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("ReverseSinglyLinkedList: No nodes in list to insertion sort!\n");
		return singly_linked_list;
	}

	SinglyLinkedListNode* node_x;
	SinglyLinkedListNode* node_y;
	SinglyLinkedListNode* node_z;

	node_x = singly_linked_list->head;
	singly_linked_list->head = NULL;

	while (node_x != NULL)
	{
		node_z = node_x;
		node_x = node_x->next;

		if (singly_linked_list->head != NULL)
		{
			if (node_z->data > singly_linked_list->head->data) // compare data between nodes
			{
				node_y = singly_linked_list->head;
				while (node_y->next != NULL && node_z->data > node_y->next->data) // compare data between nodes
				{
					node_y = node_y->next;
				}
				node_z->next = node_y->next;
				node_y->next = node_z;
			}
			else
			{
				node_z->next = singly_linked_list->head;
				singly_linked_list->head = node_z;
			}
		}
		else
		{
			node_z->next = NULL;
			singly_linked_list->head = node_z;
		}
	}

	return singly_linked_list;
} // end of InsertionSortSinglyLinkedList function

/* This function reverses a singly linked list */
SinglyLinkedList* ReverseSinglyLinkedList(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("ReverseSinglyLinkedList: No list to reverse!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("ReverseSinglyLinkedList: No nodes in list to reverse!\n");
		return singly_linked_list;
	}

	SinglyLinkedListNode* prev_node = NULL;
	SinglyLinkedListNode* current_node = singly_linked_list->head;
	SinglyLinkedListNode* next_node;
	while (current_node != NULL)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;

		/* Increment current node */
		current_node = next_node;
	}

	singly_linked_list->head = prev_node;

	return singly_linked_list;
} // end of ReverseSinglyLinkedList function

/* This function removes duplicates from a singly linked list with a buffer allowed*/
SinglyLinkedList* RemoveDuplicatesFromLinkedListBufferAllowed(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("RemoveDuplicatesFromLinkedListBufferAllowed: No list to delete from!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("RemoveDuplicatesFromLinkedListBufferAllowed: No nodes in list to delete!\n");
		return singly_linked_list;
	}

	SinglyLinkedListNode* cursor = singly_linked_list->head;
	SinglyLinkedListNode* cursor_next;

	HashTable* hash_table = NULL;
	HashTableNode* temp_hash_table_node;

	while (cursor->next != NULL)
	{
		printf("RemoveDuplicatesFromLinkedListBufferAllowed: cursor->data = %d\n", cursor->data);
		temp_hash_table_node = SearchHashTable(hash_table, cursor->data, cursor->data);
		if (temp_hash_table_node == NULL)
		{
			hash_table = AddDataToHashTable(hash_table, 10, cursor->data, cursor->data);

			cursor = cursor->next;
		}
		else
		{
			cursor_next = cursor->next;
			singly_linked_list = RemoveSinglyLinkedListNode(singly_linked_list, cursor);
			cursor = cursor_next;
		}
	}

	DeleteHashTable(hash_table);

	return singly_linked_list;
} // end of RemoveDuplicatesFromLinkedListBufferAllowed

/* This function removes duplicates from a singly linked list with a buffer NOT allowed*/
SinglyLinkedList* RemoveDuplicatesFromLinkedListBufferNotAllowed(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("RemoveDuplicatesFromLinkedListBufferNotAllowed: No list to delete from!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("RemoveDuplicatesFromLinkedListBufferNotAllowed: No nodes in list to delete!\n");
		return singly_linked_list;
	}

	SinglyLinkedListNode* current_node = singly_linked_list->head;
	SinglyLinkedListNode* cursor;
	SinglyLinkedListNode* cursor_next;

	while (current_node->next != NULL)
	{
		cursor = current_node->next;

		printf("RemoveDuplicatesFromLinkedListBufferNotAllowed: OUTER WHILE LOOP: current_node->data = %d, cursor->data = %d!\n", current_node->data, cursor->data);

		while (cursor != NULL)
		{
			printf("\tRemoveDuplicatesFromLinkedListBufferNotAllowed: INNER WHILE LOOP: current_node->data = %d, cursor->data = %d!\n", current_node->data, cursor->data);

			if (cursor->data == current_node->data) // if duplicate data
			{
				cursor_next = cursor->next;
				singly_linked_list = RemoveSinglyLinkedListNode(singly_linked_list, cursor);
				cursor = cursor_next;
			}
			else
			{
				cursor = cursor->next;
			}
		}

		current_node = current_node->next; // iterate to next node
	}

	return singly_linked_list;
} // end of RemoveDuplicatesFromLinkedListBufferNotAllowed

/* This function finds the kth to last node in a singly linked list */
SinglyLinkedListNode* FindKthToLastSinglyLinkedListNode(SinglyLinkedList* singly_linked_list, unsigned int k)
{
	if (singly_linked_list == NULL)
	{
		printf("FindKthToLastSinglyLinkedListNode: No list to traverse!\n");

		return NULL;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("FindKthToLastSinglyLinkedListNode: List has no nodes to traverse!\n");

		return NULL;
	}

	SinglyLinkedListNode* runner = singly_linked_list->head;
	SinglyLinkedListNode* cursor = singly_linked_list->head;

	/* First move k nodes into list with a pointer */
	unsigned int i;
	for (i = 0; i < k + 1; i++)
	{
		if (runner == NULL)
		{
			printf("FindKthToLastSinglyLinkedListNode: List has less than %u nodes! k is too large!\n", k + 1);
			return NULL;
		}
		runner = runner->next;
	}

	/* Now move both pointers at the same rate. When the original pointer hits the end then the second pointer is now k away from the end */
	while (runner != NULL)
	{
		runner = runner->next;
		cursor = cursor->next;
	}

	return cursor;
} // end of FindKthToLastSinglyLinkedListNode function

/* This function partitions a linked list about a value with all nodes less than it to the left and greater than or equal to it to the right */
SinglyLinkedList* PartitionSinglyLinkedListByValue(SinglyLinkedList* singly_linked_list, int data)
{
	if (singly_linked_list == NULL)
	{
		printf("PartitionSinglyLinkedListByValue: No list to partition!\n");

		return NULL;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("PartitionSinglyLinkedListByValue: List has no nodes to partition!\n");

		return NULL;
	}

	SinglyLinkedListNode* head = singly_linked_list->head;
	SinglyLinkedListNode* tail = singly_linked_list->head;
	SinglyLinkedListNode* next;

	while (singly_linked_list->head != NULL)
	{
		next = singly_linked_list->head->next;

		if (singly_linked_list->head->data < data)
		{
			/* Insert node at head */
			singly_linked_list->head->next = head;
			head = singly_linked_list->head;
		}
		else
		{
			/* Insert node at tail */
			tail->next = singly_linked_list->head;
			tail = singly_linked_list->head;
		}
		singly_linked_list->head = next;
	}
	tail->next = NULL;

	singly_linked_list->head = head;

	return singly_linked_list;
} // end of PartitionSinglyLinkedListByValue function

/* This function checks if linked list is a palindrome */
int CheckPalindromeSinglyLinkedList(SinglyLinkedList* singly_linked_list)
{
	int IsPalindrome = 0;

	if (singly_linked_list == NULL)
	{
		printf("FindKthToLastSinglyLinkedListNode: No list to traverse!\n");

		return IsPalindrome;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("FindKthToLastSinglyLinkedListNode: List has no nodes to traverse!\n");

		return IsPalindrome;
	}

	/* Create stack to store node data as we traverse */
	SinglyLinkedList* stack = NULL;

	SinglyLinkedListNode* slow = singly_linked_list->head;
	SinglyLinkedListNode* fast = singly_linked_list->head;

	while (fast != NULL && fast->next != NULL)
	{
		/* Push data onto stack */
		stack = StackPush(stack, slow->data);

		/* Move runners */
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Check to see if the fast runner is already at the end of the list. If not, there is an odd number of nodes and we need to skip the middle node */
	if (fast != NULL)
	{
		slow = slow->next;
	}

	/* Now traverse the rest of the list and check to see if it matches the stack (which will be in backwards order */
	SinglyLinkedListNode temp_stack_node;

	while (slow != NULL)
	{
		StackPop(stack, &temp_stack_node);
		if (&temp_stack_node != NULL)
		{
			if (temp_stack_node.data != slow->data)
			{
				DeleteSinglyLinkedList(stack);
				return IsPalindrome; // is NOT palindrome, stop searching
			}
		}

		slow = slow->next;
	}

	DeleteSinglyLinkedList(stack);
	IsPalindrome = 1;
	return IsPalindrome;
} // end of CheckPalindromeSinglyLinkedList function

/* This function deletes a singly linked list */
void DeleteSinglyLinkedList(SinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("DeleteSinglyLinkedList: No list to delete!\n");
		return;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("DeleteSinglyLinkedList: No nodes in list to delete!\n");
		free(singly_linked_list);
		return;
	}

	SinglyLinkedListNode *cursor, *temp;

	cursor = singly_linked_list->head->next;
	singly_linked_list->head->next = NULL;

	while (cursor != NULL)
	{
		temp = cursor->next;
		free(cursor);
		cursor = temp;
	}
	free(singly_linked_list->head);
	free(singly_linked_list);

	return;
} // end of DeleteSinglyLinkedList function

/*********************************************************************************/
/********************************* HASH TABLES ***********************************/
/*********************************************************************************/

/* Add data to hash table */
HashTable* AddDataToHashTable(HashTable* hash_table, unsigned int size, int key, int value)
{
	if (hash_table == NULL)
	{
		hash_table = CreateHashTable(hash_table, size);
	}

	unsigned int hash_index = HashFunction(key) % hash_table->size;

	printf("AddDataToHashTable: hash_index = %u\n", hash_index);

	hash_table->linked_lists[hash_index] = AppendHashTableSinglyLinkedList(hash_table->linked_lists[hash_index], key, value);

	return hash_table;
} // end of AddDataToHashTable function

/* This function returns the hash of the key */
int HashFunction(int key)
{
	return key < 0 ? -key : key;
} // end of HashFunction function

/* This function appends a new node to the end of a hash table singly linked list */
HashTableSinglyLinkedList* AppendHashTableSinglyLinkedList(HashTableSinglyLinkedList* singly_linked_list, int key, int value)
{
	if (singly_linked_list == NULL)
	{
		printf("AppendHashTableSinglyLinkedList: List doesn't exist!\n");
		singly_linked_list = CreateHashTableSinglyLinkedList(singly_linked_list);
	}

	if (singly_linked_list->head == NULL)
	{
		printf("AppendHashTableSinglyLinkedList: Head doesn't exist!\n");
		singly_linked_list->head = CreateHashTableNode(key, value, NULL);

		return singly_linked_list;
	}

	/* Find the last node */
	HashTableNode* cursor = singly_linked_list->head;

	while (cursor->next != NULL)
	{
		cursor = cursor->next;
	}

	HashTableNode* new_node = CreateHashTableNode(key, value, NULL);
	cursor->next = new_node;

	return singly_linked_list;
} // end of AppendHashTableSinglyLinkedList function

/* This function creates a hash table */
HashTable* CreateHashTable(HashTable* hash_table, unsigned int size)
{
	if (hash_table == NULL)
	{
		printf("CreateHashTable: Making hash table!\n");
		hash_table = (HashTable*)malloc(sizeof(HashTable) * 1);
		if (hash_table == NULL)
		{
			printf("CreateHashTable: Error: Unable to make hash table!\n");
			exit(0);
		}

		/* Set size of hash table */
		hash_table->size = size;

		hash_table->linked_lists = (HashTableSinglyLinkedList**)malloc(sizeof(HashTableSinglyLinkedList*) * size);
		if (hash_table->linked_lists == NULL)
		{
			printf("CreateHashTable: Error: Unable to make linked lists of hash table!\n");
			exit(0);
		}

		printf("CreateHashTable: p_hash_table->linked_lists = %p\n", hash_table->linked_lists);

		unsigned int i;

		for (i = 0; i < size; i++)
		{
			hash_table->linked_lists[i] = NULL;
		} // end of i loop

		return hash_table;
	}

	printf("CreateHashTable: No need to hash table since it already exists!\n");

	return hash_table;
} // end of CreateHashTable function

/* This function creates a singly linked list */
HashTableSinglyLinkedList* CreateHashTableSinglyLinkedList(HashTableSinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("CreateHashTableSinglyLinkedList: Making singly linked list!\n");
		singly_linked_list = (HashTableSinglyLinkedList*)malloc(sizeof(HashTableSinglyLinkedList) * 1);
		if (singly_linked_list == NULL)
		{
			printf("CreateHashTableSinglyLinkedList: Error: Unable to make singly linked list!\n");
			exit(0);
		}

		singly_linked_list->head = NULL;
		return singly_linked_list;
	}

	printf("CreateHashTableSinglyLinkedList: No need to create singly linked list since it already exists!\n");

	return singly_linked_list;
} // end of CreateHashTableSinglyLinkedList function

/* This function creates a new hash table node */
HashTableNode* CreateHashTableNode(int key, int value, HashTableNode* next)
{

	printf("CreateHashTableNode: key = %d, value = %d\n", key, value);

	HashTableNode* new_node = (HashTableNode*)malloc(sizeof(HashTableNode));
	if (new_node == NULL)
	{
		printf("CreateHashTableNode: Error: Unable to create a new node.\n");
		exit(0);
	}

	new_node->key = key;
	new_node->value = value;
	new_node->next = next;

	return new_node;
} // end of CreateHashTableNode function

/* This function traverses forward a hash table */
void TraverseForwardHashTable(HashTable* hash_table)
{
	if (hash_table == NULL)
	{
		printf("TraverseForwardHashTable: No hash table to traverse!\n");
		return;
	}

	unsigned int i;

	for (i = 0; i < hash_table->size; i++)
	{
		if (hash_table->linked_lists[i] == NULL)
		{
			printf("TraverseForwardHashTable: No list %u to traverse!\n", i);
		}
		else
		{
			if (hash_table->linked_lists[i]->head == NULL)
			{
				printf("TraverseForwardHashTable: List %u has no nodes to traverse!\n", i);
			}
			else
			{
				HashTableNode* cursor = hash_table->linked_lists[i]->head;

				while (cursor != NULL)
				{
					printf("(%d, %d) ", cursor->key, cursor->value);
					cursor = cursor->next;
				}
				printf("\n");
			}
		}
	}

	return;
} // end of TraverseForwardSinglyLinkedList function

/* This function searches a hash table for a node based on its data */
HashTableNode* SearchHashTable(HashTable* hash_table, int key, int value)
{
	if (hash_table == NULL)
	{
		printf("SearchHashTable: No hash table to search!\n");
		return NULL;
	}

	if (hash_table->linked_lists == NULL)
	{
		printf("SearchHashTable: No linked lists to search!\n");
		return NULL;
	}

	unsigned int hash_index = HashFunction(key) % hash_table->size;

	printf("SearchHashTable: hash_index = %d\n", hash_index);

	if (hash_table->linked_lists[hash_index] == NULL)
	{
		printf("SearchHashTable: No list %u to search!\n", hash_index);
		return NULL;
	}

	if (hash_table->linked_lists[hash_index]->head == NULL)
	{
		printf("SearchHashTable: No nodes in list %u to search!\n", hash_index);
		return NULL;
	}

	/* Find the node using its data */
	HashTableNode *cursor = hash_table->linked_lists[hash_index]->head;

	while (cursor != NULL)
	{
		if (cursor->key == key && cursor->value == value)
		{
			printf("SearchHashTable: Found key = %d and value = %d!\n", key, value);
			return cursor;
		}
		cursor = cursor->next;
	}

	return NULL;
} // end of SearchHashTable function

/* This function removes the head node from a singly linked list of a hash table */
HashTableSinglyLinkedList* RemoveHashTableHeadNode(HashTableSinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("RemoveHashTableHeadNode: No list to delete from!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("RemoveHashTableHeadNode: No nodes in list to delete!\n");
		return singly_linked_list;
	}

	HashTableNode* head = singly_linked_list->head;
	singly_linked_list->head = singly_linked_list->head->next;
	head->next = NULL;

	/* If the head is also the tail */
	if (head == singly_linked_list->head)
	{
		singly_linked_list->head = NULL;
	}
	free(head);

	return singly_linked_list;
} // end of RemoveHashTableHeadNode function

/* This function removes the tail node from singly linked list of a hash table */
HashTableSinglyLinkedList* RemoveHashTableTailNode(HashTableSinglyLinkedList* singly_linked_list)
{
	if (singly_linked_list == NULL)
	{
		printf("RemoveHashTableTailNode: No list to delete from!\n");
		return singly_linked_list;
	}

	if (singly_linked_list->head == NULL)
	{
		printf("RemoveHashTableTailNode: No nodes in list to delete!\n");
		return singly_linked_list;
	}

	/* Find last node */
	HashTableNode* cursor = singly_linked_list->head;
	HashTableNode* tail = NULL;

	while (cursor->next != NULL)
	{
		tail = cursor;
		cursor = cursor->next;
	}

	if (tail != NULL)
	{
		tail->next = NULL;
	}

	cursor->next = NULL;

	/* If the head is also the tail */
	if (tail == singly_linked_list->head)
	{
		singly_linked_list->head = NULL;
	}

	free(cursor);

	return singly_linked_list;
} // end of RemoveHashTableTailNode function

/* This function removes a node from a hash table */
HashTable* RemoveHashTableNode(HashTable* hash_table, HashTableNode* node)
{
	if (hash_table == NULL)
	{
		printf("RemoveHashTableNode: No hash table to search!\n");
		return hash_table;
	}

	if (hash_table->linked_lists == NULL)
	{
		printf("RemoveHashTableNode: No linked lists to search!\n");
		return hash_table;
	}

	unsigned int i;

	for (i = 0; i < hash_table->size; i++)
	{
		if (hash_table->linked_lists[i] == NULL)
		{
			printf("RemoveHashTableNode: No list %u to delete from!\n", i);
			return hash_table;
		}

		if (hash_table->linked_lists[i]->head == NULL)
		{
			printf("RemoveHashTableNode: No nodes in list %u to delete!\n", i);
			return hash_table;
		}

		/* If node is head */
		if (node == hash_table->linked_lists[i]->head)
		{
			hash_table->linked_lists[i] = RemoveHashTableHeadNode(hash_table->linked_lists[i]);
			return hash_table;
		}

		/* If node is tail */
		if (node->next == NULL) // if there is no next, then it must be the tail node
		{
			hash_table->linked_lists[i] = RemoveHashTableTailNode(hash_table->linked_lists[i]);
			return hash_table;
		}

		/* Find node */
		HashTableNode* cursor = hash_table->linked_lists[i]->head;
		while (cursor != NULL)
		{
			if (cursor->next == node)
			{
				break;
			}
			cursor = cursor->next;
		}

		if (cursor != NULL)
		{
			HashTableNode* temp = cursor->next;
			cursor->next = temp->next;
			temp->next = NULL;
			free(temp);
		}

		return hash_table;
	} // end of i loop

	return hash_table;
} // end of RemoveHashTableNode function

/* This function deletes a hash table */
void DeleteHashTable(HashTable* hash_table)
{
	if (hash_table == NULL)
	{
		printf("DeleteHashTable: No hash table to delete!\n");
		return;
	}

	if (hash_table->linked_lists == NULL)
	{
		printf("DeleteHashTable: No linked lists to delete!\n");
	}
	else
	{
		unsigned int i;

		for (i = 0; i < hash_table->size; i++)
		{
			if (hash_table->linked_lists[i] == NULL)
			{
				printf("DeleteHashTable: No list %u to delete!\n", i);
			}
			else
			{
				if (hash_table->linked_lists[i]->head == NULL)
				{
					printf("DeleteHashTable: No nodes in list %u to delete!\n", i);
					free(hash_table->linked_lists[i]);
				}
				else
				{
					HashTableNode *cursor, *temp;

					cursor = hash_table->linked_lists[i]->head->next;
					hash_table->linked_lists[i]->head->next = NULL;

					while (cursor != NULL)
					{
						temp = cursor->next;
						free(cursor);
						cursor = temp;
					}
					free(hash_table->linked_lists[i]->head);
					free(hash_table->linked_lists[i]);
				}
			}
		} // end of i loop
		free(hash_table->linked_lists);
	}
	free(hash_table);

	return;
} // end of DeleteHashTable function

/*********************************************************************************/
/************************************ STACKS *************************************/
/*********************************************************************************/

/* This function pushes a node to the top of a stack */
SinglyLinkedList* StackPush(SinglyLinkedList* stack, int data)
{
	if (stack == NULL)
	{
		printf("StackPush: No stack to push to! Creating stack!\n");
	}
	else if (stack->head == NULL)
	{
		printf("StackPop: No stack nodes to push to! Creating top node!\n");
	}

	stack = PrependSinglyLinkedList(stack, data);

	return stack;
} // end of StackPush function

/* This function pops the top node off a stack */
void StackPop(SinglyLinkedList* stack, SinglyLinkedListNode* top)
{
	if (stack == NULL)
	{
		printf("StackPop: No stack to pop from!\n");
		top = NULL;
		return;
	}

	if (stack->head == NULL)
	{
		printf("StackPop: No stack nodes to pop from!\n");
		top = NULL;
		return;
	}

	(*top) = (*stack->head);
	stack = RemoveSinglyLinkedListHeadNode(stack);
	return;
} // end of StackPop function

/* This function peeks at the value at the top of a stack */
SinglyLinkedListNode* StackPeek(SinglyLinkedList* stack)
{
	if (stack == NULL)
	{
		printf("StackPeek: No stack to peek from!\n");
		return NULL;
	}

	if (stack->head == NULL)
	{
		printf("StackPeek: No stack nodes to peek from!\n");
		return NULL;
	}

	return stack->head;
} // end of StackPeek function

/* This function checks if stack is empty */
int StackIsEmpty(SinglyLinkedList* stack)
{
	if (stack == NULL || stack->head == NULL)
	{
		printf("StackIsEmpty: No stack to even be empty!\n");
		return 1;
	}

	if (stack->head == NULL)
	{
		printf("StackIsEmpty: Stack has no nodes!\n");
		return 1;
	}

	return 0;
} // end of StackIsEmpty function

/* This function sorts a stack using another stack */
SinglyLinkedList* SortStackUsingAnotherStack(SinglyLinkedList* stack)
{
	/* Create temp stack */
	SinglyLinkedList* temp_stack = NULL;

	/* Create a temp variable to hold the top of our stack temporarily */
	int temp;

	SinglyLinkedListNode temp_stack_node;

	int data;

	while (StackIsEmpty(stack) != 1)
	{
		/* Pop off top node from original stack so that we can place it correctly into the temp stack */
		StackPop(stack, &temp_stack_node);
		if (&temp_stack_node != NULL)
		{
			temp = temp_stack_node.data;
		}

		/* Move all nodes from temp stack to original stack so that we can put saved temp variable into correct position in temp stack */
		while (temp_stack != NULL && StackIsEmpty(temp_stack) != 1 && StackPeek(temp_stack) != NULL && StackPeek(temp_stack)->data > temp)
		{
			StackPop(temp_stack, &temp_stack_node);
			if (&temp_stack_node != NULL)
			{
				data = temp_stack_node.data;
			}

			stack = StackPush(stack, data);
		}

		/* Finally add saved temp variable into correct position of temp stack */
		temp_stack = StackPush(temp_stack, temp);
	}

	/* Now move all of the nodes in backwards order in the temp stack into correct order in the original stack */
	while (temp_stack != NULL && StackIsEmpty(temp_stack) != 1)
	{
		StackPop(temp_stack, &temp_stack_node);
		if (&temp_stack_node != NULL)
		{
			data = temp_stack_node.data;
		}

		stack = StackPush(stack, data);
	}

	/* Free dynamic heap memory */
	DeleteSinglyLinkedList(temp_stack);

	return stack;
} // end of SortStackUsingAnotherStack function

/* This function displays the menu */
void Menu()
{
    printf("--- C Linked List Demonstration --- \n\n");
    printf("0. Menu\n");
    printf("1. Prepend a node\n");
    printf("2. Append a node\n");
    printf("3. Search for a node\n");
    printf("4. Insert after a node\n");
    printf("5. Insert before a node\n");
    printf("6. Remove front node\n");
    printf("7. Remove back node\n");
    printf("8. Remove any node\n");
    printf("9. Sort the list\n");
    printf("10. Reverse the linked list\n");
    printf("11. Remove duplicates with buffer\n");
    printf("12. Remove duplicates without buffer\n");
    printf("13. Create hash table\n");
    printf("14. Search hash table\n");
    printf("15. Find kth to last node in linked list\n");
    printf("16. Partition list by value\n");
    printf("17. Push to stack\n");
    printf("18. Pop top of stack\n");
    printf("19. Peek top of stack\n");
    printf("20. Check if linked list is a palindrome\n");
    printf("21. Sort stack using another stack\n");
    printf("-1. Quit\n");

    return;
} // end of Menu function
