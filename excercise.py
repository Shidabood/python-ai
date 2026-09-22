class APIconfig:
    def __init__(self, api_key, model, max_tokens, min_tokens):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.min_tokens = min_tokens
        self.error_log = []

    def validate_email(self, email):
                if '@' not in email:
                    self.error_log.append(f"invalid email: {email}")
                    return False
                return True

openai_API = APIconfig(api_key='openai-key1', model='Astra-6', max_tokens=1000000, min_tokens=100000)

openai_API.validate_email("a.com")

openai_API.error_log