from sanic import Sanic
from sanic.response import json, text, html
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
    logger.info('-------------------------Test-------------------------')
    return html('Nume bot: ' + bot.get_client_name())

@app.route('/servers')
async def servers(request):
    pagina = ''
    for server in bot.get_servers():
        pagina = pagina + server.name + '<br>'
    return html(pagina)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = False)
