from django.conf import settings as st
from linebot import LineBotApi, WebhookParser


line_bot_api = LineBotApi(st.LINE_ACCESS_TOKEN)
parser = WebhookParser(st.LINE_ACCESS_SECRET)


def get_profile(line_id):
    try:
        return line_bot_api.get_profile(line_id)
    except:
        return {}


def events_parse(request):
    return parser.parse(
        request.body.decode('utf-8'),
        request.META['HTTP_X_LINE_SIGNATURE'])
