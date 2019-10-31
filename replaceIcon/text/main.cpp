#include <QSqlDatabase>
#include <QtDebug>
#include <QSqlQuery>
#include <QSqlError>
#include <QSqlRecord>
#include <string.h>
#include <iostream>
using namespace std;


int  main()
{
//创建数据库
QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE", "sqlite1");
db.setHostName("acidalia");
db.setDatabaseName("customdb");
db.setUserName("root");
db.setPassword("123456");
if( !db.open())
{
   qDebug() << "db.open failed.";
}

//创建表
db = QSqlDatabase::database("sqlite1"); //建立数据库连接
QSqlQuery query(db);
bool success = query.exec("create table automobil(id int, name varchar)");
if(success)
{
    qDebug() << QObject::tr("create table success.");
}
else
{
    qDebug() << QObject::tr("create table failed.");
}

//插入记录
for(int i = 0; i < 10; i++)
{
    query.prepare("INSERT INTO automobil (id, name) "
                      "VALUES (:id, :name)");
    query.bindValue(":id", i);
    query.bindValue(":name", "furong");
    if(!query.exec())
    {
        QSqlError lastError = query.lastError();
        qDebug() << lastError.driverText() << QString(QObject::tr("INSERT failed."));
    }
}

////查询记录
//int id = 2;
//query.exec("select * from automobil where id = '" + id + "'");
//QSqlRecord rec = query.record();
//qDebug() << QObject::tr("automobil table count:" ) << rec.count();
//while(query.next())
//{
//    for(int i = 0; i < rec.count(); i++)
//        qDebug() << query.value(i);
//}

////更新记录
//string name = "sd";
//query.prepare(QString("update automobil set name = \"quange\",name = '" + name + "' where id = %1").arg(9));
//if(!query.exec())
//{
//    QSqlError lastError = query.lastError();
//    qDebug() << lastError.driverText() << QString(QObject::tr("update failed."));
//}

////删除记录
//query.prepare(QString("delete from automobil where id = %1").arg(2));
//if(!query.exec())
//{
//    qDebug() << "delete failed.";
//}
return  0;

}
