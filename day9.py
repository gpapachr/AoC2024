import time
from dataclasses import dataclass

@dataclass
class Block:
    block_type: int  # 0 for space, 1 for file
    files: list[int]
    space_length: int

    TYPE_FILE = 1
    TYPE_SPACE = 0

def process_input(file_path):
    with open(file_path, 'r') as file:
        input_str = file.read().strip()

    blocks = []
    block_type = Block.TYPE_FILE  # Alternating between file and space blocks
    file_id = 0
    space_count = 0
    space_ids = []

    for i in map(int, input_str):
        if block_type == Block.TYPE_FILE:
            block = Block(
                block_type=block_type,
                files=[file_id] * i,
                space_length=0,
            )
            blocks.append(block)
            file_id += 1
        else:
            if i > 0:
                space_count += i
                space_ids.append(len(blocks))
                block = Block(
                    block_type=block_type,
                    files=[],
                    space_length=i,
                )
                blocks.append(block)
        block_type = (block_type + 1) % 2  # Alternate between file and space

    return blocks, space_count, space_ids

def move_file_blocks(blocks, space_count, space_ids):
    curr_block = []  # Current block being moved
    curr_space_id = space_ids.pop(0)  # ID of the first available space block

    while space_count:
        if len(curr_block) == 0:
            if blocks[-1].block_type == Block.TYPE_SPACE and len(blocks[-1].files) == 0:
                blocks.pop()
                space_ids.pop()
                continue
            if blocks[-1].block_type == Block.TYPE_FILE:
                curr_block = blocks.pop().files

        try:
            item = curr_block.pop()
        except IndexError:
            break

        # Place the file into the current space block
        blocks[curr_space_id].files.append(item)
        blocks[curr_space_id].space_length -= 1
        space_count -= 1

        if blocks[curr_space_id].space_length == 0:
            blocks[curr_space_id].block_type = 1
            if space_ids:
                curr_space_id = space_ids.pop(0)
            else:
                break

    if curr_block:
        blocks.append(
            Block(
                block_type=Block.TYPE_FILE,
                files=curr_block,
                space_length=0,
            )
        )
    return blocks

def move_entire_file_blocks(blocks, space_count, space_ids):
    curr_block_id = len(blocks) - 1  # Start from the last block

    while curr_block_id > 0:
        if blocks[curr_block_id].block_type == Block.TYPE_SPACE:
            curr_block_id -= 1  # Skip space blocks
            continue

        curr_block_len = len(blocks[curr_block_id].files)  # Length of the current block
        for curr_space_id in space_ids:
            if curr_space_id >= curr_block_id:
                break  # Stop if space is beyond the current file block

            if blocks[curr_space_id].space_length >= curr_block_len:
                # Move the entire block to the space
                blocks[curr_space_id].files.extend(blocks[curr_block_id].files)
                blocks[curr_space_id].space_length -= curr_block_len

                # Update the original block to become a space block
                blocks[curr_block_id].block_type = Block.TYPE_SPACE
                blocks[curr_block_id].space_length = curr_block_len
                blocks[curr_block_id].files = []

                if blocks[curr_space_id].space_length == 0:
                    space_ids.remove(curr_space_id)  # Remove full space blocks

                break

        curr_block_id -= 1
    return blocks

def calculate_checksum(blocks):
    checksum = 0
    pos = 0
    for block in blocks:
        for file in block.files:
            checksum += pos * file  # Multiply file ID by its position
            pos += 1
    return checksum

def calculate_checksum_updated(blocks):
    checksum = 0
    pos = 0
    for block in blocks:
        for file in block.files:
            checksum += pos * file
            pos += 1
        if block.block_type == Block.TYPE_SPACE:
            pos += block.space_length  # Account for space blocks
    return checksum

file_path = 'inputs/input9.txt'

# Part 1: 
blocks, space_count, space_ids = process_input(file_path)
blocks_arranged = move_file_blocks(blocks, space_count, space_ids)
check_sum = calculate_checksum(blocks_arranged)
print(f"The final check sum is: {check_sum}")

# Part 2: 
blocks, space_count, space_ids = process_input(file_path)
blocks_arranged = move_entire_file_blocks(blocks, space_count, space_ids)
check_sum = calculate_checksum_updated(blocks_arranged)
print(f"The final check sum is: {check_sum}")
