import web

urls = (
    '/(.*)', 'index'
)
#This line says we want the URL / (i.e. the front page) to be handled by the class named index.

app = web.application(urls, globals())
render = web.template.render('templates/')

class index(object):
    def GET(self, name):
#        name = 'Bob'
#        return render.index(name)
#        i = web.input(name=None)
        return render.index(name)
#        greeting = "Hello World"
#        return render.foo(greet = greeting)



if __name__ == "__main__":
    app.run()