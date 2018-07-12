# fgg-detection
Act 1 (Ext)
Detect Gun -> Close Door
Consume camera feed from RTSP streams

Apply motion detection

If motion, then

Produce event to Gun image recognition
Consume Gun image recognition events

Apply Gun detection

If gun detection threshold met, then

Produce event for recognized Gun In Image
Consume recognized Gun In Image event

Apply gun chronology verification of subsequent events (avoid false positives)

If gun has been around for N image motion frames, then

Produce event for Close Door
Consume Close Door event

Check door state

If door isn't already closed, or in the process of opening, push the button to close the door.

Usefull Links for libraries and misc. needed files
https://github.com/tzutalin/labelImg
https://github.com/tensorflow/models
https://github.com/google/protobuf/releases?after=v3.4.1
https://github.com/datitran/raccoon_dataset
