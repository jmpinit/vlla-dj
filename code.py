#!/usr/bin/env python
import web
import os, sys, signal
from subprocess import Popen, call

urls = (
          '/', 'index'
          )
app = web.application(urls, globals())

shaderPath = "./static/shaders/"
fragShader = "/tmp/frag.glsl"

class index:
    def GET(self):
        render = web.template.render('templates')
        return render.index(get_shaders())
        #raise web.seeother('/static/html/index.html')

def signal_handler(signal, frame):
    try:
        shader.terminate()
        print "killed vlla-shader"
    except Exception as e:
        print e

    sys.exit(0)

def get_shaders():
    shaderFiles = [ f for f in os.listdir(shaderPath) if os.path.isfile(os.path.join(shaderPath, f)) ]
    return shaderFiles

if __name__ == "__main__":
    global shader

    signal.signal(signal.SIGINT, signal_handler)
    
    defaultShader = shaderPath + get_shaders()[0]
    call(["cp", defaultShader, fragShader])
    print "Starting " + defaultShader

    #shader = Popen(["vlla-shader", fragShader])

    app.run()
