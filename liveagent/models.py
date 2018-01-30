from django.db import models


class LiveagentSession(models.Model):
    class Meta:
        db_table = 'liveagent_session'

    line_id = models.CharField(max_length=255)
    liveagent_id = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    affinity_token = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    ack = models.IntegerField(blank=True, null=True)
    responder = models.CharField(max_length=255, default='LIVEAGENT')

    def __str__(self):
        return self.line_id

    @classmethod
    def get_by_line_id(cls, line_id):
        return cls.objects.filter(line_id=line_id).values().first()

    @classmethod
    def get_liveagent_sessions(cls):
        return cls.objects.filter(responder='LIVEAGENT').values('line_id')

    @classmethod
    def save_session(cls, data):
        new_data = cls(
            line_id=data.get('line_id'),
            liveagent_id=data.get('id'),
            key=data.get('key'),
            sequence=data.get('sequence'),
            affinity_token=data.get('affinityToken'),
        )
        new_data.save()
        return cls.get_by_line_id(line_id=data.get('line_id'))

    @classmethod
    def update_session(cls, data):
        cls.objects.filter(line_id=data.get('line_id')).update(**data)
        return cls.get_by_line_id(line_id=data.get('line_id'))

    @classmethod
    def delete_session(cls, line_id):
        cls.objects.filter(line_id=line_id).update(**{
            'key': None,
            'affinity_token': None,
            'sequence': 1,
            'responder': 'BOT',
        })

    @classmethod
    def get_session(cls, line_id):
        session = cls.get_by_line_id(line_id)
        return session if session is not None else {}
