/*
 * scopeTest.fast
 * Code Generated by Fast lang
 * Version language: (0.0.1)
 * Wednesday 2021-08-18 17:29:26.165319
*/

#include <locale.h>
#include <iostream>

char ** argv;

/*
 * Write in Terminal
*/
template <class printT>
std::string print(printT values){
std::cout << values << std::endl;
return "null";
};

long test(){
long number=10;
};
long scopeTest(){
long number=10;
print(number);
}

int main(int _argc,char * _argv[]){
setlocale(LC_ALL,"");
argv = _argv;
scopeTest();
return 0;
};