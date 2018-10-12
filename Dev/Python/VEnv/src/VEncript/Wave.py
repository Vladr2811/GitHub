import wave, struct, math

sampleRate = 44100.0 # hertz
duration = 1.0       # seconds
frequency = 440.0    # hertz  Contra

wavef = wave.open('sound.wav','w')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2) 
wavef.setframerate(sampleRate)
test = [30,52,10,34,12,34,54,75,24,64,12,86,43,12,86,34,96,23,76,23,87,43] 
j = 0;

for i in range(int(duration * sampleRate)):

	
    value = (int(test[j]*math.cos(frequency*math.pi*float(i)/float(sampleRate))))
    if(j < len(test)-1):
    	j = j + 1
  
    value = (int(32767.0*math.cos(500*math.pi*float(i)/float(sampleRate))))

    data = struct.pack('<h', value)
    wavef.writeframesraw( data )

wavef.writeframes(data)
wavef.close()

