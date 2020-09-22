from PySide2 import QtWidgets, QtCore
from movie import get_movies
from movie import Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ciné club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connexions()
    
    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit(self)
        self.btn_addmovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("supprimer le(s) film(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addmovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)

    def setup_connexions(self):
        self.btn_addmovie.clicked.connect(self.add_movie)

        self.btn_removeMovies.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)




    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False
        
        movie = Movie(title=movie_title)
        result = movie.add_to_movies()

        if result:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)
            
        self.le_movieTitle.setText("")


    def remove_movie(self):
        
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()

            # retire depuis son 
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))







app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
