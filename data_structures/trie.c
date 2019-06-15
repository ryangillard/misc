#include <stdio.h>      /* printf, scanf, puts */
#include <stdlib.h>     /* realloc, free, exit, NULL */

// gcc trie.c -o trie -g
// valgrind --leak-check=full --show-leak-kinds=all -v ./trie

const int ALPHABET_SIZE = 26;

/*********************************************************************************/
/********************************** STRUCTURES ***********************************/
/*********************************************************************************/

typedef struct TrieNode
{
	int* value;
	struct TrieNode* TrieNodes[26];
} TrieNode;

typedef struct Trie
{
	TrieNode* root;
} Trie;

/*********************************************************************************/
/********************************** PROTOTYPES ***********************************/
/*********************************************************************************/

/* This function creates a trie */
Trie* CreateTrie(Trie* trie);

/* This function creates a trie node */
TrieNode* CreateTrieNode();

/* This function inserts a new word into a trie */
Trie* InsertWordTrie(Trie* trie, char* word, int* value);

/* This function searches for a word in a trie */
int SearchWordTrie(Trie* trie, char* word);

/* This function deletes a word from a trie */
Trie* DeleteWordTrie(Trie* trie, char* word);

/*********************************************************************************/
/************************************* MAIN **************************************/
/*********************************************************************************/

int main(int argc, char* argv[])
{
	printf("c - a = %d\n", 'c' - 'a');

	char word[100] = {"test"};
	int value = 1234;

	Trie* trie = NULL;

	trie = InsertWordTrie(trie, word, &value);

	int found_word = 0;
	found_word = SearchWordTrie(trie, word);
	if (found_word == 1)
	{
		printf("main: Found word %s in trie\n", word);
	}

	char word2[100] = {"tee"};
	found_word = SearchWordTrie(trie, word2);
	if (found_word == 1)
	{
		printf("main: Found word %s in trie\n", word2);
	}

	char word3[100] = {"te"};
	found_word = SearchWordTrie(trie, word3);
	if (found_word == 1)
	{
		printf("main: Found word %s in trie\n", word3);
	}
} // end of main

/*********************************************************************************/
/*********************************** FUNCTIONS ***********************************/
/*********************************************************************************/

/* This function creates a trie */
Trie* CreateTrie(Trie* trie)
{
	if (trie == NULL)
	{
		printf("CreateTrie: Making singly linked list!\n");
		trie = (Trie*)malloc(sizeof(Trie) * 1);
		if (trie == NULL)
		{
			printf("CreateTrie: Error: Unable to make trie!\n");
			exit(0);
		}

		trie->root = NULL;
		return trie;
	}

	printf("CreateTrie: No need to create trie since it already exists!\n");

	return trie;
} // end of CreateTrie function

/* This function creates a trie node */
TrieNode* CreateTrieNode()
{
	TrieNode* new_node = (TrieNode*)malloc(sizeof(TrieNode));
    if (new_node == NULL)
    {
        printf("CreateTrieNode: Error: Unable to create a new node.\n");
        exit(0);
    }

    new_node->value = NULL;

    unsigned int i;
    for (i = 0; i < ALPHABET_SIZE; i++)
    {
        new_node->TrieNodes[i] = NULL;
    } // end of i loop

    return new_node;
} // end of CreateTrieNode function

/* This function inserts a new word into a trie */
Trie* InsertWordTrie(Trie* trie, char* word, int* value)
{
	if (trie == NULL)
	{
		printf("InsertWordTrie: trie doesn't exist!\n");
		trie = CreateTrie(trie);
	}

	if (trie->root == NULL)
	{
		printf("InsertWordTrie: root doesn't exist!\n");
		trie->root = CreateTrieNode();
	}

	if (word[0] == '\0')
	{
		printf("InsertWordTrie: null word!\n");
		return trie;
	}

	TrieNode* cursor = trie->root;

	unsigned int word_length = 0;
	while (word[word_length] != '\0')
	{
		word_length++;
	}

	printf("InsertWordTrie: Word is %s with length %u\n", word, word_length);

	unsigned int i;
	int character_index;
	for (i = 0; i < word_length; i++)
	{
		character_index = word[i] - 'a';

		if (cursor->TrieNodes[character_index] == NULL)
		{
			printf("InsertWordTrie: Creating new node at character_index %d\n", character_index);
			cursor->TrieNodes[character_index] = CreateTrieNode();
		}

		cursor = cursor->TrieNodes[character_index];
	} // end of i loop

	cursor->value = value;

	return trie;
} // end of InsertWordTrie function

/* This function searches for a word in a trie */
int SearchWordTrie(Trie* trie, char* word)
{
	if (trie == NULL)
	{
		printf("SearchWordTrie: trie doesn't exist!\n");
		return 0;
	}

	if (trie->root == NULL)
	{
		printf("SearchWordTrie: root doesn't exist!\n");
		return 0;
	}

	if (word[0] == '\0')
	{
		printf("SearchWordTrie: null word!\n");
		return 0;
	}

	TrieNode* cursor = trie->root;

	unsigned int word_length = 0;
	while (word[word_length] != '\0')
	{
		word_length++;
	}

	printf("SearchWordTrie: Word is %s with length %u\n", word, word_length);

	int i, j;
	int character_index;
	for (i = 0; i < word_length; i++)
	{
		character_index = word[i] - 'a';

		if (cursor->TrieNodes[character_index] == NULL)
		{
			printf("SearchWordTrie: No node at character_index %d. Word doesn't exist in trie\n", character_index);
			return 0;
		}

		cursor = cursor->TrieNodes[character_index];
	} // end of i loop

	if (cursor->value == NULL)
	{
		printf("SearchWordTrie: Found word NOT at leaf!\n");
	}
	else
	{
		printf("SearchWordTrie: Found word at leaf with value = %d!\n", (*cursor->value));
	}

	return 1;
} // end of SearchWordTrie function

/* This function deletes a word from a trie */
Trie* DeleteWordTrie(Trie* trie, char* word)
{
	if (trie == NULL)
	{
		printf("DeleteWordTrie: trie doesn't exist!\n");
		return trie;
	}

	if (trie->root == NULL)
	{
		printf("DeleteWordTrie: root doesn't exist!\n");
		return trie;
	}

	if (word[0] == '\0')
	{
		printf("DeleteWordTrie: null word!\n");
		return trie;
	}

	TrieNode* cursor = trie->root;

	unsigned int word_length = 0;
	while (word[word_length] != '\0')
	{
		word_length++;
	}

	printf("DeleteWordTrie: Word is %s with length %u\n", word, word_length);

	int i, j;
	int character_index;
	for (i = 0; i < word_length; i++)
	{
		character_index = word[i] - 'a';

		if (cursor->TrieNodes[character_index] == NULL)
		{
			printf("DeleteWordTrie: No node at character_index %d. Word doesn't exist in trie\n", character_index);
			return trie;
		}

		cursor = cursor->TrieNodes[character_index];
	} // end of i loop

	/* If we made it this far we have found the word */
	cursor->value = NULL;

	/* Work backwards up the word */
	int found_pointers;
	for (i = word_length - 1; i >= 0; i--)
	{
		found_pointers = 0;
		for (j = 0; j < ALPHABET_SIZE; j++)
		{
			if (cursor->TrieNodes[j] != NULL)
			{
				found_pointers = 1;
				break;
			}
		} // end of j loop

		if (found_pointers == 0)
		{
//			cursor->TrieNodes[j];
		}
	} // end of i loop

	return trie;
} // end of DeleteWordTrie function
