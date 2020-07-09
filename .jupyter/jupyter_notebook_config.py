import os
c.ServerProxy.servers = {
  'atoti': {
    'command': [
      'python',
       'finance/value-at-risk/main.py', 
    ],
    'timeout': 120,
    'launcher_entry': {
      'title': 'atoti'
    },
    'port': 9999,
  },
    'test-server': {
    'command': ['python3', '-m', 'http.server', '{port}'],
    'absolute_url': False
  }
}
