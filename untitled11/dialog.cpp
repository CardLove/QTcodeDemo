#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
}
void Dialog::setLabelText(const QString text)
{
    ui->label->setText(text);
}

Dialog::~Dialog()
{
    delete ui;
}
