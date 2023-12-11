#!/usr/bin/env python3

import asyncio
from aiohttp import web

# Env ettings
HOST = '0.0.0.0'
PORT = 8080


async def start(request):
    return web.Response(text=f"Welcome to example app deployed on Kubernetes :)")

async def create_app():
    ''' Prepare application '''
    app = web.Application()
    app.router.add_get('/', start, name='start')
    return app

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(create_app())
    web.run_app(app, host=HOST, port=PORT)
