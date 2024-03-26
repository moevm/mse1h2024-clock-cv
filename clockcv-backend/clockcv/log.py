import logging
import sys

from clockcv.middlewares import request_id_contextvar


def make_log_record_factory():
    prev_factory = logging.getLogRecordFactory()

    def log_record_factory(*args, **kwargs):
        record = prev_factory(*args, **kwargs)
        record.request_id = request_id_contextvar.get("")
        return record

    return log_record_factory


def setup_logging(level=logging.INFO):
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        style="{",
        format=(
            "{asctime} [{levelname:.1}] [{name:^16}] [{request_id}] {message}"
        ),
    )
    logging.setLogRecordFactory(make_log_record_factory())
