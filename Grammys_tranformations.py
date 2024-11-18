from functools import reduce


# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def filtered_songs(playlist):
  return [song for song in playlist if song[1] > 5.00]

long_songs = filtered_songs(playlist)
print('Songs longer than 5 minutes:', list(long_songs))
    
def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = int((duration - minutes) * 100)
    total_seconds = minutes * 60 + round(seconds)
    return (song[0], total_seconds)

min_to_secs = map(minutes_to_seconds, playlist)

print('Songs with duration in seconds: ', list(min_to_secs))

def addition(x,y):
    return x + y

total_duration = reduce(addition, [song[1] for song in playlist])
print('Total duration of the playlist: ', total_duration, ' minutes')
    

