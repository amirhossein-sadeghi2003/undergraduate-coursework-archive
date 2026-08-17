#ifndef USERCLASS_H
#define USERCLASS_H
#include <QMainWindow>

class userClass
{
    public:
        userClass();
        QString status;
        QString getUsername();
        QString getPassword();
        QString getToken();

        void setUsername(QString u);
        void setPassword(QString p);
        void setToken(QString t);
    private:
        QString username;
        QString password;
        QString token;

};

#endif // USERCLASS_H
