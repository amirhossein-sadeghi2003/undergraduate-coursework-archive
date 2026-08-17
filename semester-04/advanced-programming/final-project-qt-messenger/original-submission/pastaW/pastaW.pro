QT       += core gui network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    contact.cpp \
    login.cpp \
    main.cpp \
    messanger_list.cpp \
    messanger_page.cpp \
    signup.cpp \
    userclass.cpp

HEADERS += \
    contact.h \
    login.h \
    messanger_list.h \
    messanger_page.h \
    signup.h \
    userclass.h

FORMS += \
    login.ui \
    messanger_list.ui \
    messanger_page.ui \
    signup.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
