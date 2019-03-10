from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "10.0.0.199", 9559)
tts.say("Hello, world!")