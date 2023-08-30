# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Ui_ColorSchemes.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Appearance(object):
    def setupUi(self, ColorSchemes):
        ColorSchemes.setObjectName("ColorSchemes")
        ColorSchemes.resize(480, 236)
        self.gridLayout_2 = QtWidgets.QGridLayout(ColorSchemes)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(ColorSchemes)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.font_fam_label = QtWidgets.QLabel(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_fam_label.setFont(font)
        self.font_fam_label.setObjectName("font_fam_label")
        self.gridLayout.addWidget(self.font_fam_label, 0, 0, 1, 1)
        self.font_combo_box = QtWidgets.QFontComboBox(ColorSchemes)
        self.font_combo_box.setObjectName("font_combo_box")
        self.gridLayout.addWidget(self.font_combo_box, 0, 1, 1, 2)
        self.font_color_label = QtWidgets.QLabel(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_color_label.setFont(font)
        self.font_color_label.setObjectName("font_color_label")
        self.gridLayout.addWidget(self.font_color_label, 1, 0, 2, 1)
        self.font_color_text = QtWidgets.QLineEdit(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_color_text.setFont(font)
        self.font_color_text.setObjectName("font_color_text")
        self.gridLayout.addWidget(self.font_color_text, 1, 1, 1, 2)
        self.font_pallete = QtWidgets.QToolButton(ColorSchemes)
        self.font_pallete.setObjectName("font_pallete")
        self.gridLayout.addWidget(self.font_pallete, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(ColorSchemes)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 2)
        self.bgcolor_label = QtWidgets.QLabel(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bgcolor_label.setFont(font)
        self.bgcolor_label.setObjectName("bgcolor_label")
        self.gridLayout.addWidget(self.bgcolor_label, 3, 0, 1, 1)
        self.bgcolor_text = QtWidgets.QLineEdit(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bgcolor_text.setFont(font)
        self.bgcolor_text.setText("")
        self.bgcolor_text.setObjectName("bgcolor_text")
        self.gridLayout.addWidget(self.bgcolor_text, 3, 1, 1, 2)
        self.bgcolor_pallete = QtWidgets.QToolButton(ColorSchemes)
        self.bgcolor_pallete.setObjectName("bgcolor_pallete")
        self.gridLayout.addWidget(self.bgcolor_pallete, 3, 3, 1, 1)
        self.menu_bar_color_label = QtWidgets.QLabel(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_bar_color_label.setFont(font)
        self.menu_bar_color_label.setObjectName("menu_bar_color_label")
        self.gridLayout.addWidget(self.menu_bar_color_label, 4, 0, 1, 1)
        self.menu_bar_color_text = QtWidgets.QLineEdit(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_bar_color_text.setFont(font)
        self.menu_bar_color_text.setText("")
        self.menu_bar_color_text.setObjectName("menu_bar_color_text")
        self.gridLayout.addWidget(self.menu_bar_color_text, 4, 1, 1, 2)
        self.menu_pallete = QtWidgets.QToolButton(ColorSchemes)
        self.menu_pallete.setObjectName("menu_pallete")
        self.gridLayout.addWidget(self.menu_pallete, 4, 3, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonBox = QtWidgets.QDialogButtonBox(ColorSchemes)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 2, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(ColorSchemes)
        self.buttonBox.accepted.connect(ColorSchemes.accept)  # type: ignore
        self.buttonBox.rejected.connect(ColorSchemes.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ColorSchemes)

    def retranslateUi(self, ColorSchemes):
        _translate = QtCore.QCoreApplication.translate
        ColorSchemes.setWindowTitle(_translate("ColorSchemes", "Dialog"))
        self.label_6.setText(_translate("ColorSchemes", "Appearance"))
        self.font_fam_label.setText(_translate("ColorSchemes", "Font:"))
        self.font_color_label.setText(_translate("ColorSchemes", "Font Color:"))
        self.font_pallete.setText(_translate("ColorSchemes", "..."))
        self.label_5.setText(_translate("ColorSchemes", "eg.#ffffff or White"))
        self.bgcolor_label.setText(_translate("ColorSchemes", "Background Color:"))
        self.bgcolor_pallete.setText(_translate("ColorSchemes", "..."))
        self.menu_bar_color_label.setText(_translate("ColorSchemes", "Menubar Color:"))
        self.menu_pallete.setText(_translate("ColorSchemes", "..."))