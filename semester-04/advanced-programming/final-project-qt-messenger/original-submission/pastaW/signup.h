#ifndef SIGNUP_H
#define SIGNUP_H

#include <QDialog>
#include <QJsonDocument>
#include <QJsonObject>

class QNetworkAccessManager;
namespace Ui {
class SignUp;
}

class SignUp : public QDialog
{
    Q_OBJECT

public:
    explicit SignUp(QWidget *parent = nullptr);
    ~SignUp();

private slots:
    void on_pushButton_clicked();

private:
    Ui::SignUp *ui;
    QNetworkAccessManager* network_manager;

    QByteArray data;
    QString data_str;
    QJsonDocument data_doc;
    QJsonObject data_obj;
    QString error_code;
};

#endif // SIGNUP_H
