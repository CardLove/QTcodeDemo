#include "widget.h"
#include "ui_widget.h"


Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    connect(&myWatcher, SIGNAL(directoryChanged(QString)), this, SLOT(showMessage(QString)));
    connect(&myWatcher, SIGNAL(fileChanged(QString)), this, SLOT(showMessage(QString)));


    // 显示出当前目录下的所有.h文件
    QDir myDir(QDir::currentPath());
    myDir.setNameFilters(QStringList("*.h"));



    // 创建目录，并将其加入到监视器中
    myDir.mkdir("mydir");
    myDir.cd("mydir");

    myWatcher.addPath(myDir.absolutePath());
    // 创建文件，并将其加入到监视器中
    QFile file(myDir.absolutePath() + "/myfile.txt");
    if (file.open(QIODevice::WriteOnly)) {
        QFileInfo info(file);
        myWatcher.addPath(info.absoluteFilePath());
        file.close();
    }
}

void Widget::showMessage(const QString &path)
{
    static int i = 0;
    QDir dir(QDir::currentPath() + "/mydir");
    // 如果是目录发生了改变
    if (path == dir.absolutePath()) {
        qDebug() <<i<< " 目录发生了改变" << path <<  endl;
        i++;

    } else { // 如果是文件发生了改变

        qDebug() << i<<" 文件发生了改变"<< path << endl;
        i++;
    }

    dirnum = 0
    filenum = 0
    path = 'C:/Users/Dell/Desktop/test'




    qDebug() << "文件个数：" << filenum << endl;
}

Widget::~Widget()
{
    delete ui;
}
