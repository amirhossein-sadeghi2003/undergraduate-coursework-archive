#ifndef LOGIN_H
#define LOGIN_H

#include <QMainWindow>
#include "signup.h"
#include <QJsonDocument>
#include <QJsonObject>
#include "userclass.h"
using namespace std;

QT_BEGIN_NAMESPACE
namespace Ui { class Login; }
QT_END_NAMESPACE

class QNetworkAccessManager;

class Login : public QMainWindow
{
    Q_OBJECT

public:
    Login(QWidget *parent = nullptr);
    ~Login();

    static userClass user;

private slots:
    void on_pbn_login_clicked();

    void on_pbn_signup_clicked();

private:
    Ui::Login *ui;

    QNetworkAccessManager * network_manager;

    QByteArray data;
    QString data_str;
    QJsonDocument data_doc;
    QJsonObject data_obj;
    QString error_code;



};
#endif // LOGIN_H
