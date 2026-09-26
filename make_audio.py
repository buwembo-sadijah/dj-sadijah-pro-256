import math, wave, struct
sr=44100; dur=12
notes=[261.63,329.63,392.00,523.25]
with wave.open('/mnt/data/djsite/assets/dj-sadijah-beat.wav','w') as w:
 w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
 for i in range(sr*dur):
  t=i/sr; beat=int(t*4)%4; f=notes[beat]
  x=0.18*math.sin(2*math.pi*f*t)+0.08*math.sin(2*math.pi*f*2*t)
  # kick/snare-ish pulses
  if (t*4)%1<0.08: x+=0.22*math.sin(2*math.pi*80*t)*math.exp(-((t*4)%1)*18)
  if (t*2)%1<0.04: x+=0.12*math.sin(2*math.pi*1800*t)*math.exp(-((t*2)%1)*30)
  env=min(1,t*3,(dur-t)*3)
  s=max(-1,min(1,x*env)); p=int(s*32767)
  w.writeframesraw(struct.pack('<hh',p,p))
