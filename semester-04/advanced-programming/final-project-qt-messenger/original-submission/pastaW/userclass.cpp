#include "userclass.h"

userClass::userClass()
{

}
QString userClass::getUsername()
{
    return username;
}
QString userClass::getPassword()
{
    return password;
}
QString userClass::getToken()
{
    return token;
}

void userClass::setUsername(QString u)
{
    username = u;
}
void userClass::setPassword(QString p)
{
    password = p;
}
void userClass::setToken(QString t)
{
    token = t;
}
