for (const player of document.querySelectorAll(".build-player")) {
  const video = player.querySelector("video");
  const speed = document.createElement("select");
  for (const rate of [1, 3, 4]) {
    speed.add(new Option(rate + "×", String(rate)));
  }

  const label = document.createElement("label");
  label.append("Playback speed ", speed);
  video.after(label);
  speed.value = "3";
  video.defaultPlaybackRate = 3;
  video.playbackRate = 3;

  speed.addEventListener("change", () => {
    video.defaultPlaybackRate = Number(speed.value);
    video.playbackRate = Number(speed.value);
  });

  video.addEventListener("ratechange", () => {
    const rate = String(video.playbackRate);
    if (![...speed.options].some(option => option.value === rate)) {
      speed.add(new Option(rate + "×", rate));
    }
    speed.value = rate;
  });

  for (const link of player.querySelectorAll("a[href]")) {
    link.addEventListener("click", event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      video.currentTime = Number(link.hash.slice(3));
      video.play().catch(() => video.focus());
    });
  }
}
