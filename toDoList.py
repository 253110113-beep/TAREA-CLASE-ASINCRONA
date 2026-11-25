
from PyQt5 import QtWidgets, uic

class ToDoListApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    
        uic.loadUi('toDoList.ui', self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnActualizar.clicked.connect(self.ActualizarTarea)

    def AgregarTarea(self):
        tarea = self.edtTarea.text().strip()
        if tarea != "":
            self.lstTareas.addItem(tarea)
            self.edtTarea.clear()
        self.edtTarea.setFocus()

    def EliminarTarea(self):
        indiceTareaBorrar = self.lstTareas.currentRow()
        if indiceTareaBorrar != -1:
            self.lstTareas.takeItem(indiceTareaBorrar)

    #profe este es mi codigo RAMOS MARTINEZ JUAN MANUEL

    def ActualizarTarea(self):
        indiceTareaActualizar = self.lstTareas.currentRow()
        nuevaTarea = self.edtTarea.text().strip()
        if indiceTareaActualizar != -1 and nuevaTarea != "":
            self.lstTareas.item(indiceTareaActualizar).setText(nuevaTarea)
            self.edtTarea.clear()
        self.edtTarea.setFocus()