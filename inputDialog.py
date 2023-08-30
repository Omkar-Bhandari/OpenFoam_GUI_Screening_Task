from PyQt5 import QtCore, QtGui, QtWidgets


class InputDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(645, 139)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.key_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.key_label.setFont(font)
        self.key_label.setObjectName("key_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.key_label)
        self.value_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.value_label.setFont(font)
        self.value_label.setObjectName("value_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.value_label)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.key_line_edit = QtWidgets.QLineEdit(Dialog)
        self.key_line_edit.setObjectName("key_line_edit")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.key_line_edit
        )
        self.value_line_edit = QtWidgets.QLineEdit(Dialog)
        self.value_line_edit.setObjectName("value_line_edit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.value_line_edit
        )
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.checkBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.key_label.setText(_translate("Dialog", "Key"))
        self.value_label.setText(_translate("Dialog", "Value"))
        self.checkBox.setText(_translate("Dialog", "Insert As New Parent"))
