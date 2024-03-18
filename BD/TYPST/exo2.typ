#show terms: meta => {
    let title = label("Integration Exercise")
    let duration = label("30min")
    let difficulty = label("hard")
    let solution = label("1")
    let figures = label("none")
    let points = label("20pts")
    let bonus = label("0")
    let author = label("none")
    let references = label("none")
    let language = label("english")
    let material = label("none")
}

= Exercise

Write an algorithm to find the maximum element in an array of integers.

= Soluce

#show terms: soluce => {
  ```py
  def find_max_element(arr):
    # Initialize max_element with the first element of the array
    max_element = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Update max_element if the current element is greater
        if num > max_element:
            max_element = num
    
    # Return the maximum element
    return max_element

# Example usage:
array = [3, 5, 2, 9, 10, 7, 1]
print("Maximum element in the array:", find_max_element(array))

  ```
}

