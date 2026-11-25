import sys
from PyQt5.QtWidgets import QApplication
from toDoList import ToDoListApp


app = QApplication(sys.argv)
Ventana = ToDoListApp()
Ventana.show()
sys.exit(app.exec())
