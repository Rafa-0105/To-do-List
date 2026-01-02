import uuid
from uuid import UUID
from datetime import date
from sqlalchemy import text
from DB.conection import conn
from flask import Flask
from flask_restx import Api, Resource, Namespace, fields

app = Flask(__name__)
api = Api(app, title='To Do List API', version='1.3', description='Task API')

create_ns = Namespace('create')
update_ns = Namespace('update')
delete_ns = Namespace('delete')
select_ns = Namespace('task')

create_task = create_ns.model('create', {
    'task_name': fields.String(required=True, description='Name Task')
})

update_task = update_ns.model('update', {
    'update_task': fields.String(required=True, description='Update name task'),
    'id': fields.String(required=True, description='Pass ID to update task')
})

delete_task = delete_ns.model('delete', {
    'id': fields.String(required=True, description='Pass ID to delete task')
})

@select_ns.route("/get_task") 
class ApiGet(Resource):
    def get(self):
        engine = conn()
        if not engine:
            return {"error": "Erro to connection to BD"}, 500
            
        try:
            with engine.connect() as connection:
                result = connection.execute(text("SELECT * FROM to_do_list"))
                data = [{"id": str(row[0]), "name": row[1]} for row in result]
                
                return {
                    "success": True,
                    "count": len(data),
                    "data": data
                }, 200
                
        except Exception as e:
            return {"error": str(e)}, 500

@create_ns.route('/create_task')
class CreateTask(Resource):
    @create_ns.expect(create_task, validate=True)
    def post(self):
        engine = conn()
        if not engine:
            return {"error": "Erro to connection to BD"}, 500
        
        payload = create_ns.payload
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
            
            return {'message': 'Task successfully created', 'id': new_id, 'Tarefa' : name_task_input}, 201

        except Exception as e:
            return {"error": f"Error to insert: {str(e)}"}, 500


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
            
            return {'message': 'Task successfully updated', 'id': task_id, 'Tarefa' : new_task_name}, 200

        except Exception as e:
            return {"error": f"Error to insert : {str(e)}"}, 500
        
@delete_ns.route('/delete_task')
class DeleteTask(Resource):
    @delete_ns.expect(delete_task, validate=True)
    def delete(self):
        payload = delete_ns.payload
        task_id = payload.get('id')
        print(task_id)

        engine = conn()

        try:
            with engine.connect() as connection:
                query = text("""
                    DELETE FROM public.to_do_list
                    WHERE id = :id
                """)
                connection.execute(query, {
                    "id": task_id
                })
                connection.commit()
            return {'message': 'Task successfully deleted!', 'id': task_id}, 200
        except Exception as e:
            return {"error": f"Error to delete: {str(e)}"}, 500

api.add_namespace(select_ns)
api.add_namespace(update_ns)
api.add_namespace(delete_ns)
api.add_namespace(create_ns)

if __name__ == '__main__':
    app.run(debug=True)
