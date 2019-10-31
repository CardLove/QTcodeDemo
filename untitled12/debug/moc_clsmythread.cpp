/****************************************************************************
** Meta object code from reading C++ file 'clsmythread.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.13.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../clsmythread.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'clsmythread.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.13.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_clsMyThread_t {
    QByteArrayData data[8];
    char stringdata0[75];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_clsMyThread_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_clsMyThread_t qt_meta_stringdata_clsMyThread = {
    {
QT_MOC_LITERAL(0, 0, 11), // "clsMyThread"
QT_MOC_LITERAL(1, 12, 13), // "sig_sendfirst"
QT_MOC_LITERAL(2, 26, 0), // ""
QT_MOC_LITERAL(3, 27, 14), // "sig_sendsecond"
QT_MOC_LITERAL(4, 42, 13), // "sig_sendThird"
QT_MOC_LITERAL(5, 56, 5), // "first"
QT_MOC_LITERAL(6, 62, 6), // "second"
QT_MOC_LITERAL(7, 69, 5) // "three"

    },
    "clsMyThread\0sig_sendfirst\0\0sig_sendsecond\0"
    "sig_sendThird\0first\0second\0three"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_clsMyThread[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       3,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   44,    2, 0x06 /* Public */,
       3,    0,   45,    2, 0x06 /* Public */,
       4,    0,   46,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       5,    0,   47,    2, 0x0a /* Public */,
       6,    0,   48,    2, 0x0a /* Public */,
       7,    0,   49,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void clsMyThread::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<clsMyThread *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->sig_sendfirst(); break;
        case 1: _t->sig_sendsecond(); break;
        case 2: _t->sig_sendThird(); break;
        case 3: _t->first(); break;
        case 4: _t->second(); break;
        case 5: _t->three(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (clsMyThread::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&clsMyThread::sig_sendfirst)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (clsMyThread::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&clsMyThread::sig_sendsecond)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (clsMyThread::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&clsMyThread::sig_sendThird)) {
                *result = 2;
                return;
            }
        }
    }
    Q_UNUSED(_a);
}

QT_INIT_METAOBJECT const QMetaObject clsMyThread::staticMetaObject = { {
    &QObject::staticMetaObject,
    qt_meta_stringdata_clsMyThread.data,
    qt_meta_data_clsMyThread,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *clsMyThread::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *clsMyThread::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_clsMyThread.stringdata0))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int clsMyThread::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 6;
    }
    return _id;
}

// SIGNAL 0
void clsMyThread::sig_sendfirst()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void clsMyThread::sig_sendsecond()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void clsMyThread::sig_sendThird()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
