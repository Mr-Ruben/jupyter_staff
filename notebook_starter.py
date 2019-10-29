
# To display the output of all commands
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"  # none last


# Set your own project id here
#PROJECT_ID = 'your-google-cloud-project'
PROJECT_ID = 'deep-learning-course-v3'
BUCKET_NAME='example-lesson1' # Optional (we will create one)

from google.cloud import storage
storage_client = storage.Client(project=PROJECT_ID)



