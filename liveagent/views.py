from django.views.generic import View
from django.http import HttpResponse
from liveagent.models import LiveagentSession as Session
from liveagent.tasks import get_messages, reply_text
from liveagent.services import send_message, connect_liveagent
from line.utils import events_parse
from linebot.models import MessageEvent


class LineCallbackView(View):
    @staticmethod
    def get(_):
        return HttpResponse()

    @staticmethod
    def post(request):
        events = events_parse(request)

        for event in events:
            line_id = event.source.sender_id
            reply_token = event.reply_token

            try:
                if isinstance(event, MessageEvent):
                    if event.message.type != 'text':
                        return HttpResponse()

                    message = event.message.text
                    session = Session.get_session(line_id)

                    if session.get('responder') == 'LIVEAGENT':
                        res = send_message(line_id, message)
                        if res is False:
                            reply_text.delay(
                                reply_token, 'もう一度送ってください。')
                        else:
                            get_messages.delay(line_id)

                    else:
                        if event.message.text == '接続':
                            reply_text.delay(reply_token, 'お待ちください。')
                            is_connect = connect_liveagent(line_id)
                            if is_connect is True:
                                get_messages.delay(line_id)

                            else:
                                reply_text.delay(
                                    reply_token,
                                    ('担当者が席をはずしておりますので、\n'
                                     '時間をあけて再度お呼び出しください。'))
                        else:
                            reply_text.delay(reply_token)

            except:

                reply_text(reply_token,
                           ('障害が発生しております。\n'
                            '時間をあけて再度ご利用ください。'))

        return HttpResponse()
