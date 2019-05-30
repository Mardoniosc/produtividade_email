from view.FrmPrincipal import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = FrmPrincipal()
    widget.show()
    sys.exit(app.exec())