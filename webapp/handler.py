@app.route("/")
def index():
    """routing top
    """
    return redirect(url_for('handler.index'))


@handler.route("/")
def index():
    """routing handler top
    """
    return 'handler.index'
