#You need to have path on(at least for virtual code studio)
import sounddevice as sd
#importing the "write to wave file" library
from scipy.io.wavfile import write

#fs: frames
fs = 88200
#below is how long it lasts
seconds = 5
#sd.rec: this means to record
#samplerate doesn't appear to do anything, wonder what it is for
#channels can be replaced by mapping, and another thing that I forgot
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#why would it need to wait? Probably to recored
sd.wait() 
#writing the sound to a sound file, apparently a wave file
write('output.wav', fs, myrecording)
