#include "login.h"
#include "messanger_page.h"
#include "ui_messanger_page.h"
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <iostream>
#include <QJsonDocument>
#include <QJsonObject>
#include "userclass.h"
#include "sstream"
#include "contact.h"
#include "messanger_list.h"
#include <fstream>
#include <string>

messanger_page::messanger_page(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::messanger_page)
{
    ui->setupUi(this);

    network_manager = new QNetworkAccessManager(this);

    connect (network_manager , &QNetworkAccessManager :: finished , this , [&](QNetworkReply * reply)
    {
        data_str = reply -> readAll();
        data_doc = QJsonDocument::fromJson(data_str.toUtf8());
        data_obj = data_doc.object();

        error_code = data_obj["code"].toString();

        qDebug() << error_code;

        switch (command)
        {

        case 1:
            if ( error_code == "200" )
            {
                ui -> le_message -> setText("");
            }
            command = 10;
            break;

        case 2:
            all_messages = "" ;
            if ( error_code == "200")
            {
                QString message = data_obj["message"].toString();
                QString m_nums = "";
                int num;

                for (int i = 0 ; i < message . length(); i++ )
                {
                    if (message[i].isDigit())
                        m_nums += message[i];
                }

                num = m_nums . toInt();

                for ( int i = 0 ; i < num ; i++ )
                {
                    QString n = QString::fromStdString("block ") + QString::number(i);
                    QJsonObject line_obj = data_obj[n].toObject();
                    QString line = line_obj["src"].toString() + ": " + line_obj["body"].toString();
                    all_messages += ( line + "\n" );
                }
                ui -> tb_messages -> setText(all_messages);
                    if(messanger_list::my_contact.get_type() == 0){
                        fstream file;
                        string name_user_for_file = messanger_list::my_contact.get_dst().toStdString();
                        name_user_for_file.c_str();
                        string text_for_file = all_messages.toStdString();
                        text_for_file.c_str();
                        file.open(name_user_for_file, ios:: out);
                        file << text_for_file;
                        file << "------------------------";
                        file.close();
                    }
                    else if(messanger_list::my_contact.get_type() == 1){
                        fstream file;
                        string name_group_for_file = messanger_list::my_contact.get_dst().toStdString();
                        name_group_for_file.c_str();
                        string text_for_file = all_messages.toStdString();
                        text_for_file.c_str();
                        file.open(name_group_for_file, ios:: out);
                        file << text_for_file;
                        file << "------------------------";
                        file.close();
                    }
                    else if(messanger_list::my_contact.get_type() == 2){
                        fstream file;
                        string name_channel_for_file = messanger_list::my_contact.get_dst().toStdString();
                        name_channel_for_file.c_str();
                        string text_for_file = all_messages.toStdString();
                        text_for_file.c_str();
                        file.open(name_channel_for_file, ios:: out);
                        file << text_for_file;
                        file << "------------------------";
                        file.close();
                    }

            }
            command = 10;

            break;
        }
     });
}
messanger_page::~messanger_page()
{
    delete ui;
}

void messanger_page::on_pb_send_clicked()
{
    destination = messanger_list::my_contact.get_dst();
    type = messanger_list::my_contact.get_type();
    body = ui -> le_message -> text();
    switch(type){
        case 0:
            network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/sendmessageuser?token=" + Login::user . getToken() + "&dst=" + destination + "&body=" + body )));
        break;
        case 1:
            network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/sendmessagegroup?token=" + Login::user . getToken() + "&dst=" + destination + "&body=" + body )));
        break;
        case 2:
            network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/sendmessagechannel?token=" + Login::user . getToken() + "&dst=" + destination + "&body=" + body )));
        break;
    }
    command = 1;
}
void messanger_page::on_pb_recieve_clicked()
{
    command = 2;
    destination = messanger_list::my_contact.get_dst();
    type = messanger_list::my_contact.get_type();
    body = ui -> le_message -> text();
    switch(type){
        case 0:
            network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/getuserchats?token=" + Login::user . getToken() + "&dst=" + destination)));
        break;
        case 1:
            network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/getgroupchats?token=" + Login::user . getToken() + "&dst=" + destination )));
        break;
        case 2:
            network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/getchannelchats?token=" + Login::user . getToken() + "&dst=" + destination)));
        break;
    }



    command = 2;
}


void messanger_page::on_pb_back_clicked()
{
    command = 0;
    this -> hide();
    messanger_list *m_list = new messanger_list ;
    m_list->show();
}

