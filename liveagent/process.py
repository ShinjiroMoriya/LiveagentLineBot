def process_message(message):
    if message.get('type') == 'ChatMessage':
        status = 'message'
        return [status, message['message']['text']]
    elif message.get('type') == 'ChatEnded':
        status = 'end'
        return [status, '接続が終了しました。']
    elif message.get('type') == 'ChatRequestFail':
        status = 'fail'
        return [status, 'ただいま接続できません。']
    elif message.get('type') == 'ChatRequestSuccess':
        status = 'ok'
        return [status, None]
    # elif message.get('type') == 'AgentTyping':
    #     pass
    # elif message.get('type') == 'AgentNotTyping':
    #     pass
    # elif message.get('type') == 'AgentDisconnect':
    #     pass
    # elif message.get('type') == 'ChasitorSessionData':
    #     pass
    # elif message.get('type') == 'ChatEstablished':
    #     pass
    # elif message.get('type') == 'ChatTransferred':
    #     pass
    # elif message.get('type') == 'CustomEvent':
    #     pass
    # elif message.get('type') == 'NewVisitorBreadcrumb':
    #     pass
    # elif message.get('type') == 'QueueUpdate':
    #     pass
    # elif message.get('type') == 'FileTransfer':
    #     pass
    # elif message.get('type') == 'Availability':
    #     pass

    return [None, None]
