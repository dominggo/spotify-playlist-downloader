# Onboarding Guide

## Project Overview

This is a Spotify Playlist Downloader that converts Spotify playlists to high-quality MP3 files using spotdl.

## Project Structure

```
02_spotify/
├── spotify.py              # Main script for downloading playlists
├── .gitignore             # Git ignore rules
├── README.md              # User-facing documentation
├── onboarding.md          # This file - developer onboarding
└── spotify_downloads/     # Output directory (gitignored)
```

## Setup

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dominggo/spotify-playlist-downloader.git
   cd spotify-playlist-downloader
   ```

2. Install dependencies:
   ```bash
   pip install spotdl
   ```

## Usage

Run the script with a Spotify playlist URL:

```bash
python spotify.py <playlist_url>
```

Example:
```bash
python spotify.py https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
```

## How It Works

The script uses `spotdl` to:
1. Parse the Spotify playlist URL
2. Search for each track on YouTube
3. Download and convert to MP3 (320kbps)
4. Save files to `./spotify_downloads`

## Development

### Key Files

- **spotify.py**: Main entry point
  - `download_playlist()`: Core function that handles the download process
  - Uses subprocess to call spotdl CLI
  - Error handling for missing dependencies

### Configuration

Default settings:
- Output directory: `./spotify_downloads`
- Format: MP3
- Bitrate: 320kbps

To modify, edit the `cmd` array in `spotify.py:14-20`

## Git Workflow

The repository ignores:
- `.claude/` - Claude Code settings (local only)
- `spotify_downloads/` - Downloaded music files

## Common Tasks

### Test the script
```bash
python spotify.py <test_playlist_url>
```

### Add new features
1. Create a new branch
2. Make changes to `spotify.py`
3. Test thoroughly
4. Commit and push
5. Create a pull request

## Troubleshooting

**spotdl not found error:**
```bash
pip install spotdl
```

**Permission errors on Windows:**
Run terminal as administrator or check file permissions

**Download failures:**
- Check internet connection
- Verify Spotify URL is valid
- Some tracks may not be available on YouTube

## Resources

- [spotdl Documentation](https://github.com/spotDL/spotify-downloader)
- [Spotify Playlist URLs](https://support.spotify.com/us/article/sharing/)

## Repository

GitHub: https://github.com/dominggo/spotify-playlist-downloader
