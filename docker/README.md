#Docker Installation

Configure the sqlconfig.xml.example file and rename sqlconfig.xml

Run the following command to build the image:

docker build . -t dsweb

Run the following command with the name of the database container to link to start the container:

docker run -it -d --name dsweb1 --link {db.container} dsweb

