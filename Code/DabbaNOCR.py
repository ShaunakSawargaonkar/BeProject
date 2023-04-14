import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches



def dabbaNOCR(imagePath):
    # TODO
    
    # print("from dabba here")
    # Load the EasyOCR reader with the English language
    reader = easyocr.Reader(['en'])

    # Load the image
    image = plt.imread(imagePath)

    # Perform OCR on the image
    results = reader.readtext(image)

    # Create a figure and axes
    fig, ax = plt.subplots(1)

    # Display the image
    ax.imshow(image)

    output=""
    # Draw bounding boxes around the detected text regions
    for result in results:
        # Get the coordinates of the bounding box
        bbox = result[0]

        # Create a rectangle patch
        rect = patches.Rectangle((bbox[0][0], bbox[0][1]), bbox[2][0]-bbox[0][0], bbox[2][1]-bbox[0][1], linewidth=2, edgecolor='g', facecolor='none')

        # Add the rectangle patch to the axes
        ax.add_patch(rect)
        
        output+=result[1]
        output+=" "

    # print(output)
    
    # Show the image with the bounding boxes
    plt.show()
    return output
