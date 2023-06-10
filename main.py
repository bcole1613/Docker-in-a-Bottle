from bottle import *



def main():
    run(host='0.0.0.0', port=8080, debug=True)

@route('/hello')
def hello():
    return "Hello World!"


# Get request
@route('/')
def get_index():
    return static_file('index.html', root=".")

@route('/css/styles.css')
def get_styles():
    return static_file('styles.css', root="./css/")

@route('/css/quartz.css')
def get_quartz():
    return static_file('quartz.css', root="./css/")

@route('/assests/img/brianna.jpeg')
def get_profile_img():
    return static_file('brianna.jpeg', root="./assets/")

@route('/js/scripts.js')
def get_js_scripts():
    return static_file('scripts.js', root="./js/")

# make a function to create a get request route for my resume page

if __name__ == "__main__":
    main()