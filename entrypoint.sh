#!/usr/bin/env sh
set -e

# 1) Start the Lightdash server in the background
echo "Starting Lightdash server..."
lightdash start \
  --dbt-project-dir "${DBT_PROJECT_DIR}" \
  --port "${PORT}" &
LIGHTDASH_PID=$!

# 2) Wait for the /health endpoint to return 200
echo "Waiting for Lightdash to be healthy at http://localhost:${PORT}/health"
timeout=60
counter=0
while ! curl -fs "http://localhost:${PORT}/health" > /dev/null; do
  sleep 1
  counter=$((counter + 1))
  if [ "$counter" -ge "$timeout" ]; then
    echo "Timeout waiting for Lightdash"
    kill "$LIGHTDASH_PID" 2>/dev/null || true
    exit 1
  fi
done
echo "Lightdash is healthy!"

# 3) Perform login & deploy
echo "Logging in and deploying…"
lightdash login http://localhost:${PORT} --token "${LIGHTDASH_TOKEN}"
lightdash deploy --project-dir "${DBT_PROJECT_DIR}"

# 4) Bring the server process to the foreground
wait "$LIGHTDASH_PID"