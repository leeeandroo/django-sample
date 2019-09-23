"""An extended version of the log_settings module from zamboni:
https://github.com/jbalogh/zamboni/blob/master/log_settings.py
"""

import logging
import logging.handlers
import os.path

from logging.config import dictConfig


class RemoteAddressFormatter(logging.Formatter):
    """Formatter that makes sure REMOTE_ADDR is available."""

    def format(self, record):
        if ('%(REMOTE_ADDR)' in self._fmt
                and 'REMOTE_ADDR' not in record.__dict__):
            record.__dict__['REMOTE_ADDR'] = None
        return logging.Formatter.format(self, record)


class UTF8SafeFormatter(RemoteAddressFormatter):
    """UTF-8 formatter with REMOTE_ADDR support."""
    def __init__(self, fmt=None, datefmt=None, encoding='utf-8'):
        logging.Formatter.__init__(self, fmt, datefmt)
        self.encoding = encoding

    def formatException(self, e):
        r = logging.Formatter.formatException(self, e)
        if type(r) is bytes:
            r = r.decode(self.encoding, 'replace')  # Convert to unicode
        return r

    def format(self, record):
        return RemoteAddressFormatter.format(self, record)


class NullHandler(logging.Handler):
    """NULL logging handler."""
    def emit(self, record):
        pass


def initialize_logging(syslog_tag, syslog_facility, loggers,
                       log_level=logging.INFO, use_syslog=False):
    """Initialize project's logging."""
    syslog_device = None
    if os.path.exists('/dev/log'):
        syslog_device = '/dev/log'
    elif os.path.exists('/var/run/syslog'):
        syslog_device = '/var/run/syslog'

    use_syslog = use_syslog if syslog_device is not None else False

    base_fmt = ('%(name)s:%(levelname)s %(message)s')

    cfg = {
        'version': 1,
        'filters': {},
        'formatters': {
            'debug': {
                '()': UTF8SafeFormatter,
                'datefmt': '%Y-%m-%d %H:%M:%s',
                'format': '%(asctime)s ' + base_fmt,
            },
            'prod': {
                '()': UTF8SafeFormatter,
                'datefmt': '%H:%M:%s',
                'format': '%s: [%%(REMOTE_ADDR)s] %s' % (syslog_tag, base_fmt),
            },
        },
        'handlers': {
            'console': {
                '()': logging.StreamHandler,
                'formatter': 'debug'
            },
            'null': {
                '()': NullHandler,
            },
            'syslog': {
                '()': logging.handlers.SysLogHandler,
                'facility': syslog_facility,
                'address': syslog_device,
                'formatter': 'prod',
            },
        },
        'loggers': {
        }
    }

    if use_syslog:
        cfg["handlers"]["syslog"] = {
            '()': logging.handlers.SysLogHandler,
            'facility': syslog_facility,
            'address': syslog_device,
            'formatter': 'prod',
        }

    for key, value in loggers.items():
        cfg[key].update(value)

    # Set the level and handlers for all loggers.
    for logger in cfg['loggers'].values():
        if 'handlers' not in logger:
            logger['handlers'] = ['syslog' if use_syslog else 'console']
        if 'level' not in logger:
            logger['level'] = log_level
        if 'propagate' not in logger:
            logger['propagate'] = False

    dictConfig(cfg)
