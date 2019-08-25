from flask import Flask, jsonify, request, render_template
import logging
#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder="templates")

@app.route('/hello')
def hello_world():
	return jsonify({'ip': request.remote_addr}), 200
@app.route('/')
def root():
	logging.info('aaa')
	return render_template('index.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)