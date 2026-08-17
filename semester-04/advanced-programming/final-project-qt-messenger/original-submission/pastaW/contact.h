#ifndef CONTACT_H
#define CONTACT_H
#include <QMainWindow>

class contact
{
public:
    contact();
    QString get_dst();
    int get_type();
    void set_dst(QString);
    void set_type(int);
private:
    QString destination;
    int type;
};

#endif // CONTACT_H
