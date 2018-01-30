import os
import platform
from celery import Celery


if 'local' in platform.node():
    try:
        import dotenv

        BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dotenv.read_dotenv(BASE + '/.env')
    except ImportError:
        pass
    except Exception:
        pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'line.settings')
app = Celery('line')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
