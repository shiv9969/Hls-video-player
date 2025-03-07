<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Match Stream</title>

    <!-- Plyr Player -->
    <link rel="stylesheet" href="https://cdn.plyr.io/3.7.2/plyr.css" />
    <script src="https://cdn.plyr.io/3.7.2/plyr.polyfilled.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>

    <style>
        body { text-align: center; font-family: Arial, sans-serif; }
        .video-container { max-width: 640px; margin: 20px auto; }
        video { width: 100%; border-radius: 10px; }
    </style>
</head>
<body>

    <h2>📺 Watch Live Match</h2>

    <div class="video-container">
        <video id="video" controls autoplay></video>
    </div>

    <script>
        var video = document.getElementById('video');
        var videoSrc = "{{ video_url }}";

        if (Hls.isSupported()) {
            var hls = new Hls();
            hls.loadSource(videoSrc);
            hls.attachMedia(video);
            hls.on(Hls.Events.MANIFEST_PARSED, function () {
                video.play();
            });
        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
            video.src = videoSrc;
            video.addEventListener('loadedmetadata', function () {
                video.play();
            });
        } else {
            alert("Your browser does not support HLS streaming.");
        }

        const player = new Plyr(video);
    </script>

</body>
</html>
