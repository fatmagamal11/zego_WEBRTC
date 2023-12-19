from flask import Flask, render_template
# , request, jsonify
# import your_ai_module  # Replace with the actual name of your AI module
print("hiiiiiiiiiiiiiiiiiiiii")
app_skill = Flask(__name__)

@app_skill.route('/')
def index():
    # return "hello"
    return render_template('index.html')

# @app.route('/api/perform_ai', methods=['POST'])
# def perform_ai():
#     data = request.get_json()
#     input_data = data['input_data']
#     result = your_ai_module.perform_ai(input_data)
#     return jsonify({'result': result})

if __name__ == '__main__':
    app_skill.run(debug=True,port=9000)
