# Pinterest Illustration Scraper

A powerful web scraper to collect high-resolution cute 2D illustrations from Pinterest using the `pinscrape` library.

## ✨ Features

- **High-Resolution Images**: Downloads only images with dimensions ≥ 800px (both width and height)
- **Smart Deduplication**: Uses perceptual hashing (pHash) to detect and skip visually similar images
- **Duplicate Replacement**: Automatically replaces lower-resolution duplicates with higher-resolution versions
- **Content Filtering**: Filters out real humans, cartoon characters, and movie/series characters
- **Multi-Query Support**: Searches across multiple illustration styles (cartoon, vector, pastel, minimal, etc.)
- **Real-Time Progress**: Updates CSV file after each successful download
- **Resume Capability**: Automatically skips previously downloaded images on restart

## 🎯 Target Content

The scraper focuses on **cute 2D animal illustrations** including:
- 🐢 Turtle, 🦙 Llama, 🦘 Kangaroo, 🐹 Hamster, 🦦 Otter
- 🐨 Koala, 🦑 Squid, 🦎 Iguana, 🐜 Ant, 🐌 Snail
- 🦃 Turkey, 🐐 Goat, 🦫 Beaver, 🦨 Skunk, 🦡 Badger
- 🦣 Mammoth, 🦢 Swan, 🦩 Flamingo, 🦐 Shrimp, 🦏 Rhinoceros
- 🦛 Hippopotamus, 🦓 Zebra, 🐦 Toucan, and many more!

**Exclusions**: Real humans, anime characters, Marvel/DC characters, Disney characters, and other IP-protected content.

## 📋 Requirements

- Python 3.10+
- pinscrape (Pinterest scraping library)
- Pillow (image processing)
- imagehash (perceptual hashing)
- requests

## 🚀 Installation

```bash
# Install dependencies
pip install pinscrape Pillow imagehash requests

# Or use requirements.txt
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```bash
python illustration_scraper.py
```

### Configuration

Edit the following settings in `illustration_scraper.py`:

```python
# Output settings
OUTPUT_FOLDER = "illustration_images"
CSV_FILE = "illustration_scraped.csv"

# Scraping settings
MIN_DIMENSION = 800           # Minimum width AND height in pixels
MAX_IMAGES_PER_QUERY = 100    # Images to fetch per search query
TOTAL_TARGET_IMAGES = 10000   # Total images to collect
HASH_THRESHOLD = 10           # Perceptual hash similarity threshold
```

### Adding Custom Search Queries

Modify the `SEARCH_QUERIES` list to add your own search terms:

```python
SEARCH_QUERIES = [
    "cute 2d cat illustration",
    "cute 2d dog cartoon illustration",
    "cute 2d bunny vector illustration",
    # Add more queries...
]
```

## 📊 Output

### CSV Format

The scraper generates a CSV file with the following columns:

| Column | Description |
|--------|-------------|
| height | Image height in pixels |
| width | Image width in pixels |
| page_link | Pinterest page URL (if available) |
| image_link | Direct image URL |
| platform | Always "pinterest" |
| file_path | Local file path |
| timestamp | Download timestamp (ISO format) |
| phash | Perceptual hash for deduplication |
| query | Search query used to find the image |

### Directory Structure

```
printerest/
├── illustration_scraper.py    # Main scraper script
├── requirements.txt           # Python dependencies
├── Readme.md                  # This file
├── illustration_scraped.csv   # Image metadata
└── illustration_images/       # Downloaded images
    ├── illustration_abc123.jpg
    ├── illustration_def456.png
    └── ...
```

## 🔧 How It Works

1. **Query Execution**: Uses pinscrape to search Pinterest for each query
2. **Content Filtering**: Checks queries and image metadata against blocked keywords
3. **Image Download**: Downloads images and verifies dimensions using PIL
4. **Dimension Check**: Ensures both width AND height are ≥ 800px
5. **Hash Computation**: Calculates perceptual hash for each image
6. **Deduplication**: Compares hashes to detect visually similar images
   - If new image is larger → replaces existing duplicate
   - If existing image is larger → skips new image
7. **Real-Time Save**: Updates CSV after each successful download

## 🛡️ Content Filtering

The scraper automatically filters out:

- **Real Humans**: Photographs, portraits, celebrities, influencers
- **Anime/Manga**: Naruto, Dragon Ball, One Piece, etc.
- **Marvel Characters**: Spider-Man, Iron Man, Avengers, etc.
- **DC Characters**: Batman, Superman, Justice League, etc.
- **Disney/Pixar**: Mickey Mouse, Frozen, Toy Story, etc.
- **Other IP**: Harry Potter, Star Wars, Game of Thrones, etc.

## 📈 Statistics

Current collection stats:
- **Target**: 10,000 images
- **Minimum Resolution**: 800x800 pixels
- **Output**: `illustration_images/` folder
- **Metadata**: `illustration_scraped.csv`

## ⚠️ Notes

- Pinterest may rate-limit requests; the scraper includes built-in delays
- Some images may fail to download due to access restrictions
- Respect Pinterest's Terms of Service
- For large collections, run the scraper in multiple sessions

## 🐛 Troubleshooting

### No Images Being Downloaded
- Check network connectivity
- Verify pinscrape is installed correctly
- Try different search queries

### Duplicate Detection Not Working
- Ensure imagehash is installed: `pip install imagehash`
- Check if `illustration_scraped.csv` has valid phash values

### Images Below Size Threshold
- All images must have both dimensions ≥ 800px
- Try different search queries for higher resolution results

## 📄 License

This project is for educational purposes only. Respect copyright and Pinterest's Terms of Service when using scraped content.