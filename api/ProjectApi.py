from flask_restful import Resource
import logging as logger


class ProjectApi(Resource):

    def get(self):

        logger.debug("Inside the get method")

        ProjectDetails = {
            "version" : "1.0",
            "owner"  : "SET",
            "ProjectName" : "Dockerize A Flask App"
        }


        return ProjectDetails,200