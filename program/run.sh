# echo "Sending video stream to server!"
# python3 .sending.py
echo "Server is processing the video..."
python3 human.py
echo "Server under process"
gsutil -m rsync -r ./output gs://innovation_lab/test1
# echo "clearing cache data"
rm -r ./output
