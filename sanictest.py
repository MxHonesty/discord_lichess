from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger

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
    return json({'functionat' : 'da'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000)
