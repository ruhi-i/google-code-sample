"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None         # the video currently being played
        self._paused_video = None          # the video paused at the moment

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())    # returns the number of videos in the library
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):       # shows the all the video titles, ids and tags
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()      # getting video info
        all_videos.sort(key=lambda x: x.title)                 # sorting videos by title
        print("Here's a list of all available videos:")
        for i in all_videos:
            tagstr = " ".join(i.tags)                         # formatting tags
            print(f"{i.title} ({i.video_id}) [{tagstr}]")


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)  # fetching video info based on id
        if self._current_video == None and video:           # if this is the first video played
            print(f"Playing video: {video.title}")
            self._current_video = video

        elif self._current_video != None and video and not self._paused_video: # stopping the present video & playing the new one
            print(f"Stopping video: {self._current_video.title}")
            video = self._video_library.get_video(video_id)
            print(f"Playing video: {video.title}")
            self._current_video=video

        elif self._current_video != None and video and self._paused_video:  #stopping the paused video & playing the new one
            print(f"Stopping video: {self._paused_video.title}")
            self._paused_video = None
            video = self._video_library.get_video(video_id)
            print(f"Playing video: {video.title}")
            self._current_video = video

        elif not video:
             print("Cannot play video: Video does not exist ")  # if there is no video in the lib

    def stop_video(self):
        """Stops the current video."""
        if self._current_video and not self._paused_video:  # when there is a video playing currently
            print(f"Stopping video: {self._current_video.title}")
            self._current_video = None
        elif self._paused_video and not self._current_video: # when there is a paused video
            print(f"Stopping video: {self._paused_video.title}")
            self._paused_video = None
        elif self._current_video and self._paused_video:     # when there is a video playing and another is paused
            print(f"Stopping video: {self._current_video.title}")
            self._current_video = None
            print(f"Stopping video: {self._paused_video.title}")
            self._paused_video = None

        else:      # when there is no video playing or paused
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()  # list of all videos
        random_video = random.choice(all_videos)           # choosing a random video
        if self._current_video:
            print(f"Stopping video: {self._current_video.title}") # stopping a video already playing
            print(f"Playing video: {random_video.title}")         # playing the new random video

        elif not self._current_video and not self._paused_video:   #playing a random video
            print(f"Playing video: {random_video.title}")
            self._current_video = random_video

        elif not self._current_video and self._paused_video:      #stopping a paused video and playing the random one
            print(f"Stopping video: {self._paused_video.title}")
            self._paused_video = None
            print(f"Playing video: {random_video.title}")
            self._current_video = random_video

        elif not random_video:
            print("No videos available")      # in case no video is available


    def pause_video(self):
        """Pauses the current video."""
        if self._current_video and not self._paused_video:       # pausing the currently playing video
            print(f"Pausing video: {self._current_video.title}")
            self._paused_video = self._current_video

        elif self._paused_video:     # if video is already paused
            print(f"Video already paused: {self._paused_video.title} ")

        elif not self._paused_video and not self._current_video:     # if no video is currently playing
            print("Cannot pause video: No video is currently playing")


    def continue_video(self):
        """Resumes playing the current video."""
        if not self._current_video:     # if no video is currently playing
            print("Cannot continue video: No video is currently playing")
        elif not self._paused_video:    # if video isn't paused in the first place
            print("Cannot continue video: Video is not paused")
        else:                           # continuing the paused video
            print(f"Continuing video: {self._paused_video.title} ")
            self._paused_video = None


    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video and not self._paused_video:   # showing status of video currently playing
            tagstr = " ".join(self._current_video.tags)
            print(f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{tagstr}]")
        elif self._current_video and self._paused_video:    # if current video is paused
            tagstr = " ".join(self._current_video.tags)
            print(f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{tagstr}] - PAUSED")
        elif not self._current_video and not self._paused_video:   #if no video is playing right now
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.

        """



        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
