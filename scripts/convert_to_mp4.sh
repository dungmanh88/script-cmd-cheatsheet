#!/bin/bash
filename=$1
program=ffmpeg
ext=mp4
$program -version > /dev/null 2>&1 || { echo "You must install ${program}"; exit 1; }
output=`echo $filename | cut -d "." -f 1`
output="$output.$ext"
echo $filename
echo $output
$program -i $filename -vcodec copy -acodec copy $output
