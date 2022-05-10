import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from database import Database
import Parsik
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


        db = Database()

        row = db.cursorObj.execute('''SELECT *
               FROM users''').fetchone()
        if row is not None:
            self.other_func(db)
        else:
            Parsik.Paarser



    def other_func(self,db):
        self.table = QtWidgets.QTableView()
        rows = db.cursorObj.execute('''SELECT *
               FROM users''').fetchall()
        if rows is not None:
            data = [rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9]]
            self.model = TableModel(data)
            self.table.setModel(self.model)
            self.setCentralWidget(self.table)

app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()