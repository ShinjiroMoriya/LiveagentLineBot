import json
import requests
import random
from django.conf import settings as st
from liveagent.models import LiveagentSession as Session
from liveagent.process import process_message
from linebot.models import (TextSendMessage, TemplateSendMessage,
                            ConfirmTemplate, PostbackTemplateAction)
from line.utils import line_bot_api as lba
from celery import shared_task


@shared_task
def get_messages(line_id):
    session = Session.get_by_line_id(line_id=line_id)

    url = st.LIVEAGENT_HOST + '/chat/rest/System/Messages'
    headers = {
        'X-LIVEAGENT-API-VERSION': st.LIVEAGENT_API_VERSION,
        'X-LIVEAGENT-AFFINITY': session.get('affinity_token'),
        'X-LIVEAGENT-SESSION-KEY': session.get('key'),
    }
    r = requests.get(url, headers=headers, params={
        'ack': session.get('ack', -1)
    })
    try:
        res_type = None
        result = None
        if r.status_code == 200:
            body = json.loads(r.text)
            for message in body.get('messages'):
                res_type, result = process_message(message)

            if res_type == 'end' or res_type == 'fail':
                Session.delete_session(session.get('line_id'))
            else:
                Session.update_session({
                    'line_id': session.get('line_id'),
                    'ack': body.get('sequence'),
                })

            if result is not None:
                lba.push_message(line_id, TextSendMessage(text=result))

            get_messages.delay(line_id)

        elif r.status_code == 204:
            get_messages.delay(line_id)

    except:
        get_messages.delay(line_id)


@shared_task
def reply_connect(reply_token):
    lba.reply_message(reply_token, TemplateSendMessage(
        alt_text='接続しますか？',
        template=ConfirmTemplate(
            text='接続しますか？',
            actions=[
                PostbackTemplateAction(label='はい', data='connect'),
                PostbackTemplateAction(label='いいえ', data='no_connect'),
            ]
        )
    ))


@shared_task
def reply_text(reply_token, text=None):
    if text is None:
        rep_text = [
            '良い天気だね', 'ナイス！', 'わお', 'はい？', '面白い事言うね',
            'それ良いね', 'やってみよう', 'なんですか？', '知らないです。',
            'また明日！',
        ]
        text = random.choice(rep_text)
    lba.reply_message(reply_token, TextSendMessage(
        text=text,
    ))
