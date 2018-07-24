from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)


def run():
    app.run(debug=True)


@app.route('/')
def index():
    """routing top
    """
    return redirect(url_for('list'))


@app.route('/list', methods=['GET'])
def list():
    """routing list
    """
    return render_template('list.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    """routing add
    """
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        return "TODO 本棚情報を追加し、本棚一覧にリダイレクト"
    else:
        return "TODO エラーハンドリング"


@app.route('/edit/<user_id>', methods=['GET', 'POST'])
def edit(user_id):
    """routing edit
    """
    if request.method == 'GET':
        return render_template('edit.html', user_id=user_id)
    elif request.method == 'POST':
        return "TODO 本棚情報を編集し、本棚一覧にリダイレクト:%s" % user_id
    else:
        return "TODO エラーハンドリング"


@app.route('/delete/<user_id>', methods=['GET', 'POST'])
def delete(user_id):
    """routing delete
    """
    if request.method == 'GET':
        return "TODO 本棚削除画面を表示:%s" % user_id
    elif request.method == 'POST':
        return "TODO 本棚情報を削除し、本棚一覧にリダイレクト:%s" % user_id
    else:
        return "TODO エラーハンドリング"


@app.route('/login', methods=['GET', 'POST'])
def login():
    """routing login
    """
    if request.method == 'GET':
        return "TODO ログイン画面を表示"
    elif request.method == 'POST':
        return "TODO ログインし、本棚一覧にリダイレクト"
    else:
        return "TODO エラーハンドリング"


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """routing logout
    """
    if request.method == 'GET':
        return "TODO ログアウト画面を表示"
    elif request.method == 'POST':
        return "TODO ログアウトし、ログイン前トップ画面にリダイレクト"
    else:
        return "TODO エラーハンドリング"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
