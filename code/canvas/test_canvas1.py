import os
from canvasapi import Canvas
import unicodedata

with open(os.path.join(os.path.expanduser("~"), ".canvaslms", "aggregate_token")) as f:
    token = f.read()
API_URL = "https://canvas.lms.unimelb.edu.au/"
canvas = Canvas(API_URL, token)
bec = canvas.get_user(canvas.get_current_user().id)

print("User: ", bec)

print("My courses")
for c in canvas.get_courses():
    print(c)
