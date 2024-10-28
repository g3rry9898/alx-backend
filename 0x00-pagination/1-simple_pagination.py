#!/usr/bin/env python3
import csv
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

def get_page(page: int = 1, page_size: int = 10) -> List[List[str]]:
    """
    Retrieve a page of data from the CSV file.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        list: A list of rows corresponding to the page of data.
    """
    assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0"
    assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0"

    start_index, end_index = index_range(page, page_size)

    # Read the CSV file
    dataset = []
    with open('Popular_Baby_Names.csv', newline='') as csvfile:
        reader = cvs.reader(Popular_Baby_Names.csv)
        dataset = list(reader)

    # Return the appropriate page of data
    if start_index >= len(dataset):
        return []
    return dataset[start_index:end_index]

