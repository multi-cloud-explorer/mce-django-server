try:
    import multiprocessing
    CPU_COUNT = (multiprocessing.cpu_count() * 2) +1
except:
    CPU_COUNT = 1

from decouple import config as env_config

bind = env_config('MCE_BIND', "0.0.0.0:8000")

daemon = False

#chdir = "/code"

proxy_protocol = env_config('MCE_PROXY_PROTOCOL', True, cast=bool)

proxy_allow_ips = env_config('MCE_PROXY_ALLOW_IPS', "127.0.0.1")

forwarded_allow_ips = env_config('MCE_FORWARDED_ALLOW_IPS', "*")

workers = env_config('MCE_WORKERS', CPU_COUNT, cast=int)

worker_class = env_config('MCE_WORKER_CLASS', 'gevent')

worker_connections = env_config('MCE_WORKER_CONNECTIONS', 200, cast=int)

backlog = env_config('MCE_BACKLOG', 2048, cast=int)

timeout = env_config('MCE_TIMEOUT', 30, cast=int)

keepalive = env_config('MCE_KEEPALIVE', 2, cast=int)

debug = env_config('MCE_DEBUG', False, cast=bool)

loglevel = env_config('MCE_LOG_LEVEL', 'info')

accesslog = env_config('MCE_ACCESSLOG', "-")

errorlog = env_config('MCE_ERRORLOG', "-")

syslog = env_config('MCE_SYSLOG', False, cast=bool)

if syslog:
    syslog_addr = env_config('MCE_SYSLOG_ADDR', 'udp://syslog:514')

logconfig = env_config('MCE_LOGCONFIG', None)

statsd_enable = env_config('MCE_STATSD_ENABLE', False, cast=bool)

if statsd_enable:
    statsd_host = env_config('MCE_STATSD_HOST', None)
    statsd_prefix = env_config('MCE_STATSD_PREFIX', 'mce')

def post_fork(server, worker):
    from psycogreen.gevent import patch_psycopg
    patch_psycopg()
    worker.log.info("Made Psycopg2 Green")
