import sys

from PyQt5.QtWidgets import QApplication

from calc.cl_controller import PyCalcCtrl
from calc.cl_model import evaluateExpression
from calc.cl_view import PyCalcUi


def main():
    """Main function."""
    calc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    sys.exit(calc.exec_())


if __name__ == '__main__':
    main()
