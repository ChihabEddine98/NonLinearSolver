from tests.Tester import Tester
from gui.App import *




if __name__ == '__main__':

    app=Application()
    app.mainloop()

    # Tests Des méthodes :


    guiApp=Application()
    guiApp.mainloop()
    tester=Tester()
    tester.test()

    