#include "login.h"
#include "messanger_page.h"
#include "ui_login.h"
#include "userclass.h"
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <iostream>
#include <QJsonDocument>
#include <QJsonObject>
#include <QFile>
#include <QTextStream>
#include "messanger_list.h"

using namespace std;

userClass Login::user;

Login::Login(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Login)
{
    ui->setupUi(this);

    network_manager = new QNetworkAccessManager(this);

    connect (network_manager , &QNetworkAccessManager :: finished , this , [&](QNetworkReply * reply)
    {
        data_str = reply -> readAll();
        data_doc = QJsonDocument::fromJson(data_str.toUtf8());
        data_obj = data_doc.object();

        error_code = data_obj["code"].toString();
        user.setToken(data_obj["token"].toString());
        ui->responseLabel->setText (data_obj["message"].toString()+"    "+error_code);

        qDebug() << data_obj;

        qDebug() << user .getUsername();
        qDebug() << user .getPassword();
        qDebug() << user .getToken();


         if ( error_code == "200" )
        {

            this -> hide();
            messanger_list *m_list = new messanger_list ;
            m_list->show();
        }
    });
}

Login::~Login()
{
    delete ui;
}


void Login::on_pbn_login_clicked()
{
    user .setUsername(ui -> userLineEdit -> text ());
    user .setPassword(ui -> passLineEdit -> text ());
    network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/login?username=" + user.getUsername() + "&password=" + user.getPassword() )));
//    if ( user .getToken()=="" )
//    {
//        network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/logout?username=" + Login::user . getUsername() + "&password=" + Login::user . getPassword() )));
//    }
}

void Login::on_pbn_signup_clicked()
{
    this -> hide ();

    SignUp signup;

    signup . setModal (true);

    signup . exec();
}

