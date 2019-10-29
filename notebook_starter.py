
# To display the output of all commands
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"  # none last


# ======== Setting up project and bucket ===========
#PROJECT_ID = 'your-google-cloud-project'
PROJECT_ID = 'deep-learning-course-v3'
BUCKET_NAME='lesson1' # Optional (we will create one)

from google.cloud import storage
storage_client = storage.Client(project=PROJECT_ID)

# ======== Working with buckets ===========
f'# List buckets'
buckets = storage_client.list_buckets()
bucket_names=[x.name for x in buckets]
bucket_names


f'# Create dummy bucket'
SUFFIX="-0124234e7" # To help making names unique
BUCKET_NAME="dummy_bucket"+SUFFIX
if BUCKET_NAME not in bucket_names:
    bucket = storage_client.create_bucket(BUCKET_NAME)


f'# Access bucket called {BUCKET_NAME}'
#bucket = storage_client.get_bucket(BUCKET_NAME)
bucket = storage_client.get_bucket(BUCKET_NAME)


f'# List files on bucket {bucket.name}'
[print(x.name) for x in bucket.list_blobs()]
#[print(x) for x in bucket.list_blobs()]



# ======== Transfering files ===========

DESTINATION_FILE_NAME=SOURCE_FILE_NAME="dummy_file"

f'# Create a dummy file to upload'
!echo "hello there" >> dummy_file
!ls -lh


f'# Upload file {SOURCE_FILE_NAME} to bucket'
blob = bucket.blob(DESTINATION_FILE_NAME)
blob.upload_from_filename(SOURCE_FILE_NAME)

[print(x.name) for x in bucket.list_blobs()]


f'# Download file {DESTINATION_FILE_NAME}'
blob = bucket.blob(DESTINATION_FILE_NAME)
blob.download_to_filename(SOURCE_FILE_NAME+"downloaded")

!ls -lh



#====== working with pickle and cloud ======

import pickle
PICKLE_FILE_NAME="objects.pkl"
LIST_OBJECTS_TO_SAVE=[a,b,c]

# Saving the objects to local file
pickle.dump(LIST_OBJECTS_TO_SAVE, open(PICKLE_FILE_NAME,"wb"), protocol=-1)

!ls -lh

# Copy file to cloud
SOURCE_FILE_NAME=DESTINATION_FILE_NAME=PICKLE_FILE_NAME

f'# Upload file {SOURCE_FILE_NAME} to bucket'
blob = bucket.blob(DESTINATION_FILE_NAME)
blob.upload_from_filename(SOURCE_FILE_NAME)

# Verify
[print(x.name) for x in bucket.list_blobs()]

# Copy file from Cloud into notebook

f'# Download file {DESTINATION_FILE_NAME}'
blob = bucket.blob(DESTINATION_FILE_NAME)
blob.download_to_filename(SOURCE_FILE_NAME+"downloaded")

!ls -lh

# Getting back the objects
a1,b1,c1 = pickle.load(open(PICKLE_FILE_NAME+"downloaded","rb"))
