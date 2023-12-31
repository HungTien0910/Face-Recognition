import os

if os.path.exists("AI-Product\cropped")==False:
    os.makedirs("AI-Product\cropped")

ALPHA = 1.0
THRESHOLD = 0.5
IMAGE_SIZE= 160
LAYERS_TO_FREEZE= 60
NUM_EPOCHS= 30
STEPS_PER_EPOCH= 1
BATCH_SIZE= 16
LEARNING_RATE = 0.001
MARGIN = 0.2
EMBEDDING_SIZE = 128    