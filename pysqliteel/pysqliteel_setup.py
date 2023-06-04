import os
import shutil

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content=None):
    with open(path, 'w') as file:
        if content:
            file.write(content)

app_py = """
import eel
import modules.exposed

if __name__ == "__main__":
    eel.init("web") 
    eel.start('index.html')"""

index_html = """
<!DOCTYPE html>
<html>
<head>
  <title>Botón</title>
  <script src="js/exposed.js"></script>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
  <button>Click me!</button>
</body>
</html>
"""

style_css ="""
head {
  background-color: #f2f2f2;
  padding: 10px;
}

title {
  color: #333333;
  font-size: 20px;
}

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
"""

exposed_js = """
$(document).ready(function() {
  $('button').click(async function() {
    alert('Clicked!');    
    await eel.mostrar_mensaje('Clicked!')();
  });
});
"""

exposed_py = """
import eel
@eel.expose
def mostrar_mensaje(mensaje):
    print(mensaje)
"""

# Crear la estructura de carpetas
create_folder('modules')
create_folder('data')
create_folder('web')
create_folder('web/js')
create_folder('web/css')

# Crear archivos
create_file('app.py', app_py)
create_file('setup.py')
create_file('LICENCE')
create_file('README.md')
create_file('modules/__init__.py')
create_file('modules/exposed.py', exposed_py)
create_file('data/__init__.py')
create_file('data/database.py')
create_file('data/settings.py')
create_file('web/index.html', index_html)
create_file('web/js/exposed.js', exposed_js)
create_file('web/css/style.css', style_css)

print("Estructura de carpetas y archivos creada exitosamente.")
