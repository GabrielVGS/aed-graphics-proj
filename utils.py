from csvParser import CSVParser



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
    user_health_data = []
    data = get_data('userData/user_health_data.csv')
    user_column = data['usuario']
    peso_column = data['peso']
    altura_column = data['altura']
    idade_column = data['idade']
    pressao_column = data['pressao']
    glicose_column = data['glicose']
    data_de_insercao = data['data_de_insercao']

    for user, peso, altura, idade, pressao, glicose, data_de_insercao in zip(user_column, peso_column, altura_column, idade_column, pressao_column, glicose_column, data_de_insercao):
        if user == username:
            user_health_data.append([peso, altura, idade, pressao, glicose, data_de_insercao])
    return user_health_data

def write_user_health_data(username,peso,altura,idade,pressao,glicose,data_de_insercao):
    with open('userData/user_health_data.csv', 'a', newline='') as csvfile:
        csvfile.write(username + ',' + peso + ',' + altura + ',' + idade + ',' + pressao + ',' + glicose + ',' + data_de_insercao + '\n')

def alter_user_health_data(username, value, row=None, column=None):
    # Assuming you have a CSV file named "user_health_data.csv"
    csv_file = CSVParser("userData/user_health_data.csv")

    # Find the index of the user in the complete dataset
    user_indices = [i for i, row_data in enumerate(csv_file.data) if row_data[0] == username]

    if user_indices:
        for user_index in user_indices:
            if row is not None and column is not None:
                # Update a specific cell in the complete dataset
                csv_file.data[user_index][column] = str(value)
            else:
                # Update the entire row for the user
                csv_file.data[user_index] = [str(value) for _ in range(len(csv_file.data[user_index]))]

        # Write the updated complete dataset back to the CSV file
        csv_file.write_csv(csv_file.data)
        print(f"User '{username}' health data updated.")
    else:
        print(f"User '{username}' not found in the dataset.")

    



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

file = CSVParser('userData/user_health_data.csv')

def find_user_index(username):
    if len(file.data) == 0:
        return None
    
    headers = file.data[0]
    if "usuario" in headers:
        user_index = headers.index("usuario")
        for i, row in enumerate(file.data[1:], start=1):
            if row[user_index] == username:
                return i
    return None