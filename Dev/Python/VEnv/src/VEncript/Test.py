import wave, struct, math

sampleRate = 88200.0 # hertz
duration = 4.0       # seconds
frequency = 440.0    # hertz

wavef = wave.open('sound.wav','w')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2) 
wavef.setframerate(sampleRate)
test = range(int(duration*sampleRate))
for i in range(int(duration * sampleRate)):

	
    value = (int(32767.0*math.cos(test[i]*math.pi*float(i)/float(sampleRate))))

  
    #value = (int(32767.0*math.cos(500*math.pi*float(i)/float(sampleRate))))

    data = struct.pack('<h', value)
    wavef.writeframesraw( data )

wavef.writeframes('')
wavef.close()

