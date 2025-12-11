from flask import Flask
from flask_restx import Api, Resource
from DB.conection import conn
from sqlalchemy import text

app = Flask(__name__)
api = Api(app)

@api.route("/teste", methods=['GET'])
class api_get(Resource):
    def get(self):
        engine = conn()
        if not engine:
            return {"error": "Falha na conexão"}, 500
            
        try:
            with engine.connect() as connection:
                result = connection.execute(text("SELECT * FROM teste"))
                results = result.fetchall()
                
                data = [{"name": row[0], "password": row[1]} for row in results]
                
                return {
                    "success": True,
                    "count": len(data),
                    "data": data
                }, 200
                
        except Exception as e:
            return {"error": str(e)}, 500
