class HelloWorld:

  def __init__(self):
    self.msg = ''

  def hello(self, failme):
    if failme:
      try:
        f = open("hello_world.xxx", "r")
      except Exception as e:
          self.msg = e
    else:
      self.msg = 'Hello World'

    return self.msg
