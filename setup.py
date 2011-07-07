from distutils.core import setup

setup (name='batch-queue',
       version='0.4',
       url='http://code.google.com/p/batch-queue/',
       author='Neal Becker',
       author_email='ndbecker2@gmail.com',
       packages=['queue_server'],
       package_data={'queue_server' : ['queue.tac']},
       scripts=['queue'],
       description='simple batch queuing system',
       install_requires = ['twisted']
       )
