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

# make a function to create a get request route for my resume page

if __name__ == "__main__":
    main()