from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func

# Set the api and parser of line bot
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    """
    Process the line bot get message command with @ beginning
    :param request: [WSGIRequest] http request
    :return: No return value
    """
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtex = event.message.text
                    # identify the command and act
                    if mtex == '@查課的啦!':
                        func.send_courses(event)
                    elif mtex == '@吃飯的啦!':
                        func.not_open(event)
                    elif mtex == '@回報問題的啦!':
                        func.report(event)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
