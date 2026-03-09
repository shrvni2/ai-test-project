```python
import os

class Config:
    def __init__(self):
        self.GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
        self.GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME')
        self.GITHUB_REPO = os.environ.get('GITHUB_REPO')
        self.LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
        self.SCHEDULE_INTERVAL = int(os.environ.get('SCHEDULE_INTERVAL', 60))

    def get_github_token(self):
        return self.GITHUB_TOKEN

    def get_github_username(self):
        return self.GITHUB_USERNAME

    def get_github_repo(self):
        return self.GITHUB_REPO

    def get_log_level(self):
        return self.LOG_LEVEL

    def get_schedule_interval(self):
        return self.SCHEDULE_INTERVAL

config = Config()
```