# Импортируем необходимые модули из Flask
from flask import Flask, render_template, request, redirect, url_for

# Создаем экземпляр Flask приложения
app = Flask(__name__)

# Инициализируем пустой список для хранения задач
tasks = []

# Определяем маршрут для главной страницы
@app.route('/')
def index():
    # Отображаем шаблон index.html и передаем список задач
    return render_template('index.html', tasks=tasks)

# Определяем маршрут для добавления новой задачи
@app.route('/add', methods=['POST'])
def add_task():
    # Получаем задачу из формы
    task = request.form.get('task')
    if task:
        # Добавляем задачу в список задач
        tasks.append({'title': task, 'completed': False})
    # Перенаправляем на главную страницу
    return redirect(url_for('index'))

# Определяем маршрут для завершения задачи
@app.route('/complete/<int:task_index>')
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        # Отмечаем задачу как завершенную
        tasks[task_index]['completed'] = True
    # Перенаправляем на главную страницу
    return redirect(url_for('index'))

# Определяем маршрут для удаления задачи
@app.route('/delete/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        # Удаляем задачу из списка
        tasks.pop(task_index)
    # Перенаправляем на главную страницу
    return redirect(url_for('index'))

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True, port=8000)
