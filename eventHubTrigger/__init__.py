import json
import logging
import azure.functions as func


def main(event: func.EventHubEvent):
    body = event.get_body().decode()
    logging.info(f"Function triggered to process a message: {body}")
    logging.info(f"  EnqueuedTimeUtc = {event.enqueued_time}")
    logging.info(f"  SequenceNumber = {event.sequence_number}")
    logging.info(f"  Offset = {event.offset}")

    result = json.loads(body)

    # result = json.dumps({
    #     'id': event.id,
    #     'data': event.get_json(),
    #     'topic': event.topic,
    #     'subject': event.subject,
    #     'event_type': event.event_type,
    # })


    logging.info("Python EventGrid trigger processed an event: {}".format(result))



