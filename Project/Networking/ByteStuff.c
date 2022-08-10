#include<stdio.h>             
#include<string.h>         
main(){
        char a[20],b[20];
        int i,n,j;
        char f,s;
        printf("Enter the size of the frame : ");
        scanf("%d",&n);
        n=n*2;
        printf("\nEnter the characters in frame : \n");
        for(i=0;i<n;i++)
                scanf("%c",&a[i]);
        printf("\n FRAME \n ");
        for(i=0;i<n;i++)
                printf("%c",a[i]);
        j=0;
        for(i=0;i<n;i++)
        {
                if(a[i]=='f')
                {
                        b[j]='s';
                        j++;
                        b[j]=a[i];

                }
                else if(a[i]=='s')
                {
                        b[j]='s';
                        j++;
                        b[j]=a[i];
                }
                else
                        b[j]=a[i];

                j++;
        }
        printf("\n RESULT \n");
        printf("f");
        for(i=0;i<j;i++)
        {
                printf("\n");
                printf("%c",b[i]);
        }
        printf("\nf");
}
