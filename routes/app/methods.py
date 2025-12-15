import uuid
from datetime import date
from sqlalchemy import text
from DB.conection import conn
from flask import Flask
from flask_restx import Api, Resource, Namespace, fields

app = Flask(__name__)
api = Api(app, title='ToDo List API', version='1.0', description='API de Tarefas')

ns = Namespace('tasks', description='Operações de Tarefas')

update_ns = Namespace('update')

create_task = ns.model('Task', {
    'task_name': fields.String(required=True, description='Nome da tarefa')
})

update_task = update_ns.model('update', {
    'update_task': fields.String(required=True, description='Atualizar nome da Task'),
    'id': fields.String(required=True, description='Passar o id da tarefa para atualizar')
})

@ns.route("/get_task") 
class ApiGet(Resource):
    def get(self):
        engine = conn()
        if not engine:
            return {"error": "Falha na conexão com o BD"}, 500
            
        try:
            with engine.connect() as connection:
                result = connection.execute(text("SELECT * FROM to_do_list"))
                data = [{"id": row[0], "name": row[1]} for row in result]
                
                return {
                    "success": True,
                    "count": len(data),
                    "data": data
                }, 200
                
        except Exception as e:
            return {"error": str(e)}, 500

@ns.route('/create_task')
class CreateTask(Resource):
    @ns.expect(create_task, validate=True)
    def post(self):
        engine = conn()
        if not engine:
            return {"error": "Falha na conexão com o BD"}, 500
        
        payload = ns.payload
        name_task_input = payload.get('task_name')
        
        new_id = str(uuid.uuid4())
        current_date = date.today()
        
        try:
            with engine.connect() as connection:
                query = text("""
                    INSERT INTO public.to_do_list (id, name_task, data_created) 
                    VALUES (:id, :name, :date)
                """)
                
                connection.execute(query, {
                    "id": new_id, 
                    "name": name_task_input, 
                    "date": current_date
                })
                connection.commit()
            
            return {'message': 'Tarefa criada com sucesso!', 'id': new_id, 'Tarefa' : name_task_input}, 201

        except Exception as e:
            return {"error": f"Erro ao inserir: {str(e)}"}, 500


@update_ns.route('/update_task')
class UpdateTask(Resource):
    @update_ns.expect(update_task, validate=True)
    def put(self):
        payload = update_ns.payload
        task_id = payload.get('id')
        new_task_name = payload.get('update_task')

        engine = conn()

        try:
            with engine.connect() as connection:
                query = text("""
                    UPDATE public.to_do_list
                    SET name_task = :name
                    WHERE id = :id
                """)                
                connection.execute(query, {
                    "id": task_id, 
                    "name": new_task_name
                })
                connection.commit()
            
            return {'message': 'Tarefa criada com sucesso!', 'id': task_id, 'Tarefa' : new_task_name}, 200

        except Exception as e:
            return {"error": f"Erro ao inserir: {str(e)}"}, 500
api.add_namespace(ns)
api.add_namespace(update_ns)

if __name__ == '__main__':
    app.run(debug=True)
