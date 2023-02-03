import streamlit as st
import numpy as np
from PIL import Image
import cv2 



st.set_option('deprecation.showfileUploaderEncoding', False)






st.title('Image processing in Streamlit')

file = st.file_uploader("Upload an image", type=["jpg", "png"])


if file is None:
	st.text('Waiting for upload....')

else:
	slot = st.empty()
	slot.text('images : ')

	# original
	test_image = Image.open(file)
	st.image(test_image, caption="original image", width = 400)


	# numpy version for opencv processing
	img = np.asarray(test_image)



	# gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	st.image(gray, caption="gray scaled image", width = 400)

	# gaussian blur
	gauss = cv2.GaussianBlur(img,(5,5),0)
	st.image(gauss, caption="gaussian blur", width = 400)


	# finished
	st.success('Done')

