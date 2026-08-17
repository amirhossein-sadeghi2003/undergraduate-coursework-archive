#include "contact.h"

contact::contact()
{

}
QString contact::get_dst(){
    return destination;
}

int contact::get_type(){
    return type;
}
void contact::set_dst(QString my_dst){
    destination = my_dst;
}
void contact::set_type(int type){
    this -> type = type;
}
