from pathlib import Path 

def input_scan_files(settings):
    '''
    scan input files and read files names based on supported extension
    '''
    input_directory = settings.get("input_directory")
    supported_extension = settings.get("supported_extension")

    input_path = Path(input_directory)

    if not input_path.exists():
        return None
    
    if not input_path.is_dir():
        return None

    file_names = []

    for file in input_path.iterdir():
        if file.suffix == supported_extension:
            file_names.append(file.name)
        
    return sorted(file_names)
