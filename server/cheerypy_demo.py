import cherrypy

class HelloWorld:
    # CherryPy 绝不会发布未将 `expose` 属性设置为 `True` 的方法
    # 在 Web 中公开 index 方法
    @cherrypy.expose
    def index(self):
        # CherryPy 将为根 URI（"/"）调用此方法，并将其返回值发送给客户端
        return "Hello World!"

# 在尝试将请求 URI 映射到对象时，CherryPy 始终以 `app.root` 开始，
# 因此我们需要挂载请求处理程序根。 对 `'/'` 的请求将映射到 `HelloWorld().index()`。
cherrypy.config.update({ 
    'server.socket_port': 8077,
    # 'log.screen': True,
    # 'log.error_log.propagate': False,
    # 'log.access_log.propagate': False,
    # 'log.access_file': '',
    # 'log.error_file': ''
})
# cherrypy.log.error_log.propagate = False
# cherrypy.log.access_log.propagate = False
cherrypy.quickstart(HelloWorld())
