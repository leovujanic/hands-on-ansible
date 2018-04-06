import falcon
import MySQLdb
import os


class UserResource:
    def on_get(self, req, resp):

        resp.content_type = 'text/html'

        try:

            db = MySQLdb.connect(host='dbserver', user='educationx_db', passwd=os.environ['databasepassword'],
                                 db='educationx_db')

        except Exception as exc:
            resp.body = '<html><head><title>Error</title></head><body><h1>Oooops! Error!</h1><p>' + str(exc) +'</p></body></html>'
            return

        cursor = db.cursor()
        cursor.execute('SELECT `id`, `name`, `last_name` FROM `users` ORDER BY RAND() LIMIT 1')
        data = cursor.fetchone()

        result='{}, {} has ID {}'.format(
            data[1], data[2], data[0])

        resp.body = '<html><head><title>Results</title></head><body><h1>Got results!</h1><p>' + result + '</p></body></html>'


app = falcon.API()
app.add_route('/', UserResource())
