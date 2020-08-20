from backend.predixcan import parse_predixcan_results

from flask import Flask, request,send_file
import json
from flask_cors import CORS
import backend.plots
# from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
# without line below angular my throw an error: 'Access-Control-Allow-Origin' header is present on the requested resource. angular'
CORS(server)

#_run_plots_function('metaxcan2')
def _run_plots_function(function_beginning):
    function_name = 'not_found'
    for name in dir(backend.plots):
        if name.startswith(function_beginning):
            function_name = name
            break
    if function_name!='not_found':
        getattr(backend.plots, function_name)()
        return 0
    return -1

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
    if isinstance(int(request.args.get('id')),int):
        id =request.args.get('id')
        if _run_plots_function(f'metaxcan{id}') == -1:
            print('No function for picture found')
        filename = f'pictures/metaxcan{id}.png'
    else:
        filename = 'pictures/error.png'
    return send_file(filename, mimetype='image/png')


@server.route('/tigar', methods=['POST', 'GET'])
def tigar():
    pass

@server.route('/fusion', methods=['POST', 'GET'])
def fusion():
    if isinstance(int(request.args.get('id')), int):
        id = request.args.get('id')
        if _run_plots_function(f'fusion{id}') == -1:
            print('No function for picture found')
        filename = f'pictures/fusion{id}.png'
    else:
        filename = 'pictures/error.png'
    return send_file(filename, mimetype='image/png')




if __name__ == "__main__":
    # execute_predixcan_method()
    server.run(debug=True)
    # _run_plots_function('metaxcan2')
    # result = getattr(backend.plots,'metaxcan1_pvalue_and_pred_perf_r2_plot')()
    # result = getattr(backend.plots,'metaxcan2_pvalue_histogram_plot')()
    #


    print()
