output "alb_hostname" {
  value = "${aws_alb.main.dns_name}:${var.app_port}"
}

output "sqs_queue_url" {
  value = aws_sqs_queue.inbound.url
}

output "sqs_queue_arn" {
  value = aws_sqs_queue.inbound.arn
}
