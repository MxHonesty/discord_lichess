from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger

import bot

app = Sanic(__name__)

@app.route('/')
async def test(request):
    logger.info('Accesat')
    logger.info(request.url)
    logger.info(request.args)
    return json({'hello' : 'world'})

@app.route('/test')
async def salut(request):
    logger.info('Test')
    return json({'nume' : bot.client.user})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
