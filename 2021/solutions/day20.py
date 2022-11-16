'''
=========================================
|| 🎄 Advent of Code 2021: Day 20 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

LIGHT_PIXEL = '#'

### Part One
def part_one(input):
    return helper(input, 2)

### Part Two
def part_two(input):
    return helper(input, 50)


def helper(input, n):
    image, enhancement_algorithm, background_changes = parse_input(input)
    background = False

    # Enhance image n times
    for _ in range(n):
        image = enhance_image(image, enhancement_algorithm, background)

        # Condition to change the infinite background's pixel value
        if background_changes: background = not background

    return len(image)

def parse_input(input):
    # Initialize enhancement algorithm, marking light pixel values
    enhancement_algorithm = set([i for i, char in enumerate(input[0].strip()) if char == LIGHT_PIXEL])
    
    # Determine if infinite background will change after each enhancement
    background_changes = 0 in enhancement_algorithm

    # Save image relevant information: light pixel coordinates
    image = set()
    for i, line in enumerate([line for line in input if line.strip()]):
        for j, pixel in enumerate(line):
            if pixel == LIGHT_PIXEL: image.add((i, j))

    return image, enhancement_algorithm, background_changes

def enhance_image(image, enhancement_algorithm, background):
    top, bottom, left, right = calculate_image_bounds(image)
    enhanced_image = set()

    # Loop through all pixels to enhance
    for i, j in [(i, j) for i in range(top-1, bottom+2) for j in range(left-1, right+2)]:            
        
        new_pixel = ''
        # Check the 9 surrounding pixels to determine the new pixel's value
        for pixel in [(pixel_i, pixel_j) for pixel_i in range(i-1,i+2) for pixel_j in range(j-1, j+2)]:
            # Verify if the pixel being checked is within the image bounds
            if pixel[0] >= top and pixel[0] <= bottom and pixel[1] >= left and pixel[1] <= right:
                new_pixel += '1' if (pixel[0], pixel[1]) in image else '0'
            else:
                new_pixel += '1' if background else '0'

        # Add the coordinates to the enhanced image if the new pixel is light
        if int(new_pixel, 2) in enhancement_algorithm: 
            enhanced_image.add((i, j))
    
    return enhanced_image

def calculate_image_bounds(image):
    top = left = float('inf')
    bottom = right = float('-inf')
    
    for light_pixel in image:
        top = min(top, light_pixel[0])
        bottom = max(bottom, light_pixel[0])
        left = min(left, light_pixel[1])
        right = max(right, light_pixel[1])

    return (top, bottom, left, right)
