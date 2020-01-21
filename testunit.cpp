#include <iostream>
#include <unistd.h>
#include <stdlib.h>
using namespace std;
int main(int argc,char** argv){
        if(argc>1){
//              int num=argv[1]-'0';
                char *str=argv[1];
                int num=atoi(str);
                cout<<"parameters is "<<num<<endl;
        }else{
                cout<<"missing parameters!"<<endl;
        }
        return 0;
}