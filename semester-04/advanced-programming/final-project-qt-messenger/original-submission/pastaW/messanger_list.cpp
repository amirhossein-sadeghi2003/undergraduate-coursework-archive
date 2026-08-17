#include "messanger_list.h"
#include "messanger_page.h"
#include "ui_messanger_list.h"
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <iostream>
#include <QJsonDocument>
#include <QJsonObject>
#include "login.h"
contact messanger_list::my_contact;
messanger_list::messanger_list(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::messanger_list)
{
    ui->setupUi(this);
    network_manager = new QNetworkAccessManager(this);
    connect (network_manager , &QNetworkAccessManager :: finished , this , [&](QNetworkReply * reply)
        {
            data_str = reply -> readAll();
            data_doc = QJsonDocument::fromJson(data_str.toUtf8());
            data_obj = data_doc.object();

            error_code = data_obj["code"].toString();
            all_contacts = "" ;
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
                    QString line = line_obj["src"].toString();
                    all_contacts += ( line + "\n" );
                }
            switch (command)
            {
                    case 0:
                        if ( error_code == "200" )
                        {
                            this -> hide();
                            Login *login = new Login ;
                            login->show();
                        }
                        command = 10;
                        break;
                    case 1:
                        for ( int i = 0 ; i < num ; i++ )
                            {
                            QString n = QString::fromStdString("block ") + QString::number(i);
                            QJsonObject line_obj = data_obj[n].toObject();
                            QString line = line_obj["src"].toString();
                            all_contacts += ( line + "\n" );
                            }
                        ui -> tb_user -> setText(all_contacts);
                        break;
                    case 2:
                        for ( int i = 0 ; i < num ; i++ )
                        {
                            QString n = QString::fromStdString("block ") + QString::number(i);
                            QJsonObject line_obj = data_obj[n].toObject();
                            QString line = line_obj["group_name"].toString();
                            all_contacts += ( line + "\n" );
                        }
                        ui -> tb_group -> setText(all_contacts);
                        break;
                    case 3:
                        for ( int i = 0 ; i < num ; i++ )
                        {
                            QString n = QString::fromStdString("block ") + QString::number(i);
                            QJsonObject line_obj = data_obj[n].toObject();
                            QString line = line_obj["channel_name"].toString();
                            all_contacts += ( line + "\n" );
                        }
                        ui -> tb_channel -> setText(all_contacts);
                        break;
            }

                        }
            qDebug() << data_str;
         });

}

messanger_list::~messanger_list()
{
    delete ui;
}

void messanger_list::on_tw_tabBarClicked(int index)
{
    switch(index){
    case 0:
        command = 1;
        network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/getuserlist?token=" + Login::user . getToken() )));

        my_contact.set_type(0);
        break;
    case 1:
        command = 2;
        network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/getgrouplist?token=" + Login::user . getToken() )));
        my_contact.set_type(1);
        break;
    case 2:
        command = 3;
        network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/getchannellist?token=" + Login::user . getToken() )));
        my_contact.set_type(2);
        break;

    }

}


void messanger_list::on_pbn_out_clicked()
{
    network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/logout?username=" + Login::user . getUsername() + "&password=" + Login::user . getPassword() )));
    command = 0;
}


void messanger_list::on_pbn_open_chat_clicked()
{
    my_contact.set_dst(ui->le_choose->text());
    this -> hide();
    messanger_page *m_page = new messanger_page ;
    m_page->show();
}


void messanger_list::on_pbn_create_group_clicked()
{
    command = 10;
    my_contact.set_dst(ui->le_name->text());
    my_contact.set_type(1);
    network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/creategroup?token=" + Login::user . getToken()+ "&group_name=" + my_contact.get_dst() )));
    if(error_code == "200"){
    this -> hide();
    messanger_page *m_page = new messanger_page ;
    m_page->show();
    }
}


void messanger_list::on_pbn_createchannel_clicked()
{
    my_contact.set_dst(ui->le_name->text());
    my_contact.set_type(2);
    network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/createchannel?token=" + Login::user . getToken()+ "&channel_name=" + my_contact.get_dst() )));
    if(error_code == "200"){
    this -> hide();
    messanger_page *m_page = new messanger_page ;
    m_page->show();
    }
}


void messanger_list::on_pbn_join_group_clicked()
{
    command = 10;
    my_contact.set_dst(ui->le_name->text());
    my_contact.set_type(1);
    network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/joingroup?token=" + Login::user . getToken()+ "&group_name=" + my_contact.get_dst() )));
    if(error_code == "200"){
        this -> hide();
        messanger_page *m_page = new messanger_page;
        m_page->show();
    }
}


void messanger_list::on_pbn_join_channel_clicked()
{
    command = 10;
    my_contact.set_dst(ui->le_name->text());
    my_contact.set_type(2);
    network_manager -> get (QNetworkRequest ( QUrl( "http://api.barafardayebehtar.ml:8080/joinchannel?token=" + Login::user . getToken()+ "&channel_name=" + my_contact.get_dst() )));
    qDebug() << error_code;
    if(error_code == "200"){
        this -> hide();
        messanger_page *m_page = new messanger_page;
        m_page->show();
    }
}

