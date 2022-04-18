# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 493)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.c_nrosocio = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.c_nrosocio.setObjectName("c_nrosocio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.c_nrosocio)
        self.l_nombre = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_nombre.setObjectName("l_nombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.l_nombre)
        self.c_nombre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.c_nombre.setObjectName("c_nombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.c_nombre)
        self.l_apellido = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_apellido.setObjectName("l_apellido")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.l_apellido)
        self.c_apellido = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.c_apellido.setObjectName("c_apellido")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.c_apellido)
        self.l_edad = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_edad.setObjectName("l_edad")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.l_edad)
        self.c_edad = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.c_edad.setObjectName("c_edad")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.c_edad)
        self.l_categoria = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_categoria.setObjectName("l_categoria")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.l_categoria)
        self.c_categoria = QtWidgets.QComboBox(self.formLayoutWidget)
        self.c_categoria.setObjectName("c_categoria")
        self.c_categoria.addItem("")
        self.c_categoria.addItem("")
        self.c_categoria.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.c_categoria)
        self.l_sexo = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_sexo.setObjectName("l_sexo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.l_sexo)
        self.c_sexo = QtWidgets.QComboBox(self.formLayoutWidget)
        self.c_sexo.setObjectName("c_sexo")
        self.c_sexo.addItem("")
        self.c_sexo.addItem("")
        self.c_sexo.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.c_sexo)
        self.l_nrosocio = QtWidgets.QLabel(self.formLayoutWidget)
        self.l_nrosocio.setObjectName("l_nrosocio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.l_nrosocio)
        self.bot_agregar = QtWidgets.QPushButton(self.centralwidget)
        self.bot_agregar.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.bot_agregar.setObjectName("bot_agregar")
        self.bot_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.bot_buscar.setGeometry(QtCore.QRect(140, 180, 111, 23))
        self.bot_buscar.setObjectName("bot_buscar")
        self.bot_borrar = QtWidgets.QPushButton(self.centralwidget)
        self.bot_borrar.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.bot_borrar.setObjectName("bot_borrar")
        self.bot_salir = QtWidgets.QPushButton(self.centralwidget)
        self.bot_salir.setGeometry(QtCore.QRect(450, 180, 75, 23))
        self.bot_salir.setObjectName("bot_salir")
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(10, 210, 701, 251))
        self.tabla.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(6)
        self.tabla.setRowCount(0)
        self.tabla.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registry"))
        self.l_nombre.setText(_translate("MainWindow", "First Name"))
        self.l_apellido.setText(_translate("MainWindow", "Last Name"))
        self.l_edad.setText(_translate("MainWindow", "Age"))
        self.l_categoria.setText(_translate("MainWindow", "Category"))
        self.c_categoria.setItemText(0, _translate("MainWindow", "A"))
        self.c_categoria.setItemText(1, _translate("MainWindow", "B"))
        self.c_categoria.setItemText(2, _translate("MainWindow", "C"))
        self.l_sexo.setText(_translate("MainWindow", "Gender"))
        self.c_sexo.setItemText(0, _translate("MainWindow", "Male"))
        self.c_sexo.setItemText(1, _translate("MainWindow", "Female"))
        self.c_sexo.setItemText(2, _translate("MainWindow", "Other"))
        self.l_nrosocio.setText(_translate("MainWindow", "Member Number"))
        self.bot_agregar.setText(_translate("MainWindow", "Add"))
        self.bot_buscar.setText(_translate("MainWindow", "Search (Member Nº)"))
        self.bot_borrar.setText(_translate("MainWindow", "Delete"))
        self.bot_salir.setText(_translate("MainWindow", "Exit"))
        self.tabla.setSortingEnabled(True)
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Member Nº"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last name"))
        item = self.tabla.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Age"))
        item = self.tabla.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tabla.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Gender"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())