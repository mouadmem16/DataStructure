#include "file.c"

Arbre* creer(Arbre* filsG, Arbre* filsD, int x)
{
    Arbre* ar = (Arbre*)malloc(sizeof(Arbre));
    ar->left = filsG;
    ar->right = filsD;
    ar->val = x;
    return ar;
}

void creerRech(Arbre** bt, Arbre* fils)
{
    if(*bt == NULL){*bt=fils;}
    else if((*bt)->val > fils->val){
        creerRech(&(*bt)->left, fils);
    }else if((*bt)->val < fils->val){
        creerRech(&(*bt)->right, fils);
    }
}

void ParcourLargeur(Arbre *ar)
{
    File *fil=NULL;
    enfiler(&fil, ar);
    while(fil != NULL)
    {
        ar = defiler(&fil);
        printf("%d ", ar->val);
        if(ar->left != NULL)
            enfiler(&fil, ar->left);
        if(ar->right != NULL)
            enfiler(&fil, ar->right);
    }
}

void prefixeIteratif(Arbre* ar)
{
    Pile* pil = NULL;
    empiler(&pil, ar);
    while(pil != NULL)
    {
        ar = depiler(&pil);
        if(ar->left != NULL || ar->right != NULL){
            if(ar->right != NULL)empiler(&pil, ar->right);
            if(ar->left != NULL)empiler(&pil, ar->left);
            empiler(&pil, creer(NULL, NULL, ar->val));
        }else if(ar->left == NULL){
            printf("%d ", ar->val);
        }
    }
}

void infixeIteratif(Arbre* ar)
{
    Pile* pil = NULL;
    empiler(&pil, ar);
    while(pil != NULL)
    {
        ar = depiler(&pil);
        if(ar->left != NULL || ar->right != NULL){
            if(ar->right != NULL)empiler(&pil, ar->right);
            empiler(&pil, creer(NULL, NULL, ar->val));
            if(ar->left != NULL)empiler(&pil, ar->left);
        }else if(ar->left == NULL){
            printf("%d ", ar->val);
        }
    }
}

void postfixeIteratif(Arbre* ar)
{
    Pile* pil = NULL;
    empiler(&pil, ar);
    while(pil != NULL)
    {
        ar = depiler(&pil);
        if(ar->left != NULL || ar->right != NULL){
            empiler(&pil, creer(NULL, NULL, ar->val));
            if(ar->right != NULL)empiler(&pil, ar->right);
            if(ar->left != NULL)empiler(&pil, ar->left);
        }else if(ar->left == NULL){
            printf("%d ", ar->val);
        }
    }
}

int main()
{
    Arbre* bt=NULL;
    creerRech(&bt, creer(NULL, NULL, 5));
    creerRech(&bt, creer(NULL, NULL, 7));
    creerRech(&bt, creer(NULL, NULL, 3));
    creerRech(&bt, creer(NULL, NULL, 2));
    creerRech(&bt, creer(NULL, NULL, 4));
    creerRech(&bt, creer(NULL, NULL, 6));
    creerRech(&bt, creer(NULL, NULL, 8));
    creerRech(&bt, creer(NULL, NULL, 9));
    creerRech(&bt, creer(NULL, NULL, 10));
    creerRech(&bt, creer(NULL, NULL, 1));

    printf("prefixe: ");prefixeIteratif(bt);
    printf("\ninfixe: ");infixeIteratif(bt);
    printf("\npostfixe: ");postfixeIteratif(bt);
    return 0;
}



