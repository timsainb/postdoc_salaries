from pathlib2 import Path
import pathlib2
import os

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
FIGURE_DIR = PROJECT_DIR / "figures"

def ensure_dir(file_path):
    """ create a safely nested folder
    """
    if type(file_path) == str:
        if "." in os.path.basename(os.path.normpath(file_path)):
            directory = os.path.dirname(file_path)
        else:
            directory = os.path.normpath(file_path)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except FileExistsError as e:
                # multiprocessing can cause directory creation problems
                print(e)
    elif type(file_path) == pathlib2.PosixPath:
        # if this is a file
        if len(file_path.suffix) > 0:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        else:
            file_path.mkdir(parents=True, exist_ok=True)

import matplotlib.pyplot as plt
def save_fig(loc):
	plt.savefig(str(loc)+'.pdf',dpi=300, bbox_inches = 'tight',
    pad_inches = 0)
	plt.savefig(str(loc)+'.jpg',dpi=150, bbox_inches = 'tight',
	    pad_inches = 0)