from flask import Flask, render_template
import os

app = Flask(__name__)

directory = "templates"
routes = []  # Store route names

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path) and filename.endswith('.html'):
        route_name = filename[:-5]
        routes.append(route_name)
        
        def generate_route(filename):
            def route_function():
                return render_template(filename)
            return route_function
        
        app.add_url_rule(f'/{route_name}', route_name, generate_route(filename))

@app.route('/')
def home():
    route_links = "".join([f'<li><a href="/{route}">{route}</a></li>' for route in routes])
    return f'''
    <html>
    <head><title>GovWiki</title></head>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h1>Welcome to GovWiki</h1>
        <p>Here are the available types:</p>
        <ul>{route_links}</ul>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
