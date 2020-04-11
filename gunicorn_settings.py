# TODO: attention ne sera pas lancé par djangoq cluster !!!!!

from psycogreen.gevent import patch_psycopg

def post_fork(server, worker):
    patch_psycopg()
    worker.log.info("Made Psycopg2 Green")
