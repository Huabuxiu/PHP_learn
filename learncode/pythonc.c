#include <stdio.h>    
#include<stdlib.h>   
#include<string.h>  
extern "C"    
{    
    char* itype(int b)    
    {   
        char*   s   = (char*)malloc(100   );   
        sprintf(s,"%d",b);  
        return s;  
    }    
    char* ftype(float b)    
    {   
        char*   s = (char*)malloc(100  );   
          
        sprintf(s,"%f",b);  
              
        return s;  
    }  
    char* stype(char* b)    
    {   
        char*   s   =   (char*)malloc(100 );   
        if (s)   
           strcpy   (   s   ,   b  );   
        return  s;   
    }     
        
} 