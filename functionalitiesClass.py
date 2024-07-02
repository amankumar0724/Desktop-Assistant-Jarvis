class MusicPlayer:
        def __init__(self):
            pygame.init()
            pygame.mixer.init()
            self.playlist = []
            self.current_song = 0
            self.voice_recognition = VoiceRecognition_and_SpeechToText()

        def load_songs_from_folder(self, folder_path):
            songs = os.listdir(folder_path)
            self.playlist = [os.path.join(folder_path, song) for song in songs if song.endswith(".mp3")]

        def play(self):
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()

        def pause(self):
            pygame.mixer.music.pause()

        def unpause(self):
            pygame.mixer.music.unpause()

        def stop(self):
            pygame.mixer.music.stop()

        def next_song(self):
            self.stop()
            self.current_song = (self.current_song + 1) % len(self.playlist)
            self.play()

        def choose_song(self):
            print("Select a song:")
            for i, song_path in enumerate(self.playlist):
                print(f"{i+1}. {os.path.basename(song_path)}")

            choice = int(input("Enter the number of the song: "))
            if choice > 0 and choice <= len(self.playlist):
                self.stop()
                self.current_song = choice - 1
                self.play()
            else:
                print("Invalid choice.")

        
        def get_user_choice(self):
            print("\n1. Play\n2. Pause\n3. Unpause\n4. Stop\n5. Next Song\n6. Choose Song\n7. Exit")
            choice = input("Enter your choice: ")
            return choice

        def run(self):

            while True:
                user_voice = self.voice_recognition.take_command()

                if "play" in user_voice:
                    self.play()

                elif "pause" in user_voice:
                    self.pause()

                elif "unpause" in user_voice:
                    self.unpause()

                elif "stop" in user_voice:
                    self.stop()

                elif "next song" in user_voice:
                    self.next_song()

                elif "select song" in user_voice:
                    self.choose_song()

                elif "option" in user_voice:
                    self.get_user_choice()

                elif "exit" in user_voice:
                    break

                else:
                    print("Invalid choice. Try again.")
