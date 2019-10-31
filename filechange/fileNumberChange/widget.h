#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QFileSystemWatcher>
#include <QDir>
#include <QtDebug>


namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();
        QFileSystemWatcher myWatcher;
private slots:
    void showMessage(const QString &path);

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
