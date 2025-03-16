# Generator function to read file in chunks
def read_file_in_chunks(file_name, chunk_size=1024):
    with open(file_name, 'rb') as file:  # Open in binary mode for chunks
        while chunk := file.read(chunk_size):
            yield chunk  # Yield each chunk of data

# Example usage
file_name = "large_file.bin"
for chunk in read_file_in_chunks(file_name, 2048):  # Reading file in 2KB chunks
    print(chunk)  # Process each chunk
