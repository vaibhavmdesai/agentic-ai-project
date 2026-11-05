from app.config import get_settings

s = get_settings()

print("AWS Endpoint URL:", s.aws_endpoint_url)