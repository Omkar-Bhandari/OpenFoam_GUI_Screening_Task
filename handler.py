from solver import SolverWin
from inputDialog import InputDialog
from appearance import Appearance
from functools import partial
import qdarktheme
import json
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QDialog,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
    QHBoxLayout,
    QFileDialog,
    QColorDialog,
    QStyle,
)


# Handler Class :: Inheriting from QMainWindow & SolverWin Classes
class Handler(QMainWindow, SolverWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Setting up the SolverWin
        qdarktheme.setup_theme("dark")  # Default Setup theme dark
        self.open_files = {}  # For keeping track of the open files in respective tabs
        self.tab_count = 2  # Initial Count of blank tabs
        self.tab_widget.tabCloseRequested.connect(self.tab_close)  # Closing tab
        self.tab_widget.currentChanged.connect(
            self.action_only_keys_handle
        )  # Setting up the tab whenever the tab is changed

        # File Menu Action Signals Connecting with respective Functions
        self.action_new.triggered.connect(self.action_new_handle)  # New Tab
        self.action_open.triggered.connect(self.action_open_handle)  # Open File
        self.action_save.triggered.connect(self.action_save_handle)  # Saving
        self.action_saveas.triggered.connect(self.action_saveas_handle)  # Save as
        self.action_close.triggered.connect(self.close)  # Exiting Application

        # Insert Menu Action Signals Connecting with respective Functions
        self.action_insert.triggered.connect(self.action_insert_handle)
        self.action_replace.triggered.connect(self.action_replace_handle)
        self.action_delete.triggered.connect(self.action_delete_handle)

        # View Menu Action Signals Connecting with respective Functions
        self.action_only_keys.triggered.connect(self.action_only_keys_handle)
        self.slider.valueChanged.connect(
            lambda value: self.tab_widget.setStyleSheet(
                self.tab_widget.styleSheet()
                + "font-size:{value}pt;".format(value=value)
            )
        )
        self.action_light.triggered.connect(self.light_theme_handle)
        self.action_dark.triggered.connect(self.dark_theme_handle)
        self.action_color_schemes.triggered.connect(self.color_scheme_handle)

    # Helper Function to return the working widget
    def _current_tab_widget(self):
        current_tab = self.tab_widget.currentWidget()
        return current_tab.findChild(QTreeWidget)

    # Closing Tab signal sent
    def tab_close(self, index):
        self.tab_widget.removeTab(index)  # Closes the tab
        self.tab_count -= 1
        if index in self.open_files.keys():  # checks if the tab has open file
            self.open_files.pop(index)  # Removes open files if any
        for i in range(self.tab_count):
            self.tab_widget.setTabText(i, f"Tab {i+1}")  # Renaming all the tabs

    """ File Menu Functions """

    # Creating New Blank Tab & File
    def action_new_handle(self):
        self.tab = QWidget()
        self.tab_widget.addTab(self.tab, "")
        self.tab_widget.setTabText(
            self.tab_widget.indexOf(self.tab),
            "Tab {num}".format(num=self.tab_count + 1),
        )
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        # setting properties for the tree_Widget
        self.tree_widget = QTreeWidget(self.tab)
        self.tree_widget.setColumnWidth(0, 250)
        self.tree_widget.setHeaderHidden(True)
        self.tree_widget.setColumnCount(2)
        self.horizontalLayout_4.addWidget(self.tree_widget)
        self.tab_count += 1
        self.action_only_keys_handle()

    """-- Helper Functions--"""

    # Helper Function to convert raw data from Json to QtreeWidget Item and adding to the treeWidget
    def populate_tree(self, data, parent_item=None):
        tree_widget = self._current_tab_widget()
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):  # Checks if its a root item
                    # Convert => TreeWidgetItem
                    child_item = QTreeWidgetItem([str(key)])
                    self.tree_item_props(child_item)  # Assign Properties
                    tree_widget.addTopLevelItem(child_item)  # Add to the Root
                    self.populate_tree(value, child_item)
                else:
                    child_item = QTreeWidgetItem([str(key), str(value)])
                    self.tree_item_props(child_item)
                    if parent_item:
                        parent_item.addChild(child_item)  # Add child to the root
                    else:
                        tree_widget.addTopLevelItem(child_item)
        tree_widget.expandAll()  # Expands all the roots

    # Helper Function to set up indivisual items properties
    def tree_item_props(self, item):
        item.setCheckState(0, Qt.Unchecked)  # Default Checking State Unchecked
        item.setFlags(
            Qt.ItemIsAutoTristate  # To have the Auto checking when all children are selected respective root is also selected
            | Qt.ItemIsUserCheckable  # MAke the item Checkable
            | Qt.ItemIsEnabled  # Enabled
            | Qt.ItemIsEditable  # Edit Permission
        )

        # Helper Function to covert the Tree Data to Json for Saving

    def tree_to_json(self):
        current_tab = self.tab_widget.currentWidget()
        tree_widget = current_tab.findChild(QTreeWidget)
        tree_dict = {}
        if tree_widget.topLevelItemCount() != 0:
            for i in range(tree_widget.topLevelItemCount()):
                parent_item = tree_widget.topLevelItem(i)
            children_dict = {}
            for j in range(parent_item.childCount()):
                child_item = parent_item.child(j)
                children_dict[child_item.text(0)] = child_item.text(1)

            parent_key = parent_item.text(0)
            tree_dict[parent_key] = children_dict
        return tree_dict

    """-- Helper Functions--"""

    # Opening a File
    def action_open_handle(self):
        # Opening the File Dialog to get the file Name
        fname = QFileDialog.getOpenFileName(self, "Open", filter="JSON Files(*.json);")
        if fname[0]:  # Checking for valid name
            if fname[0] in self.open_files.values():  # Checking if file is already open
                for key, val in self.open_files.items():
                    if val == fname[0]:
                        index = key  # find out the tab of file if open
                # Switching to the tab where the file is already open
                self.tab_widget.setCurrentIndex(index)
            else:  # If file is not open already
                # Update the Open Files Dict to keep track
                self.open_files[
                    self.tab_widget.indexOf(self.tab_widget.currentWidget())
                ] = fname[0]
                with open(fname[0]) as file:  # opening the file
                    try:
                        data = json.load(file)  # Loading the Json data from file
                        self.populate_tree(data)  # Write to screen using Helper Func
                    except:
                        print("Wrong Format")  # Message Box for Wrong Format
        self.action_only_keys_handle()

    # Saving the file
    def action_save_handle(self):
        tree_dict = self.tree_to_json()  # Using helper Func for data
        # Finding out the current open file
        if self.open_files:
            fpath = self.open_files[
                self.tab_widget.indexOf(self.tab_widget.currentWidget())
            ]
            with open(fpath, "w") as file:
                json.dump(tree_dict, fp=file, indent=4)  # Writing to the Json file
            self.statusbar.showMessage(f"Saved to {fpath}", 3000)

    # Saving as a new File
    def action_saveas_handle(self):
        # Using QFile Dialog to save the file
        fname = QFileDialog.getSaveFileName(self, "Save As", "", filter=".json")
        tree_dict = self.tree_to_json()  # Using helper Func for data
        with open(fname[0] + ".json", "x") as file:
            json.dump(tree_dict, fp=file, indent=4)  # Writing to the Json file
        self.statusbar.showMessage(f"Saved to {fname}", 3000)

    """ Insert Menu Functions """

    """--- Helper Functions ---"""

    # BoilerPlate code to create the dialog box for taking the input for Insert & Replace
    def create_dialog(self, title):
        self.dialog_box = QDialog()
        self.dialog = InputDialog()
        self.dialog.setupUi(self.dialog_box)
        self.dialog_box.setWindowTitle(title)
        self.dialog_box.show()

    def action_insert_handle(self):
        self.create_dialog("Insert")
        self.dialog.buttonBox.accepted.connect(self.insert_accepted)  # Insert
        self.dialog.buttonBox.rejected.connect(self.dialog_box.close)  # Cancel

    def action_replace_handle(self):
        self.create_dialog("Replace")
        self.dialog.checkBox.setDisabled(True)  # setting the checkbox disabled
        self.dialog.buttonBox.accepted.connect(self.replace_accepted)  # Replace
        self.dialog.buttonBox.rejected.connect(self.dialog_box.close)  # Cancel

    # Function to Delete Selected Items
    def action_delete_handle(self):
        tree_widget = self._current_tab_widget()
        # Iterating from last element
        for i in range(tree_widget.topLevelItemCount() - 1, -1, -1):
            parent_item = tree_widget.topLevelItem(i)  # Extracting the root elements
            if parent_item.checkState(0) == Qt.Checked:  # CHecking if selected
                tree_widget.takeTopLevelItem(i)  # Removing the root and all its child
            else:
                for j in range(parent_item.childCount() - 1, -1, -1):
                    child_item = parent_item.child(j)
                    if child_item.checkState(0) == Qt.Checked:
                        parent_item.takeChild(j)  # Removing the selected child

    # Replacing the key and Value
    def replace_accepted(self):
        # Taking inputs from the Dilog Box
        key = self.dialog.key_line_edit.text()
        value = self.dialog.value_line_edit.text()
        tree_widget = self._current_tab_widget()
        if len(key) == 0 or len(value) == 0:
            print("Fields Cannot be Empty")
        else:
            for i in range(tree_widget.topLevelItemCount() - 1, -1, -1):
                parent_item = tree_widget.topLevelItem(i)
                if parent_item.checkState(0) == Qt.Checked:  # Checking selection
                    print("Select Only Child")
                else:
                    for j in range(parent_item.childCount() - 1, -1, -1):
                        child_item = parent_item.child(j)
                        if child_item.checkState(0) == Qt.Checked:
                            child_item.setText(0, key)  # Setting key
                            child_item.setText(1, value)  # setting value
            self.dialog_box.close()

    def insert_accepted(self):
        key = self.dialog.key_line_edit.text()
        value = self.dialog.value_line_edit.text()
        tree_widget = self._current_tab_widget()
        if len(key) == 0 and len(value) == 0:
            print("Fields Cannot be Empty")
        else:
            if self.dialog.checkBox.isChecked():  # Checking if item to be added as root
                if key and value:
                    # Adding Root item with key and value
                    child_to_add = QTreeWidgetItem([str(key), str(value)])
                elif key:
                    # Adding Root with key
                    child_to_add = QTreeWidgetItem([str(key)])

                self.tree_item_props(child_to_add)
                tree_widget.addTopLevelItem(child_to_add)  # Addibg to tree

            # Inserting to the Existing Parent
            child_to_add = QTreeWidgetItem([str(key), str(value)])
            self.tree_item_props(child_to_add)
            for i in range(tree_widget.topLevelItemCount() - 1, -1, -1):
                parent_item = tree_widget.topLevelItem(i)
                if parent_item.checkState(0) == Qt.Checked:
                    parent_item.addChild(child_to_add)
                else:
                    for j in range(parent_item.childCount() - 1, -1, -1):
                        child_item = parent_item.child(j)
                        if child_item.checkState(0) == Qt.Checked:
                            print("Select a Parent Item to Add Child")
            self.dialog_box.close()

    """ View Menu Functions """

    # To hide Value Column
    def action_only_keys_handle(self):
        if self.tab_count > 0:
            tree_widget = self._current_tab_widget()
            if self.action_only_keys.isChecked():
                tree_widget.setColumnHidden(1, True)  # Hiding the keys
            else:
                tree_widget.setColumnHidden(1, False)  # Showing

    def light_theme_handle(self):
        self.action_light.setChecked(True)  # Toggling Between the Dark and Light Theme
        self.action_dark.setChecked(False)
        # Setting up the color for slider
        self.slider_widget.setStyleSheet("background-color:#ffffff;")
        # Setting up the dark theme
        qdarktheme.setup_theme("light")

    def dark_theme_handle(self):
        self.action_light.setChecked(False)  # Toggling Between the Dark and Light Theme
        self.action_dark.setChecked(True)
        # Setting up the color for slider
        self.slider_widget.setStyleSheet("background-color:#2a2b2f;")
        # Setting up the Light theme
        qdarktheme.setup_theme("dark")

    def color_scheme_handle(self):
        self.dialog_box = QDialog()
        self.appearance = Appearance()
        # Launching the Appearance change dialog
        self.appearance.setupUi(self.dialog_box)
        self.dialog_box.setWindowTitle("Appearance")
        # Color Dialog
        self.appearance.font_pallete.clicked.connect(
            partial(self.launch_color_dialog, "font")
        )
        self.appearance.menu_pallete.clicked.connect(
            partial(self.launch_color_dialog, "menu")
        )
        self.appearance.bgcolor_pallete.clicked.connect(
            partial(self.launch_color_dialog, "bgcolor")
        )
        self.appearance.buttonBox.accepted.connect(self.appearance_apply)
        self.appearance.buttonBox.rejected.connect(self.dialog_box.close)
        self.dialog_box.show()

    # Applying the colors
    def appearance_apply(self):
        font = self.appearance.font_combo_box.currentText()
        self.setStyleSheet("font-family:{font};".format(font=font))
        font_color = self.appearance.font_color_text.text()
        menu_color = self.appearance.menu_bar_color_text.text()
        bg_color = self.appearance.bgcolor_text.text()
        if font_color:
            if QColor(font_color).isValid():  # checking Q color validity
                self.tab_widget.setStyleSheet(
                    self.tab_widget.styleSheet()
                    + "color:{color};".format(color=font_color)  # adding to stylesheet
                )
                self.menu_bar.setStyleSheet(
                    self.menu_bar.styleSheet()
                    + "color:{color};".format(color=font_color)
                )
            else:
                print("Invalid Color")
        if menu_color:
            if QColor(menu_color).isValid():
                self.menu_bar.setStyleSheet(
                    self.menu_bar.styleSheet()
                    + "background-color:{color};".format(color=menu_color)
                )
                self.slider_widget.setStyleSheet(
                    "background-color:{color};".format(color=menu_color)
                )
            else:
                print("Invalid Color")
        if bg_color:
            if QColor(bg_color).isValid():
                self.centralwidget.setStyleSheet(
                    self.centralwidget.styleSheet()
                    + "background-color:{color};".format(color=bg_color)
                )
                self.dialog_box.setStyleSheet(
                    self.dialog_box.styleSheet()
                    + "background-color:{color};".format(color=bg_color)
                )
            else:
                print("Invalid Color")

    # Lauching the color dialog from tool button and setting the color text
    def launch_color_dialog(self, pallete):
        color = QColorDialog.getColor()
        if pallete == "font":
            self.appearance.font_color_text.setText(color.name())
        elif pallete == "menu":
            self.appearance.menu_bar_color_text.setText(color.name())
        elif pallete == "bgcolor":
            self.appearance.bgcolor_text.setText(color.name())
