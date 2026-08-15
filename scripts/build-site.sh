#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="$project_root/src/site"
output_dir="$project_root/dist"
stage_dir="$(mktemp -d "${TMPDIR:-/tmp}/mal-site.XXXXXX")"

cleanup() {
  rm -rf "$stage_dir"
}
trap cleanup EXIT

cp "$source_root/pages/landing.html" "$stage_dir/index.html"
cp "$source_root/pages/landing.html" "$stage_dir/landing.html"
find "$source_root/pages" -maxdepth 1 -type f -name '*.html' ! -name 'landing.html' -exec cp {} "$stage_dir"/ \;
cp -R "$source_root/assets/icons/." "$stage_dir/"
cp -R "$source_root/assets/images/." "$stage_dir/"
cp -R "$source_root/assets/styles/." "$stage_dir/"
cp -R "$source_root/assets/scripts/." "$stage_dir/"
cp -R "$source_root/assets/logo" "$stage_dir/"
cp -R "$source_root/assets/metadata/." "$stage_dir/"

for route_name in homework assignment-2 lab3 organizers; do
  mkdir -p "$stage_dir/$route_name"
  cp "$source_root/pages/$route_name.html" "$stage_dir/$route_name/index.html"
done

mkdir -p "$stage_dir/sponsor"
cp "$source_root/pages/sponsor-deck.html" "$stage_dir/sponsor/index.html"

cp "$project_root/src/content/briefs/MAL_LAB1_HOMEWORK.md" "$stage_dir/"
cp "$project_root/src/content/briefs/MAL_LAB2_HOMEWORK.md" "$stage_dir/"

rm -rf "$output_dir"
mv "$stage_dir" "$output_dir"
trap - EXIT

printf 'Built static site in %s\n' "$output_dir"
