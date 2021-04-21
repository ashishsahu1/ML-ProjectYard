# RAVDESS Emotional Speech Audio Dataset

- The dataset contains 1440 files, having 60 trials per actor x 24 actors. 
- It contains 24 professional (12 female and 12 male), vocalizing two lexically matched statements in a neutral North American accent.
- The emotions includes calm, happy, sad, angry, fearful, surprise, and disguist.

**Filename identifiers**

- Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
- Vocal channel (01 = speech, 02 = song).
- Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
- Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
- Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
- Repetition (01 = 1st repetition, 02 = 2nd repetition).
- Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).

**Filename example: 03-01-06-01-02-01-12.wav**

- Audio-only (03)
- Speech (01)
- Fearful (06)
- Normal intensity (01)
- Statement "dogs" (02)
- 1st Repetition (01)
- 12th Actor (12)
- Female, as the actor ID number is even.