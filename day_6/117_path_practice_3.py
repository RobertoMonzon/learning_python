# Implement and create an absolute path that allows us to reach the "user/practices/practice_path.py" file from the following folder structure:

from pathlib import Path
 
ruta = Path(Path.home(), "user","pratices","practica_path.py")