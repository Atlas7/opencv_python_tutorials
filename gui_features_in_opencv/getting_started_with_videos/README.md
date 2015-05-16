# Getting Started with Videos

## Prerequisites:

- If run via an IDE (like Anaconda). Make sure to change the current working directory to where this directory (i.e. where the Python file and the input video file is stored). The code uses relative pathnames. So this is mandatory for the Video Capture and writer steps.
- Make sure the `ffmpeg` codec is installed and works within OpenCV. This [Stackoverflow forum](http://stackoverflow.com/questions/23119413/how-to-install-python-opencv-through-conda) has provided a good tip on getting this done. Check out the solution by user [eculeus](http://stackoverflow.com/users/2012659/eculeus). This is mandatory for the Video Writer step.

## Test Instructions:

So here are the files that we have to begin with:

- `load_video.py`: the python code that we are going to run.
- `all_blacks_skills_part_2.mp4` the video that we are going to use to test run our code.

![screenshot_dir_before.png](./screenshots/screenshot_dir_before.png)

Feel free to view the video `all_blacks_skills_part_2.mp4` (e.g. via VLC player), to see what the video looks like.

![screenshot_video_before.png](./screenshots/screenshot_video_before.png)

Run the `load_video.py`. If run via IDE (e.g. Anaconda), take heed of the Prerequisites section above!

![screenshot_test_run_code.png](./screenshots/screenshot_test_run_code.png)

While the code is running, you shall see the video being processed (i.e. flipped upside down) and played (via a new window "frame"). A new output video (`output.avi`) is created and being updated in the meantime.

![screenshot_run_entire_code_0.png](./screenshots/screenshot_run_entire_code_0.png)

![screenshot_run_entire_code_1.png](./screenshots/screenshot_run_entire_code_1.png)

When the code finishes running the window "frame" closes down automatically.

![screenshot_run_entire_code_2.png](./screenshots/screenshot_run_entire_code_2.png)

You shall also notice that a new output video `output.avi` is created:

![screenshot_dir_after.png](./screenshots/screenshot_dir_after.png)

And when you play it (`output.avi`), you shall see our new processed (flipped upside down) video!

![screenshot_video_after.png](./screnshots/screenshot_video_after.png)

This completes our test run :)

# References

The test sample video (`all_blacks_skills_part_2.mp4`) is originated from [this YouTube Video](https://www.youtube.com/watch?v=3WUUovQwwrM) uploaded by [Brand Spank](https://www.youtube.com/channel/UC-yJ5ogPw3wmWJhyAKEfx2Q). Since at the time of code testing I did not have any video files on my desktop, I used the free and open-source tool [youtube-dl](https://rg3.github.io/youtube-dl/) to download the video from [YouTube](https://www.youtube.com), save it as a MPEG4 (`.mp4`) file. The code uses this `.mp4` file and output a `.avi` format video. The use of this video is purely for illustration purpose. I do not own the video.