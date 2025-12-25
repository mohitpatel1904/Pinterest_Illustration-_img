"""
Pinterest Illustration Scraper using pinscrape
Collects cute animals, animals, and object-related illustrations
Excludes: real humans, cartoon characters, movie/series characters
"""

import os
import csv
import hashlib
from datetime import datetime
from io import BytesIO
from pathlib import Path

import requests
import imagehash
from PIL import Image
from pinscrape import scraper, Pinterest


# ============================================================
# CONFIGURATION
# ============================================================

# Output settings
OUTPUT_FOLDER = "illustration_images"
CSV_FILE = "illustration_scraped.csv"

# Search settings
SEARCH_QUERIES = [
    # ============================================================
    # CONTINUE FROM HERE - After moth pastel
    # ============================================================
    
    # Moth illustrations (remaining)
    "cute 2d moth minimal illustration",
    
    # ============================================================
    # COMPLETED QUERIES (commented out)
    # ============================================================
    
    # # Turtle illustrations
    # "cute 2d turtle illustration",
    # "cute 2d turtle cartoon illustration",
    # "cute 2d turtle flat illustration",
    # "cute 2d turtle vector illustration",
    # "cute 2d turtle pastel illustration",
    # "cute 2d turtle minimal illustration",
    
    # # Llama illustrations
    # "cute 2d llama illustration",
    # "cute 2d llama cartoon illustration",
    # "cute 2d llama flat illustration",
    # "cute 2d llama vector illustration",
    # "cute 2d llama pastel illustration",
    # "cute 2d llama minimal illustration",
    
    # # Kangaroo illustrations
    # "cute 2d kangaroo illustration",
    # "cute 2d kangaroo cartoon illustration",
    # "cute 2d kangaroo flat illustration",
    # "cute 2d kangaroo vector illustration",
    # "cute 2d kangaroo pastel illustration",
    # "cute 2d kangaroo minimal illustration",
    
    # # Hamster illustrations
    # "cute 2d hamster illustration",
    # "cute 2d hamster cartoon illustration",
    # "cute 2d hamster flat illustration",
    # "cute 2d hamster vector illustration",
    # "cute 2d hamster pastel illustration",
    # "cute 2d hamster minimal illustration",
    
    # # Otter illustrations
    # "cute 2d otter illustration",
    # "cute 2d otter cartoon illustration",
    # "cute 2d otter flat illustration",
    # "cute 2d otter vector illustration",
    # "cute 2d otter pastel illustration",
    # "cute 2d otter minimal illustration",
    
    # # Koala illustrations
    # "cute 2d koala illustration",
    # "cute 2d koala cartoon illustration",
    # "cute 2d koala flat illustration",
    # "cute 2d koala vector illustration",
    # "cute 2d koala pastel illustration",
    # "cute 2d koala minimal illustration",
    
    # # Squid illustrations
    # "cute 2d squid illustration",
    # "cute 2d squid cartoon illustration",
    # "cute 2d squid flat illustration",
    # "cute 2d squid vector illustration",
    # "cute 2d squid pastel illustration",
    # "cute 2d squid minimal illustration",
    
    # # Iguana illustrations
    # "cute 2d iguana illustration",
    # "cute 2d iguana cartoon illustration",
    # "cute 2d iguana flat illustration",
    # "cute 2d iguana vector illustration",
    # "cute 2d iguana pastel illustration",
    # "cute 2d iguana minimal illustration",
    
    # # Moth illustrations (already done)
    # "cute 2d moth illustration",
    # "cute 2d moth cartoon illustration",
    # "cute 2d moth flat illustration",
    # "cute 2d moth vector illustration",
    # "cute 2d moth pastel illustration",
    
    # Ant illustrations
    "cute 2d ant illustration",
    "cute 2d ant cartoon illustration",
    "cute 2d ant flat illustration",
    "cute 2d ant vector illustration",
    "cute 2d ant pastel illustration",
    "cute 2d ant minimal illustration",
    
    # Snail illustrations
    "cute 2d snail illustration",
    "cute 2d snail cartoon illustration",
    "cute 2d snail flat illustration",
    "cute 2d snail vector illustration",
    "cute 2d snail pastel illustration",
    "cute 2d snail minimal illustration",
    
    # Turkey illustrations
    "cute 2d turkey illustration",
    "cute 2d turkey cartoon illustration",
    "cute 2d turkey flat illustration",
    "cute 2d turkey vector illustration",
    "cute 2d turkey pastel illustration",
    "cute 2d turkey minimal illustration",
    
    # Goat illustrations
    "cute 2d goat illustration",
    "cute 2d goat cartoon illustration",
    "cute 2d goat flat illustration",
    "cute 2d goat vector illustration",
    "cute 2d goat pastel illustration",
    "cute 2d goat minimal illustration",
    
    # Beaver illustrations
    "cute 2d beaver illustration",
    "cute 2d beaver cartoon illustration",
    "cute 2d beaver flat illustration",
    "cute 2d beaver vector illustration",
    "cute 2d beaver pastel illustration",
    "cute 2d beaver minimal illustration",
    
    # Skunk illustrations
    "cute 2d skunk illustration",
    "cute 2d skunk cartoon illustration",
    "cute 2d skunk flat illustration",
    "cute 2d skunk vector illustration",
    "cute 2d skunk pastel illustration",
    "cute 2d skunk minimal illustration",
    
    # Badger illustrations
    "cute 2d badger illustration",
    "cute 2d badger cartoon illustration",
    "cute 2d badger flat illustration",
    "cute 2d badger vector illustration",
    "cute 2d badger pastel illustration",
    "cute 2d badger minimal illustration",
    
    # Mammoth illustrations
    "cute 2d mammoth illustration",
    "cute 2d mammoth cartoon illustration",
    "cute 2d mammoth flat illustration",
    "cute 2d mammoth vector illustration",
    "cute 2d mammoth pastel illustration",
    "cute 2d mammoth minimal illustration",
    
    # Swan illustrations
    "cute 2d swan illustration",
    "cute 2d swan cartoon illustration",
    "cute 2d swan flat illustration",
    "cute 2d swan vector illustration",
    "cute 2d swan pastel illustration",
    "cute 2d swan minimal illustration",
    
    # Flamingo illustrations
    "cute 2d flamingo illustration",
    "cute 2d flamingo cartoon illustration",
    "cute 2d flamingo flat illustration",
    "cute 2d flamingo vector illustration",
    "cute 2d flamingo pastel illustration",
    "cute 2d flamingo minimal illustration",
    
    # Shrimp illustrations
    "cute 2d shrimp illustration",
    "cute 2d shrimp cartoon illustration",
    "cute 2d shrimp flat illustration",
    "cute 2d shrimp vector illustration",
    "cute 2d shrimp pastel illustration",
    "cute 2d shrimp minimal illustration",
    
    # Rhinoceros illustrations
    "cute 2d rhinoceros illustration",
    "cute 2d rhinoceros cartoon illustration",
    "cute 2d rhinoceros flat illustration",
    "cute 2d rhinoceros vector illustration",
    "cute 2d rhinoceros pastel illustration",
    "cute 2d rhinoceros minimal illustration",
    
    # Hippopotamus illustrations
    "cute 2d hippopotamus illustration",
    "cute 2d hippopotamus cartoon illustration",
    "cute 2d hippopotamus flat illustration",
    "cute 2d hippopotamus vector illustration",
    "cute 2d hippopotamus pastel illustration",
    "cute 2d hippopotamus minimal illustration",
    
    # Zebra illustrations
    "cute 2d zebra illustration",
    "cute 2d zebra cartoon illustration",
    "cute 2d zebra flat illustration",
    "cute 2d zebra vector illustration",
    "cute 2d zebra pastel illustration",
    "cute 2d zebra minimal illustration",
    
    # Toucan illustrations
    "cute 2d toucan illustration",
    "cute 2d toucan cartoon illustration",
    "cute 2d toucan flat illustration",
    "cute 2d toucan vector illustration",
    "cute 2d toucan pastel illustration",
    "cute 2d toucan minimal illustration",
    
    # ============================================================
    # General Illustration Styles
    # ============================================================
    "Original 2D Character Illustration",
    "Non-Anime Stylized Illustration",
    "Editorial Character Illustration",
    "Hand-Painted Digital Illustration",
    "Watercolor-Style Illustration",
    "Lifestyle Character Illustration",
    "Storybook-Style Illustration",
    "Painterly Character Illustration",
    "Original 2D Environment Illustration",
    "Non-Anime Stylized Landscape Illustration",
    "Painterly Nature Illustration",
    "Hand-Painted Digital Landscape",
    "Watercolor-Style Environment Illustration",
    "Editorial Nature Illustration",
    "Storybook-Style Landscape Art",
    "Atmospheric Painterly Illustration",
    
    # ============================================================
    # PREVIOUS QUERIES - Owl, Penguin, etc. (commented out)
    # ============================================================
    
    # # Owl illustrations
    # "cute 2d owl illustration",
    # "cute 2d owl cartoon illustration",
    # "cute 2d owl flat illustration",
    # "cute 2d owl vector illustration",
    # "cute 2d owl kawaii illustration",
    # "cute 2d owl pastel illustration",
    # "cute 2d owl minimal illustration",
    # "cute 2d owl chibi illustration",
    
    # # Penguin illustrations
    # "cute 2d penguin illustration",
    # "cute 2d penguin cartoon illustration",
    # "cute 2d penguin flat illustration",
    # "cute 2d penguin vector illustration",
    # "cute 2d penguin kawaii illustration",
    # "cute 2d penguin pastel illustration",
    # "cute 2d penguin minimal illustration",
    # "cute 2d penguin chibi illustration",
    
    # # Squirrel illustrations
    # "cute 2d squirrel illustration",
    # "cute 2d squirrel cartoon illustration",
    # "cute 2d squirrel flat illustration",
    # "cute 2d squirrel vector illustration",
    # "cute 2d squirrel kawaii illustration",
    # "cute 2d squirrel pastel illustration",
    # "cute 2d squirrel minimal illustration",
    # "cute 2d squirrel chibi illustration",
    
    # # Monkey illustrations
    # "cute 2d monkey illustration",
    # "cute 2d monkey cartoon illustration",
    # "cute 2d monkey flat illustration",
    # "cute 2d monkey vector illustration",
    # "cute 2d monkey kawaii illustration",
    # "cute 2d monkey pastel illustration",
    # "cute 2d monkey minimal illustration",
    # "cute 2d monkey chibi illustration",
    
    # # Sloth illustrations
    # "cute 2d sloth illustration",
    # "cute 2d sloth cartoon illustration",
    # "cute 2d sloth flat illustration",
    # "cute 2d sloth vector illustration",
    # "cute 2d sloth kawaii illustration",
    # "cute 2d sloth pastel illustration",
    # "cute 2d sloth minimal illustration",
    # "cute 2d sloth chibi illustration",
    
    # # Hedgehog illustrations
    # "cute 2d hedgehog illustration",
    # "cute 2d hedgehog cartoon illustration",
    # "cute 2d hedgehog flat illustration",
    # "cute 2d hedgehog vector illustration",
    # "cute 2d hedgehog kawaii illustration",
    # "cute 2d hedgehog pastel illustration",
    # "cute 2d hedgehog minimal illustration",
    # "cute 2d hedgehog chibi illustration",
    
    # # Raccoon illustrations
    # "cute 2d raccoon illustration",
    # "cute 2d raccoon cartoon illustration",
    # "cute 2d raccoon flat illustration",
    # "cute 2d raccoon vector illustration",
    # "cute 2d raccoon kawaii illustration",
    # "cute 2d raccoon pastel illustration",
    # "cute 2d raccoon minimal illustration",
    # "cute 2d raccoon chibi illustration",
    
    # # Deer illustrations
    # "cute 2d deer illustration",
    # "cute 2d deer cartoon illustration",
    # "cute 2d deer flat illustration",
    # "cute 2d deer vector illustration",
    # "cute 2d deer kawaii illustration",
    # "cute 2d deer pastel illustration",
    # "cute 2d deer minimal illustration",
    # "cute 2d deer chibi illustration",
    
    # # Giraffe illustrations
    # "cute 2d giraffe illustration",
    # "cute 2d giraffe cartoon illustration",
    # "cute 2d giraffe flat illustration",
    # "cute 2d giraffe vector illustration",
    # "cute 2d giraffe kawaii illustration",
    # "cute 2d giraffe pastel illustration",
    # "cute 2d giraffe minimal illustration",
    # "cute 2d giraffe chibi illustration",
    
    # # Elephant illustrations
    # "cute 2d elephant illustration",
    # "cute 2d elephant cartoon illustration",
    # "cute 2d elephant flat illustration",
    # "cute 2d elephant vector illustration",
    # "cute 2d elephant kawaii illustration",
    # "cute 2d elephant pastel illustration",
    # "cute 2d elephant minimal illustration",
    # "cute 2d elephant chibi illustration",
    
    # # Parrot illustrations
    # "cute 2d parrot illustration",
    # "cute 2d parrot cartoon illustration",
    # "cute 2d parrot flat illustration",
    # "cute 2d parrot vector illustration",
    # "cute 2d parrot kawaii illustration",
    # "cute 2d parrot pastel illustration",
    # "cute 2d parrot minimal illustration",
    # "cute 2d parrot chibi illustration",
    
    # # Chick illustrations
    # "cute 2d chick illustration",
    # "cute 2d chick cartoon illustration",
    # "cute 2d chick flat illustration",
    # "cute 2d chick vector illustration",
    # "cute 2d chick kawaii illustration",
    # "cute 2d chick pastel illustration",
    # "cute 2d chick minimal illustration",
    # "cute 2d chick chibi illustration",
    
    # # Turtle illustrations (old)
    # "cute 2d turtle kawaii illustration",
    # "cute 2d turtle chibi illustration",
    
    # # Dolphin illustrations
    # "cute 2d dolphin illustration",
    # "cute 2d dolphin cartoon illustration",
    # "cute 2d dolphin flat illustration",
    # "cute 2d dolphin vector illustration",
    # "cute 2d dolphin kawaii illustration",
    # "cute 2d dolphin pastel illustration",
    # "cute 2d dolphin minimal illustration",
    # "cute 2d dolphin chibi illustration",
    
    # # Whale illustrations
    # "cute 2d whale illustration",
    # "cute 2d whale cartoon illustration",
    # "cute 2d whale flat illustration",
    # "cute 2d whale vector illustration",
    # "cute 2d whale kawaii illustration",
    # "cute 2d whale pastel illustration",
    # "cute 2d whale minimal illustration",
    # "cute 2d whale chibi illustration",
    
    # ============================================================
    # OLDER QUERIES (commented out)
    # ============================================================
    
    # # Cat illustrations
    # "cute 2d cat illustration",
    # "cute 2d cat cartoon illustration",
    # "cute 2d cat flat illustration",
    # "cute 2d cat vector illustration",
    # "cute 2d cat kawaii illustration",
    # "cute 2d cat pastel illustration",
    # "cute 2d cat minimal illustration",
    # "cute 2d cat chibi illustration",
    
    # # Fox illustrations
    # "cute 2d fox illustration",
    # "cute 2d fox cartoon illustration",
    # "cute 2d fox flat illustration",
    # "cute 2d fox vector illustration",
    # "cute 2d fox kawaii illustration",
    # "cute 2d fox pastel illustration",
    # "cute 2d fox minimal illustration",
    # "cute 2d fox chibi illustration",
    
    # # Bear illustrations
    # "cute 2d bear illustration",
    # "cute 2d bear cartoon illustration",
    # "cute 2d bear flat illustration",
    # "cute 2d bear vector illustration",
    # "cute 2d bear kawaii illustration",
    # "cute 2d bear pastel illustration",
    # "cute 2d bear minimal illustration",
    # "cute 2d bear chibi illustration",
    
    # # Bunny illustrations
    # "cute 2d bunny illustration",
    # "cute 2d bunny cartoon illustration",
    # "cute 2d bunny flat illustration",
    # "cute 2d bunny vector illustration",
    # "cute 2d bunny kawaii illustration",
    # "cute 2d bunny pastel illustration",
    # "cute 2d bunny minimal illustration",
    # "cute 2d bunny chibi illustration",
    
    # # Panda illustrations
    # "cute 2d panda illustration",
    # "cute 2d panda cartoon illustration",
    # "cute 2d panda flat illustration",
    # "cute 2d panda vector illustration",
    # "cute 2d panda kawaii illustration",
    # "cute 2d panda pastel illustration",
    # "cute 2d panda minimal illustration",
    # "cute 2d panda chibi illustration",
    
    # # Dog illustrations
    # "cute 2d dog illustration",
    # "cute 2d dog cartoon illustration",
    # "cute 2d dog flat illustration",
    # "cute 2d dog vector illustration",
    # "cute 2d dog kawaii illustration",
    # "cute 2d dog pastel illustration",
    # "cute 2d dog minimal illustration",
    # "cute 2d dog chibi illustration",
]

