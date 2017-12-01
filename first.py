import web
# import MySQLdb
# import MySQLdb.cursors

render = web.template.render('templates')

urls = (
    # '/(.*)', 'hello'
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello',
)
# app = web.application(urls, globals())

class index:
    def GET(self):
        query = web.input()
        return web.seeother('http://www.douban.com/')

class blog:
    def POST(self):
        data = web.input()
        return data
    def GET(self):
        return web.ctx.env

class hello:
    def GET(self, name):
        return render.hello2('zhourong')

if __name__ == "__main__":
    app.run()
