#include <QCoreApplication>
#include <iostream>
using namespace std;
#include <vector>
#include <string>
#include <algorithm>

#include <QDateTime>
#include <QTimer>
#include <qdebug.h>


bool cmp1(const vector<int> &a, const vector<int> &b)
{
    return a[0] > b[0];
}


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    vector<vector<int>> viA(10);
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            viA[i].push_back(rand() % 100);
        }
    }

    cout<< "no ："  << endl;
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << viA[i][j] << "\t";
        }
        cout << endl;
    }
    cout << "sort ：" << endl;

    sort(viA.begin(), viA.end(), cmp1);

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << viA[i][j] << "\t";
        }
        cout << endl;
    }



    return a.exec();
}
