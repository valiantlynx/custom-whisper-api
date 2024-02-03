# run using docker
docker build -t depth-first-search-image .
docker run --name depth-first-search-container -d -p 8000:8000 -v $(pwd):/code depth-first-search-image

#connect to turborepo
git subtree add --prefix=apps/custom-whisper-api https://github.com/valiantlynx/custom-whisper-api.git main --squash
git subtree pull --prefix=apps/custom-whisper-api https://github.com/valiantlynx/custom-whisper-api.git main --squash
git subtree push --prefix=apps/custom-whisper-api https://github.com/valiantlynx/custom-whisper-api.git main
