#!/usr/bin/env python
import web
import os, sys, signal
from subprocess import Popen, call

urls = (
          '/', 'index',
          '/ctrl/(.*)', 'ctrl'
          )
app = web.application(urls, globals())

shaderPath = "./static/shaders/"
fragShader = "/tmp/frag.glsl"

class index:
    def GET(self):
        render = web.template.render('templates')
        return render.index(get_shaders())

class ctrl:
    def POST(self, url):
        play_shader(shaderPath + url)
        return "starting " + url

def signal_handler(signal, frame):
    try:
        shader.terminate()
        print "killed vlla-shader"
    except Exception as e:
        print e

    sys.exit(0)

def play_shader(file):
    if os.path.isfile(file):
        call(["cp", file, fragShader])
        print "updated frag.glsl with " + file
    else:
        print "shader file " + file + " does not exist"

def get_shaders():
    shaderFiles = [ f for f in os.listdir(shaderPath) if os.path.isfile(os.path.join(shaderPath, f)) ]
    return shaderFiles

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    defaultShader = shaderPath + get_shaders()[0]
    play_shader(defaultShader)

    global shader
    #shader = Popen(["vlla-shader", fragShader])

    app.run()
