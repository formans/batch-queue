from queue_server.server import Spawner

from twisted.web import server
from twisted.application import service, internet

application = service.Application("Demo application")
spawn_server = server.Site(Spawner())
service = internet.TCPServer(7080, spawn_server)
service.setServiceParent(application)
