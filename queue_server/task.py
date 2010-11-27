class Task (object):
    def __init__ (self, args, user, num, path, env={}, log_stdout=None, log_stderr=None, notify=None):
        self.args = args
        self.user = user
        self.path = path
        self.env = env
        self.num = num
        self.log_stdout = log_stdout
        self.log_stderr = log_stderr
        self.notify = notify
        self.pid = None
    def __repr__ (self):
        return '%s,%s,%s' % (self.args,self.pid,self.num)
    
