#ifndef MESSANGER_LIST_H
#define MESSANGER_LIST_H

#include "contact.h"
#include <QDialog>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <iostream>
#include <QJsonDocument>
#include <QJsonObject>

namespace Ui {
class messanger_list;
}

class messanger_list : public QDialog
{
    Q_OBJECT

public:
    explicit messanger_list(QWidget *parent = nullptr);
    ~messanger_list();
    static contact my_contact;

private slots:
    void on_tw_tabBarClicked(int index);

    void on_pbn_out_clicked();

    void on_pbn_open_chat_clicked();

    void on_pbn_create_group_clicked();

    void on_pbn_createchannel_clicked();

    void on_pbn_join_group_clicked();

    void on_pbn_join_channel_clicked();

private:
    Ui::messanger_list *ui;
    QByteArray data;
    QString data_str;
    QJsonDocument data_doc;
    QJsonObject data_obj;
    QString error_code;
    QNetworkAccessManager* network_manager;
    int command;
    QString all_contacts;

};

#endif // MESSANGER_LIST_H
