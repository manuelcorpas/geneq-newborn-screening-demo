#!/usr/bin/env python3
"""Generate data.js from cached analyses."""
import json
from pathlib import Path

cache_dir = Path(__file__).parent.parent / 'DATA' / 'demo_cache'
output_file = Path(__file__).parent / 'data.js'

# Load all cached content
uk = json.load(open(cache_dir / 'country_UK.json'))
australia = json.load(open(cache_dir / 'country_AUSTRALIA.json'))
comparison = json.load(open(cache_dir / 'compare_AUSTRALIA_UK.json'))
theme = json.load(open(cache_dir / 'theme_implementation_challenges.json'))

# Escape content for JavaScript template literals
def escape_js(text):
    return text.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

# Create JS data file
js_content = f'''// Demo data - pre-generated analyses from GENEQ Newborn Screening Agent
// Generated: {uk.get('generated_at', 'Unknown')}

const demoData = {{
    uk: `{escape_js(uk.get('analysis', ''))}`,
    australia: `{escape_js(australia.get('analysis', ''))}`,
    comparison: `{escape_js(comparison.get('analysis', ''))}`,
    theme: `{escape_js(theme.get('analysis', ''))}`
}};
'''

with open(output_file, 'w') as f:
    f.write(js_content)

print(f'Created {output_file}')
print(f'  UK: {len(uk.get("analysis", ""))} chars')
print(f'  Australia: {len(australia.get("analysis", ""))} chars')
print(f'  Comparison: {len(comparison.get("analysis", ""))} chars')
print(f'  Theme: {len(theme.get("analysis", ""))} chars')
