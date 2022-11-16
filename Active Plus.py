#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install mediapipe opencv-python')
import mediapipe as mp
import cv2


# In[3]:


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic


# In[4]:


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('MediaPipe test for Active Plus', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()


# In[6]:


cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        #Recolor 
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        print(results)
    
        cv2.imshow('MediaPipe test for Active Plus', frame)
    
        if cv2.waitKey(10) & 0xFF == ord('q'):
             break
   
cap.release()
cv2.destroyAllWindows()


# In[ ]:


cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        #Recolor 
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        print(results.face_landmarks)
    
        cv2.imshow('MediaPipe test for Active Plus', frame)
    
        if cv2.waitKey(10) & 0xFF == ord('q'):
             break
   
cap.release()
cv2.destroyAllWindows()


# In[8]:


cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        #Recolor 
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        print(results.pose_landmarks)
    
        cv2.imshow('MediaPipe test for Active Plus', frame)
    
        if cv2.waitKey(10) & 0xFF == ord('q'):
             break
   
cap.release()
cv2.destroyAllWindows()


# In[ ]:


cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        #Recolor 
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        print(results.face_landmarks)
        
        #face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
        
        #Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        #Draw face landmarks
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONTOURS)
        
    
        cv2.imshow('MediaPipe test for Active Plus', frame)
    
        if cv2.waitKey(10) & 0xFF == ord('q'):
             break
   
cap.release()
cv2.destroyAllWindows()


# In[ ]:


mp_holistic.FACE_CONNECTIONS


# In[ ]:


pip install mediapipe==0.8.9.1


# In[ ]:


mp_holistic.FACEMESH_CONTOURS


# In[ ]:


cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        #Recolor 
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        #print(results.face_landmarks)
        
        #face_landmarks, post_landmarks, left_hand_landmarks, right_hand_landmarks
        
        #Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        #Draw face landmarks
        #mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
        
        #Right hand
        #mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        
        #Left hand
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        
        #Post Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        
    
        cv2.imshow('MediaPipe test for Active Plus', image)
    
        if cv2.waitKey(10) & 0xFF == ord('q'):
             break
   
cap.release()
cv2.destroyAllWindows()


# In[ ]:


mp_holistic.POSE_CONNECTIONS


# In[ ]:




