def format_model_chunk(model):
    """
    Convert a model's metadata into a readable text chunk.

    Args:
        model (dict): A dictionary containing model details.

    Returns:
        str: Formatted chunk as a string.
    """
    chunk = f"Model: {model['name']}\n"
    chunk += f"Description: {model.get('description', 'No description available.')}\n"
    chunk += f"Materialization: {model.get('materialization', 'unknown')}\n"
    chunk += "Columns:\n"

    if model.get('columns'):
        for col in model['columns']:
            col_name = col['name']
            col_desc = col.get('description', 'No description provided.')
            chunk += f"  - {col_name}: {col_desc}\n"
    else:
        chunk += "  No columns available.\n"

    return chunk

def create_chunks(models):
    """
    Create formatted text chunks from a list of models.

    Args:
        models (list): List of model dictionaries.

    Returns:
        list: List of formatted chunks as strings.
    """
    chunks = []
    for model in models:
        chunk = format_model_chunk(model)
        chunks.append(chunk)
    return chunks
