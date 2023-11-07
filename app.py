from flask import Flask, render_template, request
from gpt4all import GPT4All
app = Flask(__name__)

# Define a variable to store the user input
user_input = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    model = GPT4All('mistral-7b-openorca.Q4_0.gguf')
    global user_input

    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.form['user_input']
    try:
        with model.chat_session():
            response1 = model.generate(prompt = user_input, temp=0)
            __forDisp = model.current_chat_session
    except:
        __forDisp = "[zrnlbs_err]An Error Occured with the GPT Model !"
        
    return render_template('index.html', user_output=__forDisp)

if __name__ == '__main__':
    app.run(debug=True)
 