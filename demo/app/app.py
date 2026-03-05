import os
import re

import json

import boto3
from flask import Flask, jsonify, request

app = Flask(__name__)

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _get_sqs_client():
    return boto3.client("sqs", region_name=os.environ.get("AWS_REGION"))


def _enqueue_email(email: str, subject: str, body: str) -> None:
    queue_url = os.environ.get("SQS_QUEUE_URL")
    if not queue_url:
        raise RuntimeError("SQS_QUEUE_URL is not set")
    payload = {
        "recipients": [email],
        "subject": subject,
        "body": body,
    }
    _get_sqs_client().send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(payload),
    )

@app.route("/", methods=["GET"])
def index():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>SQS Subscribe Demo</title>
        <style>
          :root {
            --bg: #f3f8f5;
            --panel: #ffffff;
            --text: #163321;
            --muted: #4b6354;
            --accent: #1d7f4e;
            --accent-hover: #17653f;
            --ring: rgba(29, 127, 78, 0.2);
          }

          * {
            box-sizing: border-box;
          }

          body {
            margin: 0;
            min-height: 100vh;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            color: var(--text);
            background:
              radial-gradient(circle at 10% 10%, #d9efe0 0%, transparent 36%),
              radial-gradient(circle at 90% 20%, #eaf5ef 0%, transparent 30%),
              var(--bg);
            display: grid;
            place-items: center;
            padding: 24px;
          }

          .card {
            width: 100%;
            max-width: 560px;
            background: var(--panel);
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 16px 34px rgba(20, 49, 34, 0.08);
          }

          h1 {
            margin: 0 0 10px;
            font-size: clamp(1.5rem, 4vw, 2rem);
            line-height: 1.2;
          }

          p {
            margin: 0 0 20px;
            color: var(--muted);
            line-height: 1.5;
          }

          form {
            display: grid;
            gap: 12px;
          }

          label {
            font-size: 0.95rem;
            font-weight: 600;
          }

          input[type="email"] {
            width: 100%;
            border: 1px solid #c9ddcf;
            border-radius: 10px;
            padding: 12px 14px;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.15s ease, box-shadow 0.15s ease;
          }

          input[type="email"]:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 4px var(--ring);
          }

          button {
            border: 0;
            border-radius: 10px;
            background: var(--accent);
            color: #fff;
            padding: 12px 16px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: background 0.15s ease;
          }

          button:hover {
            background: var(--accent-hover);
          }

          .hint {
            margin-top: 14px;
            font-size: 0.9rem;
            color: var(--muted);
          }
        </style>
      </head>
      <body>
        <main class="card">
          <h1>DevOps Serverless Subscribe Demo</h1>
          <p>Enter your email to queue a subscription message through SQS.</p>
          <form method="post" action="/subscribe">
            <label for="email">Email address</label>
            <input id="email" type="email" name="email" placeholder="you@example.com" required />
            <button type="submit">Subscribe</button>
          </form>
          <div class="hint">You will receive a confirmation email from SNS.</div>
        </main>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({"ok": True})


@app.route("/subscribe", methods=["POST"])
def subscribe():
    if request.content_type and "application/json" in request.content_type:
        payload = request.get_json(silent=True) or {}
        email = (payload.get("email") or "").strip()
        subject = (payload.get("subject") or "SUCCESS - MPCS 56550 Intro to DevOps - Demo Presentation").strip()
        body = (payload.get("body") or "Serverless computing is amazing").strip()
    else:
        email = (request.form.get("email") or "").strip()
        subject = "SUCCESS - MPCS 56550 Intro to DevOps - Demo Presentation"
        body = "Serverless computing is amazing"

    if not email or not EMAIL_RE.match(email):
        return jsonify({"error": "invalid email"}), 400

    try:
        _enqueue_email(email, subject, body)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

    if request.content_type and "application/json" in request.content_type:
        return jsonify({"status": "queued", "email": email}), 200
    return f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Subscription Queued</title>
        <style>
          body {{
            margin: 0;
            min-height: 100vh;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: #f3f8f5;
            color: #163321;
            display: grid;
            place-items: center;
            padding: 24px;
          }}
          .panel {{
            width: 100%;
            max-width: 560px;
            background: #fff;
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 16px 34px rgba(20, 49, 34, 0.08);
          }}
          h1 {{
            margin: 0 0 10px;
            font-size: 1.7rem;
          }}
          p {{
            margin: 0 0 12px;
            line-height: 1.5;
            color: #4b6354;
          }}
          a {{
            display: inline-block;
            margin-top: 8px;
            color: #1d7f4e;
            font-weight: 600;
            text-decoration: none;
          }}
          a:hover {{
            text-decoration: underline;
          }}
        </style>
      </head>
      <body>
        <main class="panel">
          <h1>Subscription Queued</h1>
          <p><strong>{email}</strong> has been queued successfully.</p>
          <p>Check your inbox to confirm the SNS subscription.</p>
          <a href="/">Queue another email</a>
        </main>
      </body>
    </html>
    """, 200
