#!/usr/bin/env python3

import os
import json
import jinja2
import asyncio
import logging
import aiohttp_jinja2
from aiohttp import web

# App settings
HOST = '0.0.0.0'
NAME = os.environ.get('APP_NAME', 'cake-app')
PORT = os.environ.get('APP_PORT', 8080)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
APP_BG = os.environ.get('APP_BG', 'powderblue')
APP_HOST = os.environ.get('HOSTNAME', 'N/A')


# Logs settings
LOG_FORMAT = "%(asctime)s %(name)s: [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "[ %Y-%m-%d %H:%M:%S ]"
ACCESS_LOG_FORMAT = f'%a - %r %s %b %Tf'
logger = logging.getLogger(NAME)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter(LOG_FORMAT, LOG_DATE_FORMAT))
console.setLevel(logging.DEBUG)
logger.addHandler(console)

def get_app_debug_info():
    return {k: v for k, v in os.environ.items()}

class DebugView(web.View):
    @aiohttp_jinja2.template('debug.html')
    async def get(self):
        return dict(cfg=get_app_debug_info())

class IndexView(web.View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        return dict(background=APP_BG, hostname=APP_HOST)

class HealthView(web.View):
    async def get(self):
        return web.Response(text=json.dumps({
            'isItWorking': 'sure',
            'envHealth': os.environ.get('APP_HEALTH_VALUE', 'N/A'),
        }, indent=2))

async def create_app():
    ''' Prepare application '''
    app = web.Application()
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
        context_processors=[aiohttp_jinja2.request_processor],)
    app.router.add_get('/', IndexView, name='index')
    app.router.add_get('/app/debug', DebugView, name='debug')
    app.router.add_get('/health/check', HealthView, name='healthchk')
    app.router.add_static('/static', path=STATIC_DIR, name='static')
    return app

if __name__ == '__main__':
    logger.debug(f'Start server {HOST}:{PORT}')
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(create_app())
    web.run_app(app, access_log=logger, access_log_format=ACCESS_LOG_FORMAT, host=HOST, port=int(PORT))
