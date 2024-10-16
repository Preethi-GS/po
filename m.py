import difflib
import os

def read_file(filepath):
    """Read the source code file and return its contents."""
    with open(filepath, 'r') as file:
        return file.read()

def compare_files(file1, file2):
    """Compare the contents of two source code files."""
    code1 = read_file(file1)
    code2 = read_file(file2)
    
    # Use difflib to compare the similarity of the two files
    sequence_matcher = difflib.SequenceMatcher(None, code1, code2)
    similarity = sequence_matcher.ratio() * 100  # Get percentage similarity
    
    return similarity

def check_plagiarism(dir_path):
    """Check plagiarism for all files in a directory."""
    files = [f for f in os.listdir(dir_path) if f.endswith('.py')]
    plagiarism_results = []
    
    # Compare each file with every other file
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = os.path.join(dir_path, files[i])
            file2 = os.path.join(dir_path, files[j])
            similarity = compare_files(file1, file2)
            
            plagiarism_results.append((files[i], files[j], similarity))
    
    return plagiarism_results

if _name_ == "_main_":
    dir_path = "path/to/your/python/files"  # Set the directory path containing the Python files
    results = check_plagiarism(dir_path)
    
    # Output the results
    for file1, file2, similarity in results:
        print(f"Similarity between {file1} and {file2}: {similarity:.2f}%")