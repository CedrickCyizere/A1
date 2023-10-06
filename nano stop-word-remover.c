#include <stdio.h>
#include<string.h>
#include <stdbool.h>

char *stop_words[]={"the"."a","an","for","to","and","but","yet"};

int num_stop_words=sizeof(stop_words) / sizeof(char*);

//to check if a word is a stop word 

bool is_stop_word(char *word){
    for(int i=0;i < num_stop_words;i++)
    {
        if(strcmp(word, stop_words[i]==0))
        {
            return true;
        }
    }
    return false;
}

int main() 
{
    char line [1000];

    while (fgets(line, sizeof(line),stdin))
    {
        char *word=strok(line, " \n");


        while(word !=NULL)
        {
            if(!is_stop_word(word))
            
            {
                printf("%s",word);
            }
            word=strtok(NULL, " \n");
        }
        printf("\n");
    }
    return 0;
}