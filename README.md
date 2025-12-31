# Spotify Playlist Downloader

A simple Python script to download Spotify playlists as MP3 files using spotdl.

## Features

- Download entire Spotify playlists
- High-quality MP3 format (320kbps)
- Simple command-line interface

## Requirements

- Python 3.x
- spotdl

## Installation

Install spotdl:

```bash
pip install spotdl
```

## Usage

```bash
python spotify.py <playlist_url>
```

### Example

```bash
python spotify.py https://open.spotify.com/playlist/YOUR_PLAYLIST_ID
```

Downloads will be saved to `./spotify_downloads` by default.

## License

MIT
