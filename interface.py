from graphics import *
from utils import *
import time


def home(win):
    txt = Text(Point(400,50),"Sistema de Saúde")
    txt.setSize(20)
    txt.draw(win)
    rect = Rectangle(Point(100,200),Point(300,300))
    center = rect.getCenter()
    rect.draw(win)
    calc_2d = Text(center,"Login")
    calc_2d.setSize(15)
    calc_2d.draw(win)
    rect2 = Rectangle(Point(500,200),Point(700,300))
    center2 = rect2.getCenter()
    rect2.draw(win)
    calc_3d = Text(center2, "Registrar")
    calc_3d.setSize(15)
    calc_3d.draw(win)
    win.getMouse()


def login(win):

    clear_screen(win)
    Text(Point(200, 100), "Username:").draw(win)
    Text(Point(200, 200), "Senha:").draw(win)
    username_entry = Entry(Point(500, 100), 20)
    password_entry = Entry(Point(500, 200), 20)
    username_entry.draw(win)
    password_entry.draw(win)

    login_button = Rectangle(Point(300, 300), Point(500, 350))
    login_button.draw(win)
    Text(Point(400, 325), "Login").draw(win)

    while True:
        click_point = win.getMouse()


        if 300 <= click_point.getX() <= 500 and 300 <= click_point.getY() <= 350:
            username = username_entry.getText()
            password = password_entry.getText()
            if validate_login(username, password):
                app(win,username)
            else:
                Text(Point(400, 375), "Usuario nao registrado").draw(win)
                Text(Point(400, 400), "Redirecionando").draw(win)
                time.sleep(1)
                register(win)
                break


def register(win):
    clear_screen(win)
    Text(Point(200, 100), "Username:").draw(win)
    Text(Point(200, 200), "Senha:").draw(win)
    Text(Point(200, 300), "Tipo:").draw(win)
    username_entry = Entry(Point(500, 100), 20)
    password_entry = Entry(Point(500, 200), 20)
    type_entry = Entry(Point(500, 300), 20)
    username_entry.draw(win)
    password_entry.draw(win)
    type_entry.draw(win)
    
    register_button = Rectangle(Point(300, 350), Point(500, 400))
    register_button.draw(win)
    Text(Point(400, 375), "Registrar").draw(win)

    while True:
        click_point = win.getMouse()

        if 300 <= click_point.getX() <= 500 and 350 <= click_point.getY() <= 400:
            username = username_entry.getText()
            password = password_entry.getText()
            user_type = type_entry.getText()
            if user_exists(username):
                Text(Point(400, 500), "Usuario já registrado").draw(win)
                register_user(username,password,user_type)
                login(win)




def app(win,username):
    def input_health_info(username, age, height, blood_pressure, diabetes):
        with open('health_info.csv', 'a', newline='') as csvfile:
            csvfile.write(username + ',' + age + ',' + height + ',' + blood_pressure + ',' + diabetes + '\n')


    clear_screen(win)

    if user_type(username) == 'paciente':
    
        Text(Point(200, 50), "Peso:").draw(win)
        Text(Point(200, 100), "Altura (cm):").draw(win)
        Text(Point(200, 150), "Idade:").draw(win)
        Text(Point(200, 200), "Pressao:").draw(win)
        Text(Point(200, 250), "Glicose:").draw(win)
        Text(Point(200, 300), "Data de insercao:").draw(win)

        weigth_entry = Entry(Point(500, 50), 20)
        height_entry = Entry(Point(500, 100), 20)
        age_entry = Entry(Point(500, 150), 20)
        bp_entry = Entry(Point(500, 200), 20)
        glicose_entry = Entry(Point(500, 250), 20)
        data_de_insercao_entry = Entry(Point(500, 300), 20)

        weigth_entry.draw(win)
        height_entry.draw(win)
        age_entry.draw(win)
        bp_entry.draw(win)
        glicose_entry.draw(win)
        data_de_insercao_entry.draw(win)

        submit_button = Rectangle(Point(200, 500), Point(400, 550))
        submit_button.draw(win)
        Text(Point(300, 525), "Enviar").draw(win)
        export_button = Rectangle(Point(500, 500), Point(700, 550))
        export_button.draw(win)
        Text(Point(600, 525), "Exportar").draw(win)



        while True:
            click_point = win.getMouse()

            if 200 <= click_point.getX() <= 400 and 500 <= click_point.getY() <= 550:
                username = username
                age = age_entry.getText()
                weigth= weigth_entry.getText()
                height = height_entry.getText()
                blood_pressure = bp_entry.getText()
                glicose = glicose_entry.getText()
                data = data_de_insercao_entry.getText()
                write_user_health_data(username,weigth,height,age,blood_pressure,glicose,data)
                Text(Point(400, 575), "Informação Salva").draw(win)
                time.sleep(2)  
                app(win,username)
            elif 500 <= click_point.getX() <= 700 and 500 <= click_point.getY() <= 550:
                export_html_health_data(username)

    elif user_type(username) == 'medico':
        Text(Point(200, 100), "Paciente:").draw(win)
        patient_entry = Entry(Point(500, 100), 20)
        patient_entry.draw(win)
        submit_button = Rectangle(Point(200, 500), Point(400, 550))
        submit_button.draw(win)
        Text(Point(300, 525), "Enviar").draw(win)

        alter_button = Rectangle(Point(500, 500), Point(700, 550))
        alter_button.draw(win)
        Text(Point(600, 525), "Alterar").draw(win)

        while True:
            click_point = win.getMouse()
            patient = patient_entry.getText()
            data = get_user_health_data(patient)
            result_string = list_to_data(data)
            if 200 <= click_point.getX() <= 400 and 500 <= click_point.getY() <= 550 and user_exists(patient):
                Text(Point(win.getWidth()//2,win.getHeight()//2), result_string).draw(win)
            if 500 <= click_point.getX() <= 700 and 500 <= click_point.getY() <= 550 and user_exists(patient):
                clear_screen(win)
                row_entry = Entry(Point(500, 100), 20)
                row_entry.draw(win)
                colum_entry = Entry(Point(500, 200), 20)
                colum_entry.draw(win)
                value_entry = Entry(Point(500, 300), 20)
                value_entry.draw(win)
                Text(Point(200, 100), "Linha:").draw(win)
                Text(Point(200, 200), "Coluna:").draw(win)
                Text(Point(200, 300), "Valor:").draw(win)
                submit_button = Rectangle(Point(200, 500), Point(400, 550))
                submit_button.draw(win)
                Text(Point(300, 525), "Enviar").draw(win)
                click_point = win.getMouse()
                row = int(row_entry.getText())
                colum = int(colum_entry.getText())
                value = value_entry.getText()
                while True:
                    click_point = win.getMouse()
                    if 200 <= click_point.getX() <= 400 and 500 <= click_point.getY() <= 550:
                        alter_user_health_data(patient,row,colum,value)
                        Text(Point(400, 575), "Informação Salva").draw(win)
                        time.sleep(2)
                        app(win,username)







def begin(window):
    while True:
        mouse = window.checkMouse()
        if mouse is not None:
            x = mouse.getX()
            y = mouse.getY()
            if x >= 100 and x <= 300 and y >= 200 and y <= 300:
                login(window)
            elif x >= 500 and x <= 700 and y >= 200 and y <= 300:
                register(window)
            else:
                pass
            update(60)

def main():
    win = GraphWin("Sistema de Saúde", 800, 600)
    home(win)
    begin(win)

if __name__ == '__main__':
    main()
