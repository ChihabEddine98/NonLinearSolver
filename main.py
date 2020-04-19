from tests.Tester import Tester
from gui.App import *
import sys
from PyQt5 import QtWidgets



if __name__ == '__main__':
    # Tests Des méthodes :

    guiApp=Application()
    guiApp.mainloop()
    tester=Tester()
    tester.test()
    