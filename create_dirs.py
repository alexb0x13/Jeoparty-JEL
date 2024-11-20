import os

dirs = [
    'templates',
    'static',
    'static/css',
    'static/js'
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)
