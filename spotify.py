#!/usr/bin/env python3
import subprocess
import sys

def download_playlist(playlist_url, output_dir="./spotify_downloads"):
    """
    Download Spotify playlist to MP3
    
    Args:
        playlist_url: Spotify playlist URL
        output_dir: Output directory for MP3 files
    """
    try:
        cmd = [
            "spotdl",
            "download",
            playlist_url,
            "--output", output_dir,
            "--format", "mp3",
            "--bitrate", "320k"
        ]
        
        subprocess.run(cmd, check=True)
        print(f"Download complete. Files saved to {output_dir}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("spotdl not found. Install: pip install spotdl")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python spotify_dl.py <playlist_url>")
        sys.exit(1)
    
    download_playlist(sys.argv[1])