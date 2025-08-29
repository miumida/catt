# Cast All The Things!(catt) Service
![HAKC)][hakc-shield]
![HACS][hacs-shield]
![Version v1.0.1][version-shield]

Cast All The Things! for Home Assistant #HA

## Version history
| Version | Date        | Desc.              |
| :-----: | :---------: | ----------------------- |
| v1.0.0  | 2022.08.19  | First version  |
| v1.0.1  | 2025.08.25  | icons.json Add  |


## Installation
This can be installed through HACS(Add url to custom repository) by copying all the files from custom_components/catt/ to <config directory>/custom_components/catt/

## Services
#### scan
  Scan the local network and show all Chromecasts and their IPs.
#### help
  Show help.
#### command
 | commands | Desc.        |
 | ------------- | --------- |
 | cast         | Send a video to a Chromecast for playing. |
 | cast_site    | Cast any website to a Chromecast.         |
 | play         | Resume a video after it has been paused.  |
 | play_toggle  | Toggle between playing and paused state.  |
 | pause        | Pause a video.                            |
 | clear        | Clear the queue (YouTube only).           |
 | add          | Add a video to the queue (YouTube only).  |
 | remove       | Remove a video from the queue (YouTube only). |
 | seek         | Seek the video to TIME position. |
 | ffwd         | Fastforward a video by TIME duration. |
 | rewind       | Rewind a video by TIME duration. |
 | volume       | Set the volume to LVL [0-100]. |
 | volumedown   | Turn down volume by a DELTA increment. |
 | volumemute   | Enable or disable mute on supported devices.|
 | volumeup     | Turn up volume by a DELTA increment. |
#### stop
  Stop playing.
  
## Thanks.
- [catt](https://github.com/skorokithakis/catt) - Library for Python 3

[version-shield]: https://img.shields.io/badge/version-1.0.1-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
