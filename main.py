from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def profession(prof):
    return render_template('index.html',title='Заготовка', prof=prof)

@app.route('/list_prof/<style>')
def show_list(style):
    lst = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
           'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
           'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list.html', style=style, lst=lst)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
