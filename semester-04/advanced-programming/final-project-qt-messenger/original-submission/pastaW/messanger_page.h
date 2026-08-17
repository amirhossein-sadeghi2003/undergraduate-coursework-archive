#ifndef MESSANGER_PAGE_H
#define MESSANGER_PAGE_H

#include "login.h"
#include <QDialog>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QNetworkRequest>
#include <iostream>
#include <QJsonDocument>
#include <QJsonObject>

namespace Ui {
class messanger_page;
}

class messanger_page : public QDialog
{
    Q_OBJECT

public:
    explicit messanger_page(QWidget *parent = nullptr);
    ~messanger_page();

private slots:
    void on_pb_logout_clicked();

    void on_pb_send_clicked();

    void on_pb_recieve_clicked();

    void on_pb_back_clicked();

private:
    Ui::messanger_page *ui;

    QNetworkAccessManager * network_manager;

    QByteArray data;
    QString data_str;
    QJsonDocument data_doc;
    QJsonObject data_obj;
    QString error_code;
    QString destination;
    QString body;
    int command;
    QString all_messages;
    int type;
};

#endif // MESSANGER_PAGE_H
