import sys

# Lendo a entrada
tweet = sys.stdin.readline().strip()

# Verificando o comprimento do tweet
if len(tweet) <= 140:
    print("TWEET")
else:
    print("MUTE")
