

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        self.click = 10000
        self.pushButton.clicked.connect(self.plus_click)

    def plus_click(self):
        self.label.setText(str(int(self.label.text())+self.click))

        class ProgressBarApp(QWidget):
            def __init__(self):
                super().__init__()

                # Настройка основного окна
                self.setWindowTitle('progress')
                self.setGeometry(100, 100, 300, 200)

                # Создание прогресс-бара
                self.progress_bar = QProgressBar(self)
                self.progress_bar.setValue(0)  # Начальное значение прогресс-бара
                layout.addWidget(self.progress_bar)

                # Создание кнопки
                self.button = QPushButton('Увеличить прогресс', self)
                self.button.clicked.connect(self.increase_progress)  # Подключение сигнала к слоту
                layout.addWidget(self.button)

                # Установка лэйаута для основного окна
                self.setLayout(layout)

            def increase_progress(self):
                # Получаем текущее значение прогресс-бара
                current_value = self.progress_bar.value()

                # Увеличиваем значение на 10
                new_value = current_value + 10

                # Проверяем, не превышает ли новое значение 100
                if new_value > 100:
                    new_value = 100

                # Устанавливаем новое значение прогресс-бара
                self.progress_bar.setValue(new_value)

        if __name__ == '__main__':
            app = QApplication(sys.argv)

            # Создание и отображение приложения
            window = ProgressBarApp()
            window.show()

            # Запуск главного цикла приложения
            sys.exit(app.exec())

app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec()

