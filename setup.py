from distutils.core import setup

setup (name='queue',
       version='0.1',
       url='http://code.google.com/p/batch-queue/',
       author='Neal Becker',
       author_email='ndbecker2@gmail.com',
       packages=['queue_server'],
       package_data={'queue_server' : ['queue.tac']},
       scripts=['queue']
       )
