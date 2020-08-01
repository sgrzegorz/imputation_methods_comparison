from flask import Flask, render_template, url_for, request, redirect, jsonify
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

server = Flask(__name__)
# server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(server)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Task %r>' % self.id

class Message():
    gene = 'ENSG00000000457.9'
    beta = '2970.08804905987'
    t ='0.492865446389667'
    p = '0.622828377402499'
    se_beta ='0.622828377402499'


@server.route('/', methods=['POST', 'GET'])
def index():
    print('Received message')
    m = Message()
    m1 = Message()
    array = [m,m1]
    jsonify(array)
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
    server.run(debug=True)
