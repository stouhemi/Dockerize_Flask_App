from flask_restful import Api 
from app import flaskAppInstance
from .ProjectApi import ProjectApi


restServerInstance = Api(flaskAppInstance)


restServerInstance.add_resource(ProjectApi,"/")