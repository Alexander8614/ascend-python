from pathlib import Path
import csv
import sys
import json

DEBUG = True

DATA_DIR = Path('data')
VIDEOS_PATH = DATA_DIR / 'videos.csv'
HIGHLIGHTS_PATH = DATA_DIR / 'highlights.csv'
SUMMARY_PATH = DATA_DIR / 'summary.json'
LOG_PATH = DATA_DIR / 'run.log'
DATA_DIR.mkdir(exist_ok=True)
COLUMNS = ['title', 'views', 'duration_seconds', 'duration_mmss', 'published', 'views_vs_avg_pct']


def validate_title(title_data):
   title = title_data.strip()
   if title =='':
       raise ValueError('title is empty')
   return title

def validate_views(views_data):
    try:
        views = int(views_data)
    except ValueError:
        raise ValueError('views must be a whole number')
    if views < 0:
        raise ValueError('views cannot be negative')
    return views
    
def validate_duration_seconds(duration_seconds_data):
    try:
        duration_seconds = int(duration_seconds_data)
    except ValueError:
        raise ValueError('duration must be a whole number') 
    if duration_seconds > 0:
        return duration_seconds
    raise ValueError('duration must be positive')

def parse_tags(tags_data):
    raw_tags = tags_data.split(';')
    tags = []
    for raw_tag in raw_tags:
        clean_tag = raw_tag.lower().strip()
        if clean_tag != '': 
            tags.append(clean_tag)
    return tags

def mmss(duration_seconds):
    minutes = duration_seconds // 60
    seconds = duration_seconds % 60
    duration = f'{minutes}m {seconds}s'
    return duration

def validate_month(published_data):
    month = published_data[:7]
    return month

videos = []
errors = []
try:
    with open(VIDEOS_PATH,newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for n,row in enumerate(reader,start=1):
            video = {}
            label = row['title'].strip() or f'row {n}'
            try:
                video['title'] = validate_title(row['title'])
                video['views'] = validate_views(row['views'])
                duration_seconds = validate_duration_seconds(row['duration_seconds'])
                video['duration_seconds'] = duration_seconds
                video['tags'] = parse_tags(row['tags']) 
                video['duration_mmss'] = mmss(duration_seconds)
                video['published'] = (row['published'])
                video['month'] = validate_month(row['published'])
                videos.append(video)
            except ValueError as err:            
                errors.append(f'{label} - {err}')
except FileNotFoundError:
    print(f"""Could not find the file.
        Looked for {VIDEOS_PATH.absolute()}
        Put the videos file in that folder,
        or check the filename is exactly videos.csv, then run this again.""")
    sys.exit(1)


def calculate_average_views(videos):
    total_views = 0
    for video in videos:
        total_views = video['views'] + total_views
    return (float(total_views / len(videos)), total_views)

def calculate_highlights(videos, average):
    highlights = []
    for video in videos:
        if video['views'] > average:
            video['views_vs_avg_pct'] =round((video['views'] / average - 1) * 100)
            highlights.append(video)        
    return highlights

def calculate_tag_counts(videos):
    tag_counts = {}
    for video in videos:
        for tag in video['tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) +1
    return tag_counts

def calculate_views_by_month(videos):
    views_by_month = {}
    for video in videos:
        views_by_month[video['month']] = views_by_month.get(video['month'], 0) + video['views']
    return views_by_month 

def calculate_longest_video(videos):
    longest_video = None
    if len(videos) == 0:
        longest_video = {'title': None, 'views': None, 'duration_seconds': None, 'duration_mmss': None, 'published' : None, 'views_vs_avg_pct': None}
    else:
        for video in videos:
            if longest_video is None or  video['duration_seconds'] > longest_video['duration_seconds']:
                longest_video = video
    return longest_video

if len(videos) == 0:
    average_views = 0
    total_views = 0
else:
    average_views, total_views = calculate_average_views(videos)

highlights = calculate_highlights(videos, average_views)
tag_counts = calculate_tag_counts(videos)
views_by_month = calculate_views_by_month(videos)
longest_video = calculate_longest_video(videos)
total_views_by_month = sum(views_by_month.values())

assert total_views_by_month == total_views, f'views_by_month should sum to total_views: got {total_views_by_month:,} vs {total_views:,}'
        
print(f'{'TITLE':<32}{'VIEWS':>9}{'VS AVG':>8}')

total_highlight_views = 0               
for highlight in highlights:
            print(f'{highlight['title']:<32}{highlight['views']:>9,}{highlight['views_vs_avg_pct']:>7}%')
            total_highlight_views = highlight['views'] + total_highlight_views
print(f'{'TOTAL':<32}{total_highlight_views:>9,}')


with open(HIGHLIGHTS_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction='ignore')
    writer.writeheader()
    for highlight in highlights:
         writer.writerow(highlight)
if DEBUG:
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write('--- run start ---\n')
        for error in errors:
            f.write(f'REJECTED: {error}\n')
        f.write(f'--- run end: {len(videos)} valid, {len(errors)} rejected ---\n')



summary = {'total_rows_read': (len(videos) + len(errors)), 'valid_rows': (len(videos)), 'rejected_rows': (len(errors)), 'average_views': (average_views), 'highlight_count': (len(highlights))}
summary['highlight_titles'] = []
for highlight in highlights:
    summary['highlight_titles'].append(highlight['title'])
summary['longest_video'] = longest_video['title']
summary['longest_duration_mmss'] =longest_video['duration_mmss']
summary['tag_counts'] = tag_counts
summary['views_by_month'] = views_by_month
summary['errors'] = errors

json_summary = json.dumps(summary,indent=2)
print(json_summary)

with open(SUMMARY_PATH, 'w', encoding='utf-8') as f:
    f.write(json_summary)

    
for path in sorted(DATA_DIR.glob('*')):
    print(f'  {path.name:16} {path.stat().st_size:>6} bytes')

   