MIN_DIMENSION = 800
MAX_IMAGES_PER_QUERY = 100
TOTAL_TARGET_IMAGES = 10000
HASH_THRESHOLD = 10  # Perceptual hash similarity threshold


# ============================================================
# BLOCKED CONTENT KEYWORDS
# ============================================================

BLOCKED_KEYWORDS = {
    # Real humans indicators
    "photograph", "photo", "photography", "portrait", "selfie", "headshot",
    "real person", "celebrity", "actor", "actress", "singer", "musician",
    "model photo", "instagram", "tiktok", "influencer", "photoshoot",
    "realistic", "hyperrealistic",
    
    # Cartoon characters (popular)
    "mickey mouse", "donald duck", "minnie", "goofy", "disney",
    "spongebob", "patrick star", "tom and jerry", "bugs bunny", "daffy duck",
    "scooby doo", "shaggy", "pokemon", "pikachu", "charizard",
    "hello kitty", "sanrio", "doraemon", "shin chan", "peppa pig",
    "paw patrol", "dora", "bob the builder", "thomas train",
    "powerpuff girls", "cartoon network", "nickelodeon",
    
    # Anime/Manga characters
    "naruto", "sasuke", "goku", "dragon ball", "one piece", "luffy",
    "attack on titan", "demon slayer", "jujutsu kaisen", "my hero academia",
    "sailor moon", "studio ghibli", "totoro", "spirited away",
    "anime", "manga", "otaku", "waifu",
    
    # Marvel characters
    "spider-man", "spiderman", "iron man", "ironman", "captain america",
    "thor", "hulk", "black widow", "hawkeye", "black panther", "doctor strange",
    "scarlet witch", "vision", "ant-man", "wasp", "falcon", "winter soldier",
    "groot", "rocket raccoon", "star-lord", "gamora", "drax", "thanos", "loki",
    "wolverine", "x-men", "deadpool", "venom", "carnage", "magneto",
    "avengers", "guardians of the galaxy", "fantastic four", "daredevil",
    "marvel", "mcu",
    
    # DC characters
    "batman", "superman", "wonder woman", "aquaman", "flash", "green lantern",
    "cyborg", "shazam", "green arrow", "supergirl", "batgirl", "robin", "nightwing",
    "joker", "harley quinn", "catwoman", "riddler", "bane", "poison ivy",
    "justice league", "dc comics", "gotham", "metropolis", "arkham", "wayne",
    
    # Movie/Series characters
    "harry potter", "hermione", "ron weasley", "dumbledore", "voldemort",
    "lord of the rings", "frodo", "gandalf", "aragorn", "legolas",
    "star wars", "darth vader", "luke skywalker", "yoda", "baby yoda",
    "game of thrones", "khaleesi", "jon snow",
    "stranger things", "breaking bad", "the office", "friends sitcom",
    "walking dead", "money heist", "squid game", "peaky blinders",
    "mandalorian", "witcher", "netflix", "hbo",
    
    # Other fictional characters
    "shrek", "frozen", "elsa", "anna", "moana", "rapunzel", "cinderella",
    "snow white", "ariel", "belle", "jasmine", "mulan", "pocahontas",
    "toy story", "woody", "buzz lightyear", "finding nemo", "dory",
    "monsters inc", "cars", "pixar", "dreamworks",
}

