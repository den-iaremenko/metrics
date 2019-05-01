This is script to display metrics of cpu/memory for server.

Compatible:
1. Linux
2. Mac

Setup:
1. Install python 3.7 (https://www.python.org/downloads/)
2. Install pipenv 
- Debian Buster+: (sudo apt install pipenv)
- Fedora 28: (sudo dnf install pipenv)
- FreeBSD: (pkg install py36-pipenv)
3. Clone repository
4. Navigate to cloned repository 
5. Install dependencies (pipenv install)

Run:
- . get_metrics {command}

OR

- pipenv run python metrics.py {command}

Example:
- . get_metrics mem - to get memory metrics
- . get_metrics cpu - to get cpu metrics

Error handling:
- User will get error message with hint 