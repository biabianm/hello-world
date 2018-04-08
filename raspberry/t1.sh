echo "order:channel: $1  filename: $2"
aplay -D plughw:0,0,$1 $2 &

