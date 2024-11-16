# Predefined mapping for 7-segment displays
SEGMENT_MAP = {
    " _ | ||_|": "0", "     |  |": "1", " _  _||_ ": "2", " _  _| _|": "3",
    "   |_|  |": "4", " _ |_  _|": "5", " _ |_ |_|": "6", " _   |  |": "7",
    " _ |_||_|": "8", " _ |_| _|": "9",
    "   |     ": "+", "         ": "-", "         ": "%", "         ": "*", "         ": "="
}

# Function to parse a 3x3 grid into individual segments
def parse_segments(grid, n):
    segments = []
    for i in range(n):
        segment = "".join(grid[j][i*3:(i+1)*3] for j in range(3))
        segments.append(segment)
    return segments

# Function to toggle LEDs and find faulty character
def find_faulty_character(n, grid):
    segments = parse_segments(grid, n)
    chars = [SEGMENT_MAP.get(seg, "?") for seg in segments]
    
    # Sequentially evaluate the equation
    lhs = 0
    op = None
    for i, char in enumerate(chars):
        if char.isdigit():
            if op is None:
                lhs = int(char)
            else:
                rhs = int(char)
                if op == "+": lhs += rhs
                elif op == "-": lhs -= rhs
                elif op == "*": lhs *= rhs
                elif op == "%": lhs %= rhs
                op = None
        elif char in "+-*%":
            op = char
        elif char == "=":
            break
    
    rhs = int("".join(chars[i+1:]))
    
    # Validate result
    if lhs == rhs:
        return None
    
    # Find the faulty character
    for i, seg in enumerate(segments):
        original_char = chars[i]
        for valid_seg, valid_char in SEGMENT_MAP.items():
            if valid_char == original_char:
                continue
            # Check if toggling results in a match
            diff = sum(a != b for a, b in zip(seg, valid_seg))
            if diff == 1:  # Toggle one LED
                # Test the equation with this change
                chars[i] = valid_char
                if eval_equation(chars):
                    return i + 1
                chars[i] = original_char

# Example Usage
n = 5
grid = [
    "       _     _ ",
    "  ||_  _| _ |_|",
    "  ||  |_  _  _|"
]
print(find_faulty_character(n, grid))  # Output: 1
