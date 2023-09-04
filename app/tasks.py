from celery import shared_task
import logging

from .functions import fetch_13f_filings

logger = logging.getLogger(__name__)


@shared_task(name="fetch_filings_task")
def fetch_filings_task():
    logger.info("Succesfully fetched")
    return fetch_13f_filings()