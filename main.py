```python
import logging
import sys
from github_agent import GitHubAgent

def main():
    try:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        agent = GitHubAgent()
        agent.run()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```