# Patterns to detect real humans in alt text
REAL_HUMAN_PATTERNS = [
    "photo", "photograph", "photography",
    "portrait", "selfie", "headshot",
    "celebrity", "actor", "actress", "singer", "model",
    "real", "realistic",
]


class IllustrationScraper:
    def __init__(self):
        self.output_dir = Path(OUTPUT_FOLDER)
        self.output_dir.mkdir(exist_ok=True)
        self.csv_file = CSV_FILE
        
        # Tracking
        self.collected_urls = set()
        self.collected_images = []
        self.image_hashes = {}  # hash -> (size, filepath, index)
        self.filtered_count = 0
        self.duplicate_count = 0
        
        self._load_existing_data()
    
    def _load_existing_data(self):
        """Load existing data to avoid duplicates"""
        if os.path.exists(self.csv_file):
            with open(self.csv_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if "image_link" in row:
                        self.collected_urls.add(row["image_link"])
                    if "phash" in row and row["phash"]:
                        try:
                            w = int(row.get("width", 0))
                            h = int(row.get("height", 0))
                            img_hash = imagehash.hex_to_hash(row["phash"])
                            self.image_hashes[img_hash] = (w * h, row.get("file_path", ""), len(self.collected_images))
                            self.collected_images.append(row)
                        except:
                            pass
            print(f"Loaded {len(self.collected_urls)} existing URLs")
    
    def _is_blocked_content(self, text: str) -> tuple[bool, str]:
        """Check if text contains blocked keywords"""
        if not text:
            return False, ""
        
        text_lower = text.lower()
        
        for keyword in BLOCKED_KEYWORDS:
            if keyword in text_lower:
                return True, keyword
        
        for pattern in REAL_HUMAN_PATTERNS:
            if pattern in text_lower:
                return True, f"human:{pattern}"
        
        return False, ""
    
    def _compute_image_hash(self, img: Image.Image) -> imagehash.ImageHash:
        """Compute perceptual hash for image"""
        return imagehash.phash(img)
    
    def _is_duplicate_image(self, img_hash: imagehash.ImageHash, img_size: int) -> tuple[bool, str | None]:
        """Check if image is a duplicate based on perceptual hash"""
        for existing_hash, (existing_size, existing_path, _) in self.image_hashes.items():
            hamming_distance = img_hash - existing_hash
            if hamming_distance <= HASH_THRESHOLD:
                if img_size > existing_size:
                    # New image is larger, replace old one
                    print(f"  ↑ Replacing smaller duplicate with larger version")
                    return False, existing_path
                else:
                    # Existing image is larger or same, skip new one
                    print(f"  ⊘ Duplicate detected (hash distance: {hamming_distance})")
                    return True, None
        return False, None
    
    def _download_and_validate(self, url: str, query: str) -> dict | None:
        """Download image and validate it meets requirements"""
        try:
            # Skip if URL already collected
            if url in self.collected_urls:
                return None
            
            # Download image
            response = requests.get(url, timeout=30)
            if response.status_code != 200:
                return None
            
            content = response.content
            img = Image.open(BytesIO(content))
            width, height = img.size
            
            # Check minimum dimension (both must be >= 800)
            if width < MIN_DIMENSION or height < MIN_DIMENSION:
                return None
            
            # Compute perceptual hash
            img_hash = self._compute_image_hash(img)
            img_size = width * height
            
            # Check for duplicates
            is_dup, existing_path = self._is_duplicate_image(img_hash, img_size)
            
            if is_dup:
                self.duplicate_count += 1
                return None
            
            # Generate filename
            pin_id = hashlib.md5(url.encode()).hexdigest()[:16]
            ext = url.split(".")[-1].split("?")[0]
            if ext not in ["jpg", "jpeg", "png", "gif", "webp"]:
                ext = "jpg"
            filename = f"illustration_{pin_id}.{ext}"
            filepath = self.output_dir / filename
            
            # Replace smaller duplicate if exists
            if existing_path and os.path.exists(existing_path):
                os.remove(existing_path)
                self.collected_images = [r for r in self.collected_images if r.get("file_path") != existing_path]
                self.image_hashes = {h: v for h, v in self.image_hashes.items() if v[1] != existing_path}
            
            # Save image
            with open(filepath, "wb") as f:
                f.write(content)
            
            # Track hash
            self.image_hashes[img_hash] = (img_size, str(filepath), len(self.collected_images))
            self.collected_urls.add(url)
            
            return {
                "height": height,
                "width": width,
                "page_link": "",
                "image_link": url,
                "platform": "pinterest",
                "file_path": str(filepath),
                "timestamp": datetime.now().isoformat(),
                "phash": str(img_hash),
                "query": query,
            }
        except Exception as e:
            return None
    
    def _save_to_csv(self):
        """Save collected images to CSV"""
        if not self.collected_images:
            return
        
        fieldnames = ["height", "width", "page_link", "image_link", "platform", "file_path", "timestamp", "phash", "query"]
        
        with open(self.csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for record in self.collected_images:
                writer.writerow(record)
    
    def scrape(self):
        """Main scraping function"""
        print(f"{'='*60}")
        print(f"Pinterest Illustration Scraper (pinscrape)")
        print(f"{'='*60}")
        print(f"Target images: {TOTAL_TARGET_IMAGES}")
        print(f"Min dimension: {MIN_DIMENSION}px (both width AND height)")
        print(f"Output folder: {OUTPUT_FOLDER}")
        print(f"CSV file: {CSV_FILE}")
        print(f"{'='*60}\n")
        
        pinterest = Pinterest(proxies={}, sleep_time=2)
        
        for query in SEARCH_QUERIES:
            if len(self.collected_images) >= TOTAL_TARGET_IMAGES:
                break
            
            # Check if query itself contains blocked content
            is_blocked, blocked_reason = self._is_blocked_content(query)
            if is_blocked:
                print(f"🚫 Skipping blocked query: '{query}' (reason: {blocked_reason})")
                continue
            
            print(f"\n🔍 Searching: '{query}'")
            
            try:
                # Get image URLs using pinscrape
                image_urls = pinterest.search(query, MAX_IMAGES_PER_QUERY)
                
                if not image_urls:
                    print(f"   No images found for '{query}'")
                    continue
                
                print(f"   Found {len(image_urls)} URLs")
                
                downloaded = 0
                for url in image_urls:
                    if len(self.collected_images) >= TOTAL_TARGET_IMAGES:
                        break
                    
                    # Validate and download
                    result = self._download_and_validate(url, query)
                    
                    if result:
                        self.collected_images.append(result)
                        downloaded += 1
                        print(f"  ✓ [{len(self.collected_images)}] {result['width']}x{result['height']} - {query[:30]}...")
                        
                        # Save CSV after each download (real-time update)
                        self._save_to_csv()
                
                print(f"   Downloaded: {downloaded} images from this query")
                
            except Exception as e:
                print(f"   Error with query '{query}': {e}")
                continue
        
        # Final save
        self._save_to_csv()
        
        print(f"\n{'='*60}")
        print(f"✅ Scraping Complete!")
        print(f"{'='*60}")
        print(f"Total images collected: {len(self.collected_images)}")
        print(f"Duplicates skipped: {self.duplicate_count}")
        print(f"Blocked content: {self.filtered_count}")
        print(f"Saved to: {CSV_FILE}")
        print(f"Images in: {OUTPUT_FOLDER}")
        print(f"{'='*60}")


def main():
    scraper = IllustrationScraper()
    scraper.scrape()


if __name__ == "__main__":
    main()
