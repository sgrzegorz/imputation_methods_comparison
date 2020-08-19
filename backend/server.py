from backend.predixcan import parse_predixcan_results

from flask import Flask, request,send_file
import json
from flask_cors import CORS

# from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
# without line below angular my throw an error: 'Access-Control-Allow-Origin' header is present on the requested resource. angular'
CORS(server)



@server.route('/predixcan', methods=['POST', 'GET'])
def index():
    print('Received message')

    gene_list = parse_predixcan_results()
    json_string = json.dumps([ob.__dict__ for ob in gene_list])
    print(json_string)

    return (json_string)

#http://example.com/metaxcan?id=1
@server.route('/metaxcan', methods=['POST', 'GET'])
def metaxcan():
    if request.args.get('id') == '1':
        id =request.args.get('id')
        filename = f'pictures/metaxcan{id}.png'
    else:
        filename = 'error.gif'
    return send_file(filename, mimetype='image/png')


@server.route('/tigar', methods=['POST', 'GET'])
def tigar():
    pass

@server.route('/fusion', methods=['POST', 'GET'])
def fusion():
    pass

if __name__ == "__main__":
    # execute_predixcan_method()
    server.run(debug=True)
