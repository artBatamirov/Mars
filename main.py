from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promote():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(lst)


@app.route('/image_mars')
def show_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.png')}>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""

@app.route('/promotion_image')
def promote_image():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']

    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src={url_for('static', filename='img/mars.png')}>
                        <div class="alert alert-secondary" role="alert">
                          <h5>{lst[0]}</h5>
                        </div>
                        <div class="alert alert-success" role="alert">
                          <h5>{lst[1]}</h5>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <h5>{lst[2]}</h5>
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <h5>{lst[3]}</h5>
                        </div>
                        <div class="alert alert-danger" role="alert">
                          <h5>{lst[4]}</h5>
                        </div>
                      </body>
                    </html>'''

@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astroform():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 align="center">Анкета претендента</h1>
                                <h2 align="center">на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="surname"  placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="education">
                                              <option>дошкольное </option>
                                              <option>начальное общее</option>
                                              <option>основное общее</option>
                                              <option>среднее общее</option>
                                              <option>среднее профессиональное</option>
                                              <option>бакалавриат</option>
                                              <option>специалитет, магистратура</option>
                                              <option>подготовка кадров высшей квалификации</option>
                                            </select>
                                         </div>
                                         <div class="form-group">
                                            <label for="form-check">Каие у Вас есть профессии?</label>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male" >
                                              <label class="form-check-label" for="profession">
                                                инженер-исследователь
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                пилот
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                строитель
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                экзобиолог
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                врач
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                инженер по терраформированию
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                климатолог
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                специалист по радиационной защите
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                астрогеолог
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                гляциолог
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                инженер жизнеобеспечения
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                метеоролог
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                оператор марсохода
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                киберинженер
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                штурман
                                              </label>
                                            </div>
                                            
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="male" value="male">
                                              <label class="form-check-label" for="profession">
                                                пилот дронов
                                              </label>
                                            </div>
                                        </div>
                                        
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
