#to generate requirements.txt file
pip freeze > requirements.txt


#create image from Dockerfile
docker build -t Flask_image2022:latest .

#run container from the new image
docker container run -it -d -p 5001:5000 --name Flask2022 flask_image2022:latest