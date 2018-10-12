#Ecripting a file or anything to a wave
import wave, struct, math, random
class VEncript:
	
	def Encript(in_file,out_file="sound.wav",frequency=2,sampleRate=44100.0):
		wavef = wave.open(out_file,'w')
		wavef.setnchannels(1)
		wavef.setsampwidth(2)
		wavef.setframerate(sampleRate)
		file_bin = open(in_file,'rb')
		enc_data = file_bin.read()
		file_bin.close()
		for i in range(0, len(enc_data)):
			print(int(enc_data[i]))
		
		duration = 0
		max_data = int(sampleRate * duration/frequency)-1

		duration = 1/(sampleRate/frequency/len(enc_data))
		cont_data = 0
		cont_freq = 0
		for i in range(int(duration * sampleRate)):

			if((cont_freq % frequency == 0 and cont_data != len(enc_data) -1) or (cont_freq == 0) ):
				value = int(enc_data[cont_data])
				
				#value = (int(32767.0*math.cos(500*math.pi*float(i)/float(sampleRate))))
				if(cont_data < len(enc_data)-1):
					cont_data = cont_data + 1

			else:
				value = int(random.random() * 10000)
				#value = (int(32767.0*math.cos(500*math.pi*float(i)/float(sampleRate))))
			cont_freq= cont_freq+1
			data = struct.pack('<h', value)
			wavef.writeframesraw( data )
		wavef.writeframes(data)
		wavef.close()


	def Decript(in_file,out_file,frequency):
		wavef = wave.open(in_file,'rb')
		length = wavef.getnframes()
		bin_file = open(out_file,'wb')
		binData = []
		for i in range(0,length):
			
			waveData = wavef.readframes(1)

			if((i % frequency == 0 or i == 0) and waveData[0] < 300):
				
				binData.append(waveData[0])
				print(waveData[0])
				#data = struct.unpack("<h", waveData)
				
		bin_file.write(bytes(binData))
		

				
		bin_file.close()
		wavef.close()


VEncript.Encript('test.txt','sound.wav',3,44100.0)
VEncript.Decript('sound.wav','textito.txt',3)