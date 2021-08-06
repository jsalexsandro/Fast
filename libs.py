########################################
# Lins for "Fast" Language !           #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################


print_fast = [["<iostream>"],r"""template <class print_template>
print_template print(print_template values){
std::cout << values << std::endl;
};
"""]


types_fast = [["<iostream>","<typeinfo>"],
r"""template <typename any>
char * type(any value){
const char * __type_return;
if (*(typeid(value).name()) == 'i' || *(typeid(value).name()) == 'l' || *(typeid(value).name()) == 'x'){
__type_return = "int";
} else if (*(typeid(value).name()) == 'P'){
__type_return = "string";
} else if (*(typeid(value).name()) == 'b'){
__type_return = "bool";
} else if (*(typeid(value).name()) == 'f' || *(typeid(value).name()) == 'd' || *(typeid(value).name()) == 'e'){
__type_return = "float";
} else {
std::cout << typeid(value).name() << std::endl;
}
return (char *)__type_return;
}
"""
]