# main.py by cool-dev-guy aka cool-guy
import time
import tkinter as tk
import av
import threading
import imageio
class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HLS Video Player")

        # M3U8 URL of the online video stream
        self.m3u8_url = f"file_on_internet.m3u8" # include file here
        # Create the Tkinter video frame
        self.video_frame = tk.Frame(root)
        self.video_frame.pack()

        # Create the label for video display
        self.canvas = tk.Canvas(root, width=1080, height=720)
        self.canvas.pack()
        

        # Create the video player thread
        self.player_thread = threading.Thread(target=self.play_video)
        self.player_thread.daemon = True
        self.player_thread.start()

    def play_video(self):
        rax = self.canvas.create_image(0, 0, anchor=tk.NW,image=photo)
        container = av.open(self.m3u8_url)
        
        video_stream = container.streams.video[0]
        print(video_stream.frames)
        # Get the frame rate (fps) of the video stream
        fps_numerator = video_stream.base_rate.numerator
        fps_denominator = video_stream.base_rate.denominator
        fps = fps_numerator / fps_denominator

        print(f"Frame Rate (fps): {fps}")
        delay = 1.0 / (fps*2)
        for packet in container.demux(video_stream):
            #print(packet)
            for frame in packet.decode():
                photo.config(data=imageio.imwrite(imageio.RETURN_BYTES, frame.to_image(width=1080, height=720), format='PGM')) # can use PPM or PNG or GIF
                time.sleep(delay)
if __name__ == "__main__":
    root = tk.Tk()
    
    photo = tk.PhotoImage()
    app = VideoPlayerApp(root)
    root.mainloop()
