import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar

class ProgressBarApp(QWidget):
    def __init__(self):
        super().__init__()

        # Настройка основного окна
        self.setWindowTitle('Прогресс Бар Пример')
        self.setGeometry(100, 100, 300, 200)

        # Создание вертикального лэйаута
        layout = QVBoxLayout()

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