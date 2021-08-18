# ERROR DO ESCOPO EX:
```c#
int main(){
    string nome(){
        string s = "Ola"
    }
    print(s)
}
```

>>> ESSE CODIGO ACIMA TE QUE DA UM ERROR POIS OS A STRING "S" NÃO ESTA NO ESCOPO GLOBAL DA FUNCÃO