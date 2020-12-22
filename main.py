# test.py by Cocca Guo at 2020/12/22 14:25:58

import os
import sys
import configparser

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

import pySPM
from sxm_converter import sxm2png


class Main_window(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Main_window,self).__init__(parent)
        self.initialize()
        

    def initialize(self):
        self.setWindowTitle("SXM File Viewer")
        # self.setWindowState(Qt.WindowMaximized)
        self.resize(1000, 1000)
        self.setWindowIcon(QIcon('icon.png'))
        self.setup_config()
        self.setup_menu()
        self.setCentralWidget(QtWidgets.QWidget())


    # this func only loads once when program starts
    def setup_config(self):
        self.current_file = None
        self.current_dir = None
        self.cfg = configparser.ConfigParser()
        self.cfg.read("config.ini")


    def refresh_config(self):
        with open("config.ini", "w+") as f:
            self.cfg.write(f)  


    def setup_menu(self):
        self.m_file = QtWidgets.QMenu("File")
        self.m_tool = QtWidgets.QMenu("Tool")
        self.m_about = QtWidgets.QMenu("About")

        self.m_file_open = QtWidgets.QAction("Open", self.m_file)
        self.m_file_open.triggered.connect(self.open_file)
        self.m_file.addAction(self.m_file_open)

        self.m_file_opendir = QtWidgets.QAction("Open Folder", self.m_file)
        self.m_file_opendir.triggered.connect(self.open_folder)
        self.m_file.addAction(self.m_file_opendir)

        self.m_tool_save_pic = QtWidgets.QAction("Save Figure", self.m_tool)
        self.m_tool_save_pic.triggered.connect(self.save_pic)
        self.m_tool.addAction(self.m_tool_save_pic)

        self.m_about_about = QtWidgets.QAction("About", self.m_about)
        self.m_about_about.triggered.connect(self.about)
        self.m_about.addAction(self.m_about_about)

        self.menuBar().addMenu(self.m_file)
        self.menuBar().addMenu(self.m_tool)
        self.menuBar().addMenu(self.m_about)


    def open_file(self):
        fileName_choose, _ = QtWidgets.QFileDialog.getOpenFileName(self,  "Choose file",  self.cfg.get("file", "last_file"),  "SXM Files (*.sxm)")
        if fileName_choose == "": return
        self.cfg.set("file", "last_file", fileName_choose)
        self.refresh_config()
        self.current_file = fileName_choose
        self.sxm_show()


    def open_folder(self):
        folder_choose = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose Folder", self.cfg.get("file", "last_dir"))
        if folder_choose == "": return
        self.cfg.set("file", "last_dir", folder_choose)
        self.refresh_config()
        self.current_dir = folder_choose
        self.sxm_folder_show()


    def save_pic(self):
        if self.current_file is None: 
            QtWidgets.QMessageBox.information(self, "Infomation", "please open a file first.", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)
            return
        fname = QtWidgets.QFileDialog.getSaveFileName(self, "Save Figure", self.cfg.get("file", "output_dir"), "Image Files (*.png)")     
        if fname[0]:
            sxm2png.save(self.current_file, fname[0])


    def about(self):
        infor = self.cfg.get("about", "info")
        QtWidgets.QMessageBox.information(self, "About", infor, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)


    def sxm_show(self):
        plt.cla()
        fig = plt.figure()
        ax =fig.add_axes([0.1,0.1,0.8,0.8])
        sxm = pySPM.SXM(self.current_file)
        channel = self.cfg.get("plot", "channel")
        cmap = self.cfg.get("plot", "cmap")
        sxm.get_channel(channel).show(cmap=cmap, ax=ax)
        canvas = FigureCanvas(fig)
        self.setCentralWidget(canvas)

    
    def sxm_folder_show(self):
        dir_list = os.listdir(self.current_dir)
        self.current_file = os.path.join(self.current_dir, dir_list[0]) # temp
        self.sxm_show()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.show()
    app.exec()