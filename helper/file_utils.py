import os
import shutil

class FileUtils:
    
    @staticmethod
    def get_path_from_root(path: str) -> str:
        _root_dir = os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__))))
        return _root_dir + '/'+ path
    
    @staticmethod
    def create_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)
    
    @staticmethod
    def remove_dir(path):
        if os.path.exists(path):
            shutil.rmtree(path)
            
    @staticmethod
    def remove_file(path):
        try:
            if os.path.exists(path):
                os.remove(path)
            else:
                print(f"File not found: {path}")
        except Exception as e:
            print(f"Error deleting files: {e}")
        