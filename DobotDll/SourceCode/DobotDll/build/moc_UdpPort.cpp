/****************************************************************************
** Meta object code from reading C++ file 'UdpPort.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.9.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../src/DobotDevice/UdpPort.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'UdpPort.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.9.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_UdpPort_t {
    QByteArrayData data[6];
    char stringdata0[86];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_UdpPort_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_UdpPort_t qt_meta_stringdata_UdpPort = {
    {
QT_MOC_LITERAL(0, 0, 7), // "UdpPort"
QT_MOC_LITERAL(1, 8, 17), // "SetHeartBeartEmit"
QT_MOC_LITERAL(2, 26, 0), // ""
QT_MOC_LITERAL(3, 27, 23), // "processPendingDatagrams"
QT_MOC_LITERAL(4, 51, 15), // "OnHeartBeatTime"
QT_MOC_LITERAL(5, 67, 18) // "SetHeartBeatSignal"

    },
    "UdpPort\0SetHeartBeartEmit\0\0"
    "processPendingDatagrams\0OnHeartBeatTime\0"
    "SetHeartBeatSignal"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_UdpPort[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       4,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   34,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       3,    0,   37,    2, 0x08 /* Private */,
       4,    0,   38,    2, 0x08 /* Private */,
       5,    1,   39,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::Bool,    2,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    2,

       0        // eod
};

void UdpPort::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        UdpPort *_t = static_cast<UdpPort *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->SetHeartBeartEmit((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->processPendingDatagrams(); break;
        case 2: _t->OnHeartBeatTime(); break;
        case 3: _t->SetHeartBeatSignal((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        void **func = reinterpret_cast<void **>(_a[1]);
        {
            typedef void (UdpPort::*_t)(bool );
            if (*reinterpret_cast<_t *>(func) == static_cast<_t>(&UdpPort::SetHeartBeartEmit)) {
                *result = 0;
                return;
            }
        }
    }
}

const QMetaObject UdpPort::staticMetaObject = {
    { &QIODevice::staticMetaObject, qt_meta_stringdata_UdpPort.data,
      qt_meta_data_UdpPort,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *UdpPort::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *UdpPort::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_UdpPort.stringdata0))
        return static_cast<void*>(const_cast< UdpPort*>(this));
    return QIODevice::qt_metacast(_clname);
}

int UdpPort::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QIODevice::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void UdpPort::SetHeartBeartEmit(bool _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE