from json import JSONEncoder
from predixcan import PREDIX_PATH, execute_predixcan_method,parse_predixcan_results

from flask import Flask, render_template, url_for, request, redirect, jsonify
import json
from flask_cors import CORS

# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

server = Flask(__name__)
# without line below angular my throw an error: 'Access-Control-Allow-Origin' header is present on the requested resource. angular'
CORS(server)

# server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(server)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Task %r>' % self.id

# class Message(JSONEncoder):
#     def __init__(self,gene,beta,t,p,se_beta):
#         self.gene = gene
#         self.beta = beta
#         self.t = t
#         self.p = p
#         self.se_beta = se_beta
#
#     def default(self, o):
#         return o.__dict__
#
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__,
#                           sort_keys=False, indent=4)



@server.route('/predixcan', methods=['POST', 'GET'])
def index():
    print('Received message')

    gene_list = parse_predixcan_results()
    json_string = json.dumps([ob.__dict__ for ob in gene_list])
    print(json_string)

    return (json_string)
    # if request.method == 'POST':
    #     task_content = request.form['content']
    #     new_task = Todo(content=task_content)
    #
    #     try:
    #         db.session.add(new_task)
    #         db.session.commit()
    #         return redirect('/')
    #     except:
    #         return 'There was an issue adding your task'
    #
    # else:
    #     tasks = Todo.query.order_by(Todo.date_created).all()
    #     return render_template('index.html', tasks=tasks)

#
# @server.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)
#
#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'
#
# @server.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)
#
#     if request.method == 'POST':
#         task.content = request.form['content']
#
#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your task'
#
#     else:
#         return render_template('update.html', task=task)


if __name__ == "__main__":
    # execute_predixcan_method()
    server.run(debug=True)
