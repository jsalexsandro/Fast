/*
 * helloworld.fast
 * Code Generated by Fast lang
 * Version language: (0.0.1)
 * Monday 2021-08-30 21:41:45.226198
*/

#include <iostream>
#include <locale.h>

char ** argv;

/*
 * Write in Terminal
*/
std::string print(){std::cout<<'\n';}
template<typename T, typename ...ARGV>
std::string print(T value, ARGV... values){
std::cout<<value<<" ";
print(values...);
return "null";
}

long helloworld(){
print(std::string("Ol�, Mundo!"));
}

int main(int _argc,char * _argv[]){
setlocale(LC_ALL,"");
argv = _argv;
helloworld();
return 0;
};