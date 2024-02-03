# run using docker
docker build -t custom-whisper-api-image .
docker run --name custom-whisper-api-container -d -p 8000:8000 -v $(pwd):/code custom-whisper-api-image

#connect to turborepo
git subtree add --prefix=apps/custom-whisper-api https://github.com/valiantlynx/custom-whisper-api.git main --squash
git subtree pull --prefix=apps/custom-whisper-api https://github.com/valiantlynx/custom-whisper-api.git main --squash
git subtree push --prefix=apps/custom-whisper-api https://github.com/valiantlynx/custom-whisper-api.git main
