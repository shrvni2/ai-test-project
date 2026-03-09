```python
import unittest
from unittest.mock import patch, MagicMock
from main import main
from github_agent import GitHubAgent

class TestMain(unittest.TestCase):

    @patch('main.logging')
    @patch('main.sys')
    @patch('main.GitHubAgent')
    def test_main(self, mock_github_agent, mock_sys, mock_logging):
        mock_github_agent.return_value.run.return_value = None
        main()
        mock_logging.basicConfig.assert_called_once()
        mock_github_agent.assert_called_once()
        mock_github_agent.return_value.run.assert_called_once()

    @patch('main.logging')
    @patch('main.sys')
    @patch('main.GitHubAgent')
    def test_main_exception(self, mock_github_agent, mock_sys, mock_logging):
        mock_github_agent.return_value.run.side_effect = Exception('Test exception')
        main()
        mock_logging.error.assert_called_once()
        mock_sys.exit.assert_called_once_with(1)

    @patch('main.logging')
    @patch('main.sys')
    @patch('main.GitHubAgent')
    def test_main_runtime_error(self, mock_github_agent, mock_sys, mock_logging):
        mock_github_agent.return_value.run.side_effect = RuntimeError('Test runtime error')
        main()
        mock_logging.error.assert_called_once()
        mock_sys.exit.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()
```