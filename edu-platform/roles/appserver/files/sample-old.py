import falcon
import mysql.connector
import os


class UserResource:

    def on_get(self, req, resp):

        resp.content_type = 'text/html'

        try:

            config = {
                'user': 'educationx_db',
                'password': os.environ['databasepassword'],
                'host': 'dbserver',
                'database': 'educationx_db',
            }

            cnx = mysql.connector.connect(**config)

        except mysql.connector.Error as err:
            resp.body = '<html><head><title>Error</title></head><body><h1>Oooops! Error!</h1><p></p></body></html>'
            return

        cursor = cnx.cursor()
        query = ('SELECT `id`, `name`, `last_name` FROM `users` ORDER BY RAND() LIMIT 1')



        cursor.execute(query)

        result=''

        for (id, name, last_name) in cursor:
            result += '{}, {} has ID {}'.format(
                name, last_name, id)

        resp.body = '<html><head><title>Results</title></head><body><h1>Got results!</h1><p>' + result + '</p></body></html>'

        cursor.close()
        cnx.close()



app=falcon.API()
app.add_route('/', UserResource)
