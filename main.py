from tests.Tester import Tester
from gui.App import *


if __name__ == '__main__':

   # Affichage graphique:
    app = Application()
    app.mainloop()

   # Tests Des méthodes en affichage console :
    tester = Tester()
    tester.test()
