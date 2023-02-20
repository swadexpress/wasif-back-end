

import firebase_admin
from firebase_admin import credentials, messaging
cred = credentials.Certificate("/home/dulquer/LiveKit/orbitplug-back-end/home/peacegarden-ccbe4-firebase-adminsdk-q8oqd-a55b0951b4.json")
firebase_admin.initialize_app(cred)
message = messaging.MulticastMessage(
data={"name":'kna'},
notification=messaging.Notification(
title="Title",
body="body line1\nbody line2"),

tokens=['e1X93H2WReGBZKBqr8_9L_:APA91bE4zCdyRkW5R1of3OjrlDVrTq5TiIcTOVehKdlNW56UsHR1hNExbzbPlWXIwlqk3VUNffrWfDCgPLQ3qUNoP_6NTVwHVepE5HGIhUHwdhfUQtz_Qm5foh8Qxp0UIUz2Gj2enmVy']
)
messaging.send_multicast(message)





