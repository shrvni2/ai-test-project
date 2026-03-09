```python
# tests/test_config.py
import os
import pytest
from config.config import Config

def test_config_init():
    config = Config()
    assert config.get_github_token() is None
    assert config.get_github_username() is None
    assert config.get_github_repo() is None
    assert config.get_log_level() == 'INFO'
    assert config.get_schedule_interval() == 60

def test_config_get_github_token():
    os.environ['GITHUB_TOKEN'] = 'test_token'
    config = Config()
    assert config.get_github_token() == 'test_token'
    del os.environ['GITHUB_TOKEN']

def test_config_get_github_username():
    os.environ['GITHUB_USERNAME'] = 'test_username'
    config = Config()
    assert config.get_github_username() == 'test_username'
    del os.environ['GITHUB_USERNAME']

def test_config_get_github_repo():
    os.environ['GITHUB_REPO'] = 'test_repo'
    config = Config()
    assert config.get_github_repo() == 'test_repo'
    del os.environ['GITHUB_REPO']

def test_config_get_log_level():
    os.environ['LOG_LEVEL'] = 'DEBUG'
    config = Config()
    assert config.get_log_level() == 'DEBUG'
    del os.environ['LOG_LEVEL']

def test_config_get_schedule_interval():
    os.environ['SCHEDULE_INTERVAL'] = '30'
    config = Config()
    assert config.get_schedule_interval() == 30
    del os.environ['SCHEDULE_INTERVAL']

def test_config_get_schedule_interval_invalid():
    os.environ['SCHEDULE_INTERVAL'] = 'invalid'
    with pytest.raises(ValueError):
        Config()
    del os.environ['SCHEDULE_INTERVAL']

def test_config_get_schedule_interval_negative():
    os.environ['SCHEDULE_INTERVAL'] = '-1'
    with pytest.raises(ValueError):
        Config()
    del os.environ['SCHEDULE_INTERVAL']

# tests/test_main.py
import logging
import sys
from unittest.mock import patch, MagicMock
from main import main

def test_main():
    with patch('main.GitHubAgent') as mock_agent:
        mock_agent.return_value.run.return_value = None
        main()
        mock_agent.return_value.run.assert_called_once()

def test_main_error():
    with patch('main.GitHubAgent') as mock_agent:
        mock_agent.return_value.run.side_effect = Exception('Test error')
        with patch('sys.exit') as mock_exit:
            main()
            mock_exit.assert_called_once_with(1)

def test_main_logging():
    with patch('logging.basicConfig') as mock_logging:
        main()
        mock_logging.assert_called_once_with(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# tests/test_github_agent.py
import pytest
from unittest.mock import patch, MagicMock
from github_agent import GitHubAgent

def test_github_agent_init():
    agent = GitHubAgent()
    assert agent is not None

def test_github_agent_run():
    with patch('github_agent.GitHubAgent.run') as mock_run:
        agent = GitHubAgent()
        agent.run()
        mock_run.assert_called_once()
```