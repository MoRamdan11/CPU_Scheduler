# CPU_Schedular
Desktop Application for drawing a gantt chart for cpu schedular algrothims(FCFS, SJF, RoundRobin, Priority)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Amal\PycharmProjects\Project OS\co2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import turtle
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 635)
        MainWindow.setStyleSheet("/* ---------------------------------------------------------------------------\n"
"\n"
"    Created by the qtsass compiler v0.1.1\n"
"\n"
"    The definitions are in the \"qdarkstyle.qss._styles.scss\" module\n"
"\n"
"    WARNING! All changes made in this file will be lost!\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* QDarkStyleSheet -----------------------------------------------------------\n"
"\n"
"This is the main style sheet, the palette has nine colors.\n"
"\n"
"It is based on three selecting colors, three greyish (background) colors\n"
"plus three whitish (foreground) colors. Each set of widgets of the same\n"
"type have a header like this:\n"
"\n"
"    ------------------\n"
"    GroupName --------\n"
"    ------------------\n"
"\n"
"And each widget is separated with a header like this:\n"
"\n"
"    QWidgetName ------\n"
"\n"
"This makes more easy to find and change some css field. The basic\n"
"configuration is described bellow.\n"
"\n"
"    BACKGROUND -----------\n"
"\n"
"        Light   (unpressed)\n"
"        Normal  (border, disabled, pressed, checked, toolbars, menus)\n"
"        Dark    (background)\n"
"\n"
"    FOREGROUND -----------\n"
"\n"
"        Light   (texts/labels)\n"
"        Normal  (not used yet)\n"
"        Dark    (disabled texts)\n"
"\n"
"    SELECTION ------------\n"
"\n"
"        Light  (selection/hover/active)\n"
"        Normal (selected)\n"
"        Dark   (selected disabled)\n"
"\n"
"If a stranger configuration is required because of a bugfix or anything\n"
"else, keep the comment on the line above so nobody changes it, including the\n"
"issue number.\n"
"\n"
"*/\n"
"/*\n"
"\n"
"See Qt documentation:\n"
"\n"
"  - https://doc.qt.io/qt-5/stylesheet.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-reference.html\n"
"  - https://doc.qt.io/qt-5/stylesheet-examples.html\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* QWidget ----------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QWidget {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"  selection-background-color: #14506E;\n"
"  selection-color: #787878;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QWidget::item:hover {\n"
"  background-color: #148CD2;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QMainWindow ------------------------------------------------------------\n"
"\n"
"This adjusts the splitter in the dock widget, not qsplitter\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMainWindow::separator {\n"
"  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"  background-color: #505F69;\n"
"  border: 0px solid #148CD2;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"  width: 5px;\n"
"  margin-top: 2px;\n"
"  margin-bottom: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"  height: 5px;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"/* QToolTip ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtooltip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolTip {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Remove opacity, fix #174 - may need to use RGBA */\n"
"}\n"
"\n"
"/* QStatusBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStatusBar {\n"
"  border: 1px solid #32414B;\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: #32414B;\n"
"  /* Fixes #205, white vertical borders separating items */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"  border: none;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: transparent;\n"
"}\n"
"\n"
"/* QCheckBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
"  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 4px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:focus, QCheckBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:focus, QCheckBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus, QCheckBox::indicator:indeterminate:hover, QCheckBox::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"/* QGroupBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGroupBox {\n"
"  font-weight: bold;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 4px;\n"
"  margin-top: 16px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 3px;\n"
"  padding-left: 3px;\n"
"  padding-right: 5px;\n"
"  padding-top: 8px;\n"
"  padding-bottom: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QRadioButton -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QRadioButton {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
"  padding: 0px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton QWidget {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  border: none;\n"
"  outline: none;\n"
"  margin-left: 4px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QRadioButton::indicator:unchecked:focus, QRadioButton::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QRadioButton::indicator:checked:focus, QRadioButton::indicator:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QMenuBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenuBar {\n"
"  background-color: #32414B;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #32414B;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border: 0px solid #32414B;\n"
"  background-color: #148CD2;\n"
"  color: #F0F0F0;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu {\n"
"  border: 0px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  margin: 0px;\n"
"  padding-left: 8px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #32414B;\n"
"  padding: 4px 24px 4px 24px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  padding-left: 6px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"  margin: 5px;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractItemView {\n"
"  alternate-background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"  padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ----------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractScrollArea {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  /* fix #159 */\n"
"  min-height: 1.25em;\n"
"  /* fix #159 */\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollArea QWidget QWidget:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #19232D;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/qss_icons/rc/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWidget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #32414B;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #32414B;\n"
"  border-bottom: 1px solid #19232D;\n"
"  padding: 2px;\n"
"  font-weight: bold;\n"
"  spacing: 2px;\n"
"}\n"
"\n"
"QToolBar QToolButton {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBar QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked {\n"
"  border: 1px solid #19232D;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_vertical.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
"  background: #32414B;\n"
"  border: 0px;\n"
"  color: #F0F0F0;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"/* QAbstractSpinBox -------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractSpinBox {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-radius: 4px;\n"
"  /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  border-left: 1px solid #32414B;\n"
"  border-bottom: 1px solid #32414B;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-bottom: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: bottom right;\n"
"  border-left: 1px solid #32414B;\n"
"  border-top: 1px solid #32414B;\n"
"  border-top-left-radius: 0;\n"
"  border-bottom-left-radius: 0;\n"
"  margin: 1px;\n"
"  width: 12px;\n"
"  margin-top: -1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractSpinBox:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS --------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QTextBrowser -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextBrowser {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser:selected, QTextBrowser:pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QGraphicsView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGraphicsView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView:selected, QGraphicsView:pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCalendarWidget --------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCalendarWidget {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QLCDNumber -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLCDNumber {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLCDNumber:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QProgressBar -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #1464A0;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #14506E;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS ---------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QPushButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPushButton {\n"
"  background-color: #505F69;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"  /* Issue #194 - Special case of QPushButton inside dialogs, for better UI */\n"
"  min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
"  bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  /* The subcontrols below are used only in the DelayedPopup mode */\n"
"  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
"  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background-color: transparent;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QToolButton:checked:disabled {\n"
"  border: 1px solid #14506E;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  margin: 1px;\n"
"  background-color: transparent;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"0\"] {\n"
"  /* Only for DelayedPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"  /* Only for MenuButtonPopup */\n"
"  padding-right: 20px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"]::menu-button:hover {\n"
"  border: none;\n"
"  border-left: 1px solid #148CD2;\n"
"  border-radius: 0;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"  /* Only for InstantPopup */\n"
"  padding-right: 2px;\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"  padding: 2px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  width: 12px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-button:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"  top: 0;\n"
"  /* Exclude a shift for better image */\n"
"  left: -2px;\n"
"  /* Shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_down_focus.png\");\n"
"}\n"
"\n"
"/* QCommandLinkButton -----------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCommandLinkButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"  background-color: transparent;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QComboBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QComboBox {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  selection-background-color: #1464A0;\n"
"  padding-left: 4px;\n"
"  padding-right: 36px;\n"
"  /* 4 + 16*2 See scrollbar size */\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 0;\n"
"  background-color: #19232D;\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:hover {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"  border: none;\n"
"  border-radius: 0;\n"
"  background-color: transparent;\n"
"  selection-background-color: transparent;\n"
"  color: transparent;\n"
"  selection-color: transparent;\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox::indicator:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:checked {\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"  border: 0px solid transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"/* QSlider ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSlider:disabled {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"  background: #1464A0;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical :disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: #1464A0;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: -8px 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: 0 -8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QSlider::handle:vertical:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background-color: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabWidget {\n"
"  padding: 2px;\n"
"  selection-background-color: #32414B;\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  /* Fixes #189 */\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane with pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QTabBar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"  border: 0;\n"
"  margin: 2px;\n"
"  padding: 2px;\n"
"  image: url(\":/qss_icons/rc/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"/* QTabBar::tab - selected ------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar::tab {\n"
"  /* !selected and disabled ----------------------------------------- */\n"
"  /* selected ------------------------------------------------------- */\n"
"}\n"
"\n"
"QTabBar::tab:top:selected:disabled {\n"
"  border-bottom: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled {\n"
"  border-top: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:disabled {\n"
"  border-right: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled {\n"
"  border-left: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:disabled {\n"
"  border-bottom: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled {\n"
"  border-top: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled {\n"
"  border-right: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled {\n"
"  border-left: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"  border-bottom: 2px solid #19232D;\n"
"  margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"  border-top: 2px solid #19232D;\n"
"  margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"  border-left: 2px solid #19232D;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"  border-right: 2px solid #19232D;\n"
"  margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  min-width: 5px;\n"
"  border-bottom: 3px solid #32414B;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"  border-bottom: 3px solid #1464A0;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-bottom: 3px solid #148CD2;\n"
"  /* Fixes spyder-ide/spyder#9766 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom {\n"
"  color: #F0F0F0;\n"
"  border-top: 3px solid #32414B;\n"
"  background-color: #32414B;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-top: 3px solid #1464A0;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-top: 3px solid #148CD2;\n"
"  /* Fixes spyder-ide/spyder#9766 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:left {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-left-radius: 3px;\n"
"  border-bottom-left-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-right: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-right: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-left: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-left: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color: #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed {\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #32414B;\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: url(\":/qss_icons/rc/window_close.png\");\n"
"  titlebar-normal-icon: url(\":/qss_icons/rc/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Better size for title bar */\n"
"  padding: 6px;\n"
"  spacing: 4px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_undock_pressed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView -----------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/qss_icons/rc/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_closed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
"QListView::indicator:checked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView,\n"
"QTableView,\n"
"QColumnView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  gridline-color: #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTreeView:disabled,\n"
"QListView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QListView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"  background-color: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QTreeView:hover,\n"
"QListView:hover,\n"
"QTableView:hover,\n"
"QColumnView:hover {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QTreeView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QTreeView::item:selected:hover,\n"
"QListView::item:selected:hover,\n"
"QTableView::item:selected:hover,\n"
"QColumnView::item:selected:hover {\n"
"  background: #1464A0;\n"
"  color: #19232D;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::item:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:selected:active {\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"  outline: 0;\n"
"  color: #148CD2;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #19232D;\n"
"  border: 1px transparent #32414B;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QHeaderView {\n"
"  background-color: #32414B;\n"
"  border: 0px transparent #32414B;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"QHeaderView:disabled {\n"
"  background-color: #32414B;\n"
"  border: 1px transparent #32414B;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  padding: 2px;\n"
"  border-radius: 0px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"  color: #F0F0F0;\n"
"  background-color: #1464A0;\n"
"}\n"
"\n"
"QHeaderView::section:checked:disabled {\n"
"  color: #787878;\n"
"  background-color: #14506E;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-left: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {\n"
"  border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-top: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {\n"
"  border-top: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"  /* Those settings (border/width/height/background-color) solve bug */\n"
"  /* transparent arrow background and size */\n"
"  background-color: #32414B;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  background-color: #32414B;\n"
"  border: none;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"/* QToolBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBox {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBox:selected {\n"
"  padding: 0px;\n"
"  border: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  background-color: #505F69;\n"
"  border-bottom: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #14506E;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"  border-color: #148CD2;\n"
"  border-bottom: 2px solid #148CD2;\n"
"}\n"
"\n"
"QToolBox QScrollArea QWidget QWidget {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QFrame -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"https://doc.qt.io/qt-5/qframe.html#-prop\n"
"https://doc.qt.io/qt-5/qframe.html#details\n"
"https://stackoverflow.com/questions/14581498/qt-stylesheet-for-hline-vline-color\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"/* (dot) .QFrame  fix #141, #126, #123 */\n"
".QFrame {\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  /* No frame */\n"
"  /* HLine */\n"
"  /* HLine */\n"
"}\n"
"\n"
".QFrame[frameShape=\"0\"] {\n"
"  border-radius: 4px;\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
".QFrame[frameShape=\"4\"] {\n"
"  max-height: 2px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
".QFrame[frameShape=\"5\"] {\n"
"  max-width: 2px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"/* QSplitter --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSplitter {\n"
"  background-color: #32414B;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 1px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"  background-color: #787878;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"  width: 5px;\n"
"  image: url(\":/qss_icons/rc/line_vertical.png\");\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"  height: 5px;\n"
"  image: url(\":/qss_icons/rc/line_horizontal.png\");\n"
"}\n"
"\n"
"/* QDateEdit, QDateTimeEdit -----------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDateEdit, QDateTimeEdit {\n"
"  selection-background-color: #1464A0;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:on, QDateTimeEdit:on {\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QDateEdit::drop-down, QDateTimeEdit::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 12px;\n"
"  border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 8px;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus, QDateTimeEdit::down-arrow:on, QDateTimeEdit::down-arrow:hover, QDateTimeEdit::down-arrow:focus {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView, QDateTimeEdit QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  selection-background-color: #1464A0;\n"
"}\n"
"\n"
"/* QAbstractView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractView:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* PlotWidget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"PlotWidget {\n"
"  /* Fix cut labels in plots #134 */\n"
"  padding: 0px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(13, 20, 501, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 441, 221))
        self.tableWidget.setStyleSheet("border-color: rgb(170, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(47)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(37, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(38, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(39, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(40, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(41, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(42, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(43, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(44, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(45, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(46, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(205, 240, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(170, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-color: rgb(170, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-color: rgb(170, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(330, 110, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(170, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(205, 240, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 440, 71, 31))
        self.lineEdit_3.setStyleSheet("border-color: rgb(170, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 440, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(360, 80, 91, 21))
        self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(330, 400, 131, 21))
        self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 140, 121, 21))
        self.lineEdit_8.setStyleSheet("border-color: rgb(32, 31, 31);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.process_time)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Burst Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Priority"))
        self.pushButton.setText(_translate("MainWindow", "Simulate"))
        self.comboBox.setItemText(0, _translate("MainWindow", "FCFS"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SJF (Non Preemptive)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "SJF (Preemtive)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Round Robin"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Priority (Non Preemptive)"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Priority (Preemptive)"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "N of process"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Round Robin"))
        self.label.setText(_translate("MainWindow", "Q"))
        self.pushButton_5.setText(_translate("MainWindow", "Sechedular Algrothims"))
        self.pushButton_2.setText(_translate("MainWindow", "Average Waiting Time"))

    def process_time(self):
        try:
            n = int(self.lineEdit.text())
            self.lineEdit_8.setStyleSheet("border-color: rgb(32, 31, 31);") #main border colour
            self.lineEdit_8.clear()
            self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
            self.lineEdit_6.clear()
            if n == 0:
                self.lineEdit_8.clear()
                self.lineEdit_8.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_8.insert("Invalid N")
                self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
                self.lineEdit_6.clear()
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        except:
            self.lineEdit_8.clear()
            self.lineEdit_8.setStyleSheet("border-color: rgb(255, 255, 127);") #Yellow Border Colour
            self.lineEdit_8.insert("Invalid N")
            self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
            self.lineEdit_6.clear()
            self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
            self.lineEdit_7.clear()
            return
        try:
            p_burst = []
            p_arrival = []
            p_name = []
            for i in range(n):
                p_name.append(str(self.tableWidget.item(i, 0).text()))
                for j in range(0, i):
                    if p_name[j] == p_name[i]:
                        self.lineEdit_6.clear()
                        self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                        self.lineEdit_6.insert("Repeated process name")
                        return
            for i in range(n):
                p_arrival.append(float(self.tableWidget.item(i, 1).text()))
            for i in range(n):
                p_burst.append(float(self.tableWidget.item(i, 2).text()))
                if p_burst[i] == 0:
                    self.lineEdit_6.clear()
                    self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                    self.lineEdit_6.insert("invalid burst time")
                    self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                    self.lineEdit_7.clear()
                    return
            self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
            self.lineEdit_6.clear()
        except:
            self.lineEdit_6.clear()
            self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
            self.lineEdit_6.insert("invalid process input")
            self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
            self.lineEdit_7.clear()
            return

        if self.comboBox.currentText() == self.comboBox.itemText(3):  # Round Robin
            try:
                q = float(self.lineEdit_2.text())
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                if q == 0:
                    self.lineEdit_7.clear()
                    self.lineEdit_7.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                    self.lineEdit_7.insert("Invalid Q")
                    return
            except:
                self.lineEdit_7.clear()
                self.lineEdit_7.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_7.insert("Invalid Q")
                return
        if self.comboBox.currentText() == self.comboBox.itemText(4) or self.comboBox.currentText() == self.comboBox.itemText(5):  # Priority Non_preemptive
            try:
                self.lineEdit_6.setStyleSheet("border-color: rgb(32, 31, 31);")
                self.lineEdit_6.clear()
                p_priority = []
                for i in range(n):
                    p_priority.append(float(self.tableWidget.item(i, 3).text()))
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("invalid process input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        turtle.clearscreen()
        t = turtle.Turtle()
        text = 0
        w_time = 0
        t.speed(20)
        t.color("White")
        t.setheading(180)
        t.forward(400)
        t.color("Black")
        idle = 0
        idle_total = 0
        x = 0
        k = 0
        p_exc = 0
        m = 0
        if self.comboBox.currentText() == self.comboBox.itemText(0):  # FCFS
            try:
                for i in range(n):
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(1):  # SJF(NonPreemptive)
            try:
                for i in range(n):
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_burst[j] < p_burst[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                        if p_arrival[j] < text:
                            if p_burst[j] < p_burst[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                    text = text + p_burst[i]
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(2):  # sjf(Preemptive)
            try:
                for i in range(n):  # Non_Preemptive
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_burst[j] < p_burst[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                text = 0
                for i in range(n):
                    for j in range(i + 1, n):
                        if p_arrival[j] < text:
                            if p_burst[j] < p_burst[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                        if p_arrival[i] > text:
                            p_arr = text
                            p_exc = 0
                            while p_arr < p_arrival[i]:
                                p_arr = p_arr + 0.1
                                p_exc = p_exc + 0.1
                            text = text + p_exc
                        if p_arrival[j] > text and p_arrival[j] < text + p_burst[i]:
                            if p_burst[j] < p_burst[i]:
                                p_arr = text
                                p_exc = 0
                                while p_arr < p_arrival[j]:
                                    p_arr = p_arr + 0.1
                                    p_exc = p_exc + 0.1
                                p_burst[i] = p_burst[i] - p_exc
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                p_arrival.insert(i, p_arrival[j])
                                p_burst.insert(i, p_exc)
                                p_name.insert(i, p_name[j])
                                n = n + 1
                                m = m + 1
                    text = text + p_burst[i]
                for i in range(n):
                    if p_burst[i] == 0:
                        p_burst.pop(i)
                        p_arrival.pop(i)
                        p_name.pop(i)
                        n = n - 1
                        m = m - 1
                    else:
                        continue
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    for j in range(i + 1, n):
                        if p_name[i] == p_name[j]:
                            index = i
                            p_arrival[j] = p_arrival[j] + p_burst[i]
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / (n - m)
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(3):  # Round Robin
            try:
                if q < 3:
                    coff = 15
                elif q < 5:
                    coff = 10
                elif q <= 10:
                    coff = 7
                elif q < 50:
                    coff = 5
                else:
                    coff = 3
                m = []
                for i in range(n):
                    for j in range(i + 1, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                text = 0
                count = n
                m = 0
                w_time = 0
                while count > 0:
                    count = n
                    for i in range(n):
                        if p_burst[i] == 0:
                            continue
                        if p_burst[i] < q and p_burst[i] <= text:
                            if text == 0:
                                t.setheading(270)
                                t.forward(30)
                                t.color("Black")
                                style = ('Courier', 12)
                                t.write("0", font=style)
                                t.color("White")
                                t.setheading(90)
                                t.forward(30)
                            t.color("Black")
                            t.setheading(0)
                            t.forward(5 * p_burst[i])
                            t.setheading(90)
                            t.forward(50)
                            t.setheading(180)
                            t.forward(5 * p_burst[i])
                            t.setheading(270)
                            t.forward(50)
                            t.setheading(0)
                            t.forward(5 * p_burst[i])
                            text = text + p_burst[i]
                            text = round(text, 2)
                            t.color("White")
                            t.setheading(270)
                            t.forward(30)
                            t.setheading(180)
                            t.forward(20)
                            t.color("Black")
                            style = ('Courier', 12)
                            t.write(text, font=style)
                            t.color("White")
                            t.setheading(0)
                            t.forward(20)
                            t.setheading(90)
                            t.forward(30)
                            t.setheading(180)
                            t.forward(4 * p_burst[i])
                            t.setheading(90)
                            t.forward(10)
                            t.color("Black")
                            style = ('Courier', 20)
                            t.write(p_name[i], font=style)
                            t.color("White")
                            t.setheading(270)
                            t.forward(10)
                            t.color("Black")
                            t.setheading(0)
                            t.forward(4 * p_burst[i])
                            t.color("Black")
                            w_time = w_time + (text - p_burst[i] - p_arrival[i])
                            p_burst[i] = 0
                            m = m + 1
                            continue
                        zizo = 0
                        for j in range(0, i):
                            if p_burst[j] != 0:
                                zizo = zizo + 1
                        if p_arrival[i] > text and zizo != 0:
                            continue
                        if p_arrival[i] > text:
                            idle = p_arrival[i] - text
                            text_idle = text + idle
                            t.color("Red")
                            t.setheading(0)
                            t.forward(5 * idle)
                            t.setheading(90)
                            t.forward(50)
                            t.setheading(180)
                            t.forward(5 * idle)
                            t.setheading(270)
                            t.forward(50)
                            t.setheading(0)
                            t.forward(5 * idle)
                            t.color("White")
                            t.setheading(270)
                            t.forward(30)
                            t.color("Red")
                            style = ('Courier', 12)
                            text_idle = round(text_idle, 2)
                            t.write(str(text_idle), font=style)
                            t.color("White")
                            t.setheading(90)
                            t.forward(30)
                            t.setheading(180)
                            t.forward(4.5 * idle)
                            t.setheading(90)
                            t.forward(10)
                            t.color("Red")
                            style = ('Courier', 12)
                            t.write("IDLE", font=style)
                            t.color("White")
                            t.setheading(270)
                            t.forward(10)
                            t.color("Red")
                            t.setheading(0)
                            t.forward(4.5 * idle)
                            idle_total = idle_total + idle
                            text = text + idle
                        t.color("Black")
                        t.setheading(0)
                        t.forward(coff * q)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(coff * q)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(coff * q)
                        text = text + q  # text
                        text = round(text, 2)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(15)
                        t.color("Black")
                        style = ('Courier', 12)
                        t.write(text, font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(0)
                        t.forward(15)
                        t.setheading(180)
                        t.forward((coff - 1) * q)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Black")
                        style = ('Courier', 20)
                        t.write(p_name[i], font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Black")
                        t.setheading(0)
                        t.forward((coff - 1) * q)
                        w_time = w_time + (text - q - p_arrival[i])
                        t.color("Black")
                        p_burst[i] = p_burst[i] - q
                        p_arrival[i] = text
                        m = m + 1
                        p_arrival[i] = text
                    for i in range(n):
                        if p_burst[i] == 0:
                            count = count - 1
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(4):  # Priority Non_preemptive
            try:
                for i in range(n):
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                            temp_priority = p_priority[i]
                            p_priority[i] = p_priority[j]
                            p_priority[j] = temp_priority
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_priority[j] < p_priority[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                        if p_arrival[j] < text:
                            if p_priority[j] < p_priority[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 15)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 15)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                    text = 0
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    while index >= 0:
                        text = text + p_burst[index]
                        index = index - 1
                    text = text + idle_total
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(15)
                    t.color("Black")
                    style = ('Courier', 12)
                    text = round(text, 2)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(0)
                    t.forward(15)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                    t.color("Black")
                avg = w_time / n
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return
        elif self.comboBox.currentText() == self.comboBox.itemText(5):  # priority(Preemptive)
            try:
                p_priority = [float(self.tableWidget.item(0, 3).text())]
                for i in range(n - 1):
                    p_priority.append(float(self.tableWidget.item(i + 1, 3).text()))
                for i in range(n):  # Non_Preemptive
                    for j in range(i, n):
                        if p_arrival[i] > p_arrival[j]:  # FCFS
                            temp_arr = p_arrival[i]
                            temp_bur = p_burst[i]
                            p_arrival[i] = p_arrival[j]
                            p_arrival[j] = temp_arr
                            p_burst[i] = p_burst[j]
                            p_burst[j] = temp_bur
                            temp_name = p_name[i]
                            p_name[i] = p_name[j]
                            p_name[j] = temp_name
                            temp_priority = p_priority[i]
                            p_priority[i] = p_priority[j]
                            p_priority[j] = temp_priority
                        if (p_arrival[i] == p_arrival[j]):
                            if (p_priority[j] < p_priority[i]):
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                text = 0
                for i in range(n):
                    for j in range(i + 1, n):
                        if p_arrival[j] <= text:
                            if p_priority[j] < p_priority[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                        if p_arrival[i] > text:
                            p_arr = text
                            p_exc = 0
                            while p_arr < p_arrival[i]:
                                p_arr = p_arr + 0.5
                                p_exc = p_exc + 0.5
                            text = text + p_exc
                        if p_arrival[j] > text and p_arrival[j] < text + p_burst[i]:
                            if p_priority[j] < p_priority[i]:
                                p_arr = text
                                p_exc = 0
                                while p_arr < p_arrival[j]:
                                    p_arr = p_arr + 0.1
                                    p_exc = p_exc + 0.1
                                p_burst[i] = p_burst[i] - p_exc
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                                p_arrival.insert(i, p_arrival[j])
                                p_burst.insert(i, p_exc)
                                p_name.insert(i, p_name[j])
                                p_priority.insert(i, p_priority[j])
                                n = n + 1
                                m = m + 1
                    text = text + p_burst[i]
                for i in range(n):
                    if p_burst[i] == 0:
                        p_burst.pop(i)
                        p_arrival.pop(i)
                        p_name.pop(i)
                        p_priority.pop(i)
                        n = n - 1
                        m = m - 1
                    else:
                        continue
                text = 0
                for i in range(n):
                    if p_burst[i] < 3:
                        coff = 15
                    elif p_burst[i] < 5:
                        coff = 10
                    elif p_burst[i] <= 10:
                        coff = 7
                    elif p_burst[i] < 50:
                        coff = 5
                    else:
                        coff = 3
                    for j in range(i + 1, n):
                        if p_arrival[j] <= text:
                            if p_priority[j] < p_priority[i]:
                                temp_arr = p_arrival[i]
                                temp_bur = p_burst[i]
                                p_arrival[i] = p_arrival[j]
                                p_arrival[j] = temp_arr
                                p_burst[i] = p_burst[j]
                                p_burst[j] = temp_bur
                                temp_name = p_name[i]
                                p_name[i] = p_name[j]
                                p_name[j] = temp_name
                                temp_priority = p_priority[i]
                                p_priority[i] = p_priority[j]
                                p_priority[j] = temp_priority
                    if p_arrival[i] > text:
                        idle = p_arrival[i] - text
                        text_idle = text + idle
                        t.color("Red")
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.setheading(90)
                        t.forward(50)
                        t.setheading(180)
                        t.forward(5 * idle)
                        t.setheading(270)
                        t.forward(50)
                        t.setheading(0)
                        t.forward(5 * idle)
                        t.color("White")
                        t.setheading(270)
                        t.forward(30)
                        t.color("Red")
                        style = ('Courier', 12)
                        text_idle = round(text_idle, 2)
                        t.write(str(text_idle), font=style)
                        t.color("White")
                        t.setheading(90)
                        t.forward(30)
                        t.setheading(180)
                        t.forward(4.5 * idle)
                        t.setheading(90)
                        t.forward(10)
                        t.color("Red")
                        style = ('Courier', 12)
                        t.write("IDLE", font=style)
                        t.color("White")
                        t.setheading(270)
                        t.forward(10)
                        t.color("Red")
                        t.setheading(0)
                        t.forward(4.5 * idle)
                        idle_total = idle_total + idle
                        text = text + idle
                    t.color("Black")
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    t.setheading(90)
                    t.forward(50)
                    t.setheading(180)
                    t.forward(coff * p_burst[i])
                    t.setheading(270)
                    t.forward(50)
                    t.setheading(0)
                    t.forward(coff * p_burst[i])
                    index = i
                    text = text + p_burst[i]
                    text = round(text, 2)
                    t.color("White")
                    t.setheading(270)
                    t.forward(30)
                    t.setheading(180)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 12)
                    t.write(text, font=style)
                    t.color("White")
                    t.setheading(0)
                    t.forward(10)
                    t.setheading(90)
                    t.forward(30)
                    t.setheading(180)
                    t.forward((coff - 1) * p_burst[i])
                    t.setheading(90)
                    t.forward(10)
                    t.color("Black")
                    style = ('Courier', 20)
                    t.write(p_name[i], font=style)
                    t.color("White")
                    t.setheading(270)
                    t.forward(10)
                    t.color("Black")
                    t.setheading(0)
                    t.forward((coff - 1) * p_burst[i])
                    t.color("Black")
                    for j in range(i + 1, n):
                        if p_name[i] == p_name[j]:
                            index = i
                            p_arrival[j] = p_arrival[j] + p_burst[i]
                    w_time = w_time + (text - p_burst[i] - p_arrival[i])
                avg = w_time / (n - m)
                avg = round(avg, 2)
                self.lineEdit_3.clear()
                self.lineEdit_3.insert(str(avg) + " ms")
                turtle.done()
            except:
                self.lineEdit_6.clear()
                self.lineEdit_6.setStyleSheet("border-color: rgb(255, 255, 127);")  # Yellow Border Colour
                self.lineEdit_6.insert("Invalid Input")
                self.lineEdit_7.setStyleSheet("border-color: rgb(32, 31, 31);")  # main border colour
                self.lineEdit_7.clear()
                return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
