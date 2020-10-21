#Docker Installation

Configure the sqlconfig.xml.example file

Run the following command with the name of the database container to link:

docker run -it -d --name dsweb1 --link {db.container} dsweb

