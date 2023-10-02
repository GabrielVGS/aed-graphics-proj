from csvParser import CSVParser
import os


_headers = ['peso,altura,idade,pressao,hematocrito,hemoglobina,eritrocitos,data_de_insercao']


def user_credentials():
    _user_credentials = {}

    data = CSVParser('userData/user_data.csv')
    user_column = data['usuario']
    password_column = data['senha']

    for user, password in zip(user_column, password_column):
        _user_credentials[user] = password
    
    return _user_credentials


def get_data(file):
    data = CSVParser(file)
    return data

def clear_screen(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def user_exists(username):
    data = get_data('userData/user_data.csv')
    user_column = data['usuario']

    if username in user_column:
        return True
    else:
        return False

def validate_login(username, password):
    credentials = user_credentials()
    if username in credentials:
        if credentials[username] == password:
            return True
        else:
            return False
    else:
        return False

def user_type(username):
    data = get_data('userData/user_data.csv')
    user_column = data['usuario']
    type_column = data['tipo']
    for user, type in zip(user_column, type_column):
        if user == username:
            return type
    return None


def register_user(username,password,type):
    data = get_data('userData/user_data.csv')  
    if user_exists(username):
       return False 
    else:
        with open('userData/user_data.csv', 'a', newline='') as csvfile:
            csvfile.write(username + ',' + password + ',' + type + '\n')
        return True

def get_user_health_data(username):
    #check if file has headers, if has, return user data, else add headers
    user_health = []
    if not file_exists(f"userData/user_health/{username}_health_data.csv"):
        with open(f"userData/user_health/{username}_health_data.csv", 'w') as csvfile:
            csvfile.write('peso,altura,idade,pressao,hematocrito,hemoglobina,eritrocitos,data_de_insercao\n')
            return user_health
    else:
        with open(f"userData/user_health/{username}_health_data.csv", 'r') as csvfile:
            for row in csvfile:
                user_health.append(row.strip().split(','))


    return user_health


    



def render_html_health_data(username):
    user_health_data = get_user_health_data(username)
    html = "<table border=1>"
    html += "<tr><th>Peso</th><th>Altura</th><th>Idade</th><th>Pressão</th><th>Glicose</th><th>Data de Inserção</th></tr>"
    for data in user_health_data:
        html += "<tr>"
        for value in data:
            html += "<td>" + value + "</td>"
        html += "</tr>"
    html += "</table>"
    return html

def render_full_html():
    data = get_data('userData/user_health_data.csv')
    user_column = data['usuario']
    peso_column = data['peso']
    altura_column = data['altura']
    idade_column = data['idade']
    pressao_column = data['pressao']
    glicose_column = data['glicose']
    data_de_insercao = data['data_de_insercao']

    html = "<table border=1>"
    html += "<tr><th>Usuário</th><th>Peso</th><th>Altura</th><th>Idade</th><th>Pressão</th><th>Glicose</th><th>Data de Inserção</th></tr>"
    for user, peso, altura, idade, pressao, glicose, data_de_insercao in zip(user_column, peso_column, altura_column, idade_column, pressao_column, glicose_column, data_de_insercao):
        html += "<tr>"
        html += "<td>" + user + "</td>"
        html += "<td>" + peso + "</td>"
        html += "<td>" + altura + "</td>"
        html += "<td>" + idade + "</td>"
        html += "<td>" + pressao + "</td>"
        html += "<td>" + glicose + "</td>"
        html += "<td>" + data_de_insercao + "</td>"
        html += "</tr>"
    html += "</table>"

    with open('userData/html_export/full_health_data.html', 'w') as file:
        file.write(html)


def export_html_health_data(username):
    html = render_html_health_data(username)
    with open(f'userData/html_export/{username}_health_data.html', 'w') as file:
        file.write(html)
    return True


def write_user_health_data(username,peso,altura,idade,pressao,glicose,data_de_insercao):
    #check if file exists, if not, create it
    if not file_exists(f"userData/user_health/{username}_health_data.csv"):
        with open(f"userData/user_health/{username}_health_data.csv", 'w') as csvfile:
            csvfile.write('peso,altura,idade,pressao,glicose,data_de_insercao\n')
            csvfile.write(f'{peso},{altura},{idade},{pressao},{glicose},{data_de_insercao}\n')
    else:
        with open(f"userData/user_health/{username}_health_data.csv", 'a', newline='') as csvfile:
            csvfile.write(f'{peso},{altura},{idade},{pressao},{glicose},{data_de_insercao}\n')



def alter_user_health_data(username,row,colum,value):
    data = get_user_health_data(username)
    data[row][colum] = value
    with open(f'userData/user_health/{username}_health_data.csv', 'r+', newline='') as csvfile:
        for row in data:
            csvfile.write(','.join(row) + '\n')



def file_exists(filepath):
    if os.path.exists(filepath):
        return True
    else:
        with open(filepath, 'w') as file:
            return False



def list_to_data(list):
    return "\n".join(", ".join(item for item in sublist) for sublist in list)
