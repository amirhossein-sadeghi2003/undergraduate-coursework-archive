#include "login.h"
#include "signup.h"
#include "ui_signup.h"
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
SignUp::SignUp(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SignUp)
{
    ui->setupUi(this);
    network_manager = new QNetworkAccessManager(this);

    connect (network_manager , &QNetworkAccessManager :: finished , this , [&](QNetworkReply * reply)
    {
        data_str = reply -> readAll();
        data_doc = QJsonDocument::fromJson(data_str.toUtf8());
        data_obj = data_doc.object();

        error_code = data_obj["code"].toString();
        ui->lbl_respond->setText (data_obj["message"].toString()+"\nCode: "+error_code);

        if ( error_code == "200" )
        {
            this -> hide();

            Login *login = new Login ;

            login->show();
        }
    });
}

SignUp::~SignUp()
{
    delete ui;
}

void SignUp::on_pushButton_clicked()
{
    network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/signup?username=" + ( ui -> le_user_name_2 -> text ()) + "&password=" + ( ui -> le_pass -> text ()) )));

}

