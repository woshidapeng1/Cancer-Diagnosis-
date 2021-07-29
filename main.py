from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QFileDialog
import os


from lib.share import SI


class MainWindow:
    def __init__(self):
        qfile_MainWindow = QFile(
            "../../Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/8fdc6df7727db684caee9d5fbd34443a/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/OpenData/Archive 2/ui/MainWindow.ui")
        qfile_MainWindow.open(QFile.ReadOnly)
        qfile_MainWindow.close()

        self.ui = QUiLoader().load(qfile_MainWindow)

        self.ui.Upload.clicked.connect(self.click_Upload)
        self.ui.Archive.clicked.connect(self.click_Archive)
        self.ui.Library.clicked.connect(self.click_Library)
        self.ui.Setting.clicked.connect(self.click_Library)

    def click_Upload(self):
        SI.upload = Upload()
        SI.upload.ui.show()
        self.ui.close()

    def click_Archive(self):
        SI.archive = Archive()
        SI.archive.ui.show()
        self.ui.close()

    def click_Library(self):
        SI.library = Library()
        SI.library.ui.show()
        self.ui.close()

    def click_Setting(self):
        SI.setting = Setting()
        SI.setting.ui.show()
        self.ui.close()


class Upload:
    def __init__(self):
        qfile_MainWindow = QFile("ui/UploadImage.ui")
        qfile_MainWindow.open(QFile.ReadOnly)
        qfile_MainWindow.close()

        self.ui = QUiLoader().load(qfile_MainWindow)

        self.ui.start.clicked.connect(self.click_start)
        self.ui.back.clicked.connect(self.click_back)
        self.ui.select.clicked.connect(self.click_select)



    def click_start(self):
        os.system('python test.py')
        SI.start = start()
        SI.start.ui.show()
        self.ui.close()

    def click_back(self):
        SI.mainWin = MainWindow()
        SI.mainWin.ui.show()
        self.ui.close()

    def click_select(self):
        filePath, _ = QFileDialog.getOpenFileNames(
            self.ui,
            "Choose your Image",
            r"d:\\data",
            "type(*.png *.jpg *.bmp)"
        )


class Archive:
    def __init__(self):
        qfile_MainWindow = QFile("ui/untitled.ui")
        qfile_MainWindow.open(QFile.ReadOnly)
        qfile_MainWindow.close()

        self.ui = QUiLoader().load(qfile_MainWindow)
        self.ui.back.clicked.connect(self.click_back)

    def click_back(self):
        SI.mainWin = MainWindow()
        SI.mainWin.ui.show()
        self.ui.close()


class Library:
    def __init__(self):
        qfile_MainWindow = QFile("ui/Library.ui")
        qfile_MainWindow.open(QFile.ReadOnly)
        qfile_MainWindow.close()


        self.ui = QUiLoader().load(qfile_MainWindow)
        self.ui.back.clicked.connect(self.click_back)

    def click_back(self):
        SI.mainWin = MainWindow()
        SI.mainWin.ui.show()
        self.ui.close()


class Setting:
    def __init__(self):
        qfile_MainWindow = QFile("ui/Setting.ui")
        qfile_MainWindow.open(QFile.ReadOnly)
        qfile_MainWindow.close()

        self.ui = QUiLoader().load(qfile_MainWindow)
        self.ui.back.clicked.connect(self.click_back)

    def click_back(self):
        SI.mainWin = MainWindow()
        SI.mainWin.ui.show()
        self.ui.close()


class start:
    def __init__(self):
        qfile_MainWindow = QFile("ui/Result.ui")
        qfile_MainWindow.open(QFile.ReadOnly)
        qfile_MainWindow.close()

        self.ui = QUiLoader().load(qfile_MainWindow)
        self.ui.back.clicked.connect(self.click_back)
        self.ui.speech.clicked.connect(self.click_speech)

    def click_back(self):
        SI.upload = Upload()
        SI.upload.ui.show()
        self.ui.close()

    def click_speech(self):
        os.system('python speech.py')



app = QApplication([])
SI.mainWin = MainWindow()
SI.mainWin.ui.show()
app.exec_()
