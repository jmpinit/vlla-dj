import web

urls = (
          '/', 'index'
          )
app = web.application(urls, globals())

class index:
    def GET(self):
        raise web.seeother('/static/html/index.html')

if __name__ == "__main__":
    app.run()
