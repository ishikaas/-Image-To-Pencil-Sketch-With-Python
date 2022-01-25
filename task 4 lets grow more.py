#!/usr/bin/env python
# coding: utf-8

# # pip install opencv-python
# 

# In[13]:


import cv2


# # Importing the image

# In[ ]:


image = cv2.imread("puppy.jpg")
cv2.imshow("puppy", image)
cv2.waitKey(0)


# # Gray image

# In[ ]:


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Dog", gray_image)
cv2.waitKey(0)


# # Inverted Image

# In[ ]:


blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)


# In[ ]:


inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()


# # Dividing the gray image and inverted blurred image arrays to produce the Sketch

# In[ ]:


pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)
#cv2.imshow("skecth",pencil_sketch)


# # Sketch Image

# In[ ]:


cv2.imshow("original image",image)
cv2.imshow("sketch",pencil_sketch)
cv2.waitKey(0)


# In[ ]:




