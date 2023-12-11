#!/usr/bin/env python3

import asyncio
import logging
from aiohttp import web

# App ettings
NAME = 'cake-app'
HOST = '0.0.0.0'
PORT = 8080

# Logs settins
LOG_FORMAT = "%(asctime)s %(name)s: [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "[ %Y-%m-%d %H:%M:%S ]"
ACCESS_LOG_FORMAT = f'%a - %r %s %b %Tf'
logger = logging.getLogger(NAME)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter(LOG_FORMAT, LOG_DATE_FORMAT))
console.setLevel(logging.DEBUG)
logger.addHandler(console)


async def start(request):
    return web.Response(text=f"Welcome to example app deployed on Kubernetes :)")

async def create_app():
    ''' Prepare application '''
    app = web.Application()
    app.router.add_get('/', start, name='start')
    return app

if __name__ == '__main__':
    logger.debug(f'Start server {HOST}:{PORT}')
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(create_app())
    web.run_app(app, access_log=logger, access_log_format=ACCESS_LOG_FORMAT, host=HOST, port=PORT)
