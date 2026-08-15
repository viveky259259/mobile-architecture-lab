#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dist_dir="$project_root/dist"

bash "$project_root/scripts/build-site.sh"

required_files=(
  index.html landing.html homework.html assignment-2.html lab3.html organizers.html
  sponsor-deck.html security-adr-handout.html 404.html robots.txt sitemap.xml motion.css motion.js favicon.svg
  apple-touch-icon.png icon-512.png og-image.png MAL_LAB1_HOMEWORK.md
  MAL_LAB2_HOMEWORK.md
)

for file in "${required_files[@]}"; do
  test -f "$dist_dir/$file" || {
    printf 'Missing build output: %s\n' "$file" >&2
    exit 1
  }
done

for page in homework assignment-2 lab3 organizers; do
  cmp -s "$dist_dir/$page.html" "$dist_dir/$page/index.html" || {
    printf 'Route output diverged from canonical page: %s\n' "$page" >&2
    exit 1
  }
done

cmp -s "$dist_dir/sponsor-deck.html" "$dist_dir/sponsor/index.html" || {
  printf 'Route output diverged from canonical page: sponsor\n' >&2
  exit 1
}

test ! -d "$dist_dir/server" || {
  printf 'Unexpected worker output in Netlify build\n' >&2
  exit 1
}

if rg -n 'mobilearchitecturelab\.netlify\.app' "$project_root/README.md" "$project_root/netlify.toml" "$project_root/src/site"; then
  printf 'Stale deployment domain found in site source\n' >&2
  exit 1
fi

printf 'Verified %s\n' "$dist_dir"
