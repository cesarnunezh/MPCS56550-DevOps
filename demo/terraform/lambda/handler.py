import json
import os

import boto3
from botocore.exceptions import ClientError

ses = boto3.client("ses")


def handler(event, context):
    """
    Trigger: SQS
    Each record is one message. Body should be JSON.
    Uses partial batch response so one bad message doesn't retry the whole batch.
    """
    default_sender = os.environ["MAIL_DEFAULT_SENDER"]

    batch_item_failures = []

    for record in event.get("Records", []):
        msg_id = record["messageId"]

        try:
            payload = json.loads(record["body"])

            recipients = payload["recipients"]
            subject = payload["subject"]
            body = payload["body"]
            sender = payload.get("sender") or default_sender

            if not isinstance(recipients, list):
                recipients = [recipients]

            response = ses.send_email(
                Destination={"ToAddresses": recipients},
                Message={
                    "Body": {"Text": {"Charset": "UTF-8", "Data": body}},
                    "Subject": {"Charset": "UTF-8", "Data": subject},
                },
                Source=sender,
            )

        except (KeyError, json.JSONDecodeError) as e:
            # Bad payload: mark as failed so it retries (and eventually goes to DLQ)
            batch_item_failures.append({"itemIdentifier": msg_id})

        except ClientError:
            # SES failure: also retry / DLQ
            batch_item_failures.append({"itemIdentifier": msg_id})

        except Exception:
            batch_item_failures.append({"itemIdentifier": msg_id})

    # This tells Lambda+SQS which messages failed (only those will be retried)
    return {"batchItemFailures": batch_item_failures}
