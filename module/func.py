from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage,\
    StickerSendMessage, LocationSendMessage, QuickReply,\
    QuickReplyButton, MessageAction

from module.search_course import find_available, get_ntust_general_courses, output_result

# Set the api of line bot
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def send_courses(event):
    """
    Send a message of the courses data
    :param event: [WebhookPayload] Line bot event
    :return: None return value
    """
    try:
        message = TextSendMessage(
            text='目前尚有名額的課程:\n'+output_result(find_available(get_ntust_general_courses()))
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Error'))


def not_open(event):
    """
    Send the message that this function is not open
    :param event: [WebhookPayload] Line bot event
    :return: None return value
    """
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此功能尚未開放\n誠摯邀請您與我們一起努力\n此專案的Gitlab:\nhttp'
                                                                           '://gitlab.aiden-lai.studio/root/brandon'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Error'))


def report(event):
    """
    Send the message that how to report problem
    :param event: [WebhookPayload] Line bot event
    :return: None return value
    """
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='回報問題請直接到此專案的Issues回報\n此專案的Gitlab:\nhttp'
                                                                           '://gitlab.aiden-lai.studio/root/brandon'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Error'))
