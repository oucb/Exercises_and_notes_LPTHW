import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        form = web.input(name='Nobody', greet=None)
        greeting = "%s, %s" % (form.name, form.greet)

        return render.index(greeting)

if __name__ == "__main__":
    app.run()