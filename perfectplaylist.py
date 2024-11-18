liked_songs = {
  'Next 2 U': 'Kehlani',
  'Heal My Scars': 'Big Boogie',
  'Big Dawg': "Desiigner",
  'Talking To My Scale': 'Young Dolph',
  'Where You Been': 'Toosii',
  'KehLani Remix': 'Jordan Adetunji ft. Kehlani',
  '2AM': 'BigXthaPlug',
  'After Hours': 'Kehlani',
  'Turn Up A Notch': 'Lil Durk',
  'Sideways': 'JT',
  "On This Hill": 'T-Pain',
  'Old Days': 'Lil Durk',
  '911': 'Roddy Rich',
  'Body': 'A Boogie Wit Da Hoodie ft. Cash Cobain',
  'Not Like Us': 'Kendrick Lamar',
  'Get Back Mode': 'Boss Top ft. King Von'
}

def write_liked_songs_to_file(liked_songs, filename):
  try:
    with open(filename, 'w') as file:
      file.write('Liked Songs:\n')
      for song, artist in liked_songs.items():
        file.write(f' {song} by {artist}\n')
    print(f"File '{filename}' created successfully.")
  except Exception as e:
    print(f"An error occurred: {e}")


write_liked_songs_to_file(liked_songs, 'liked_songs.txt')
