#include<stdio.h>
#include<stdlib.h>

#define DATA NULL

typedef struct Arbre
{
    int val;
    struct Arbre *left;
    struct Arbre *right;
}Arbre;

typedef Arbre* Typedata;

typedef struct Node
{
    Typedata data;
    struct Node *next;
}Node;

typedef struct File
{
    Node *start;
    Node *end;
}File;

void enfiler(File** fil, Typedata x)
{
    if(*fil == NULL)
    {
        *fil = malloc(sizeof(File));
        (*fil)->start = malloc(sizeof(Node));
        (*fil)->start->data = x;
        (*fil)->start->next = NULL;
        (*fil)->end = (*fil)->start;
    }else{
        Node* new = malloc(sizeof(Node));
        new->data = x;
        new->next=NULL;
        (*fil)->end->next = new;
        (*fil)->end = new;
    }
}

Typedata defiler(File** fil)
{
    if((*fil)->start == NULL)return DATA;
    Node* sup = (*fil)->start;
    (*fil)->start = sup->next;
    Typedata d = sup->data;
    free(sup);
    if((*fil)->start == NULL)*fil = NULL;
    return d;
}

void afficher(File* fil)
{
    Node* n = fil->start;
    while(n != NULL)
    {
        printf("%d", n->data);
        n = n->next;
    }
}

typedef struct Pile{
	Typedata data;
	struct Pile *next;
}Pile;

void empiler(Pile **pil, Typedata data)
{
	Pile* p = (Pile*)malloc(sizeof(Pile));
	p->data = data;
	p->next = *pil;
	*pil = p;
}

Typedata depiler(Pile** pil)
{
	Pile *p = (*pil)->next;
	Typedata x = (*pil)->data;
	free(*pil);
	*pil = p;
	return x;
}
