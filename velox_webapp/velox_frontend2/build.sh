#!/bin/bash

rm -r dist/

npm run build-local

cp ./dist/index.html ../velox_backend/velox/templates/vue_index.html

rm -r ../velox_backend/velox_app/static/velox/
mkdir -p ../velox_backend/velox_app/static/velox/

cp -r ./dist/static/velox/* ../velox_backend/velox_app/static/velox/

#gsutil -m cp -r dist/* gs://cmmc_static_test/cmmc/js/
#gsutil iam -r ch allUsers:objectViewer gs://cmmc_static_test/cmmc/js
echo "done"
exit 0
