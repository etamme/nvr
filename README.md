# nvr
## a simpe network video recorder for RTSP streams

nvr is a wrapper around openRTSP, which is a required dependancy, that allows you to manage multiple camera streams via JSON based config file.  

nvr will run for a specified period of time, ususally 24 hours, and write out new video files at a specified interval.  Generally speaking you would create a cron job that starts nvr once a day, and it will run for 24 hours, then be restarted.  This is primarily to name the video files by YYYY-MM-DD-interval.mp4

nvr does not do any file or disk managment, you must set up appropriate cron jobs to remove old files and monitor disk usage.
