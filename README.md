source code from:https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe  
This file is modified by AnselCh on 2022.

需要套件:pip install -r requirements.txt  

-----可調參數-----

device:選擇webcam  
max_num_hands:偵測手部數量  
width,height  
min_detection_confidence: 0 ~ 1  
min_tracking_confidence : 0 ~ 1  

----------------
主程式: sp_app.py  
可使用hand_sign_id進行設定要執行的動作
----------------
訓練手勢步驟:  
1.執行\hand_mediapipeSP\record_gestures.py  
    'a':紀錄手勢模式  
    0~9新增手勢  
    每按一下若增側到手勢便會新增21個landmarks到\hand_mediapipeSP\sp_model\keypoint.csv  
  
2.進入\hand_mediapipeSP\sp_model\keypoint_label.csv  
    新增手勢名稱  
  
3.執行\hand_mediapipeSP\training_gestures.ipynb  
    csv檔訓練成hdf5 , tflite  
  
訓練動作步驟:  
1.要先確地有設定 point_history  
    執行\hand_mediapipeSP\record_gestures.py  
    'm':紀錄手勢模式  
    0~9新增手勢  
    每按一下若增側到手勢便會新增21個landmarks到\hand_mediapipeSP\sp_model\point_history.csv  
  
2.進入\hand_mediapipeSP\sp_model\point_history_label.csv  
    新增動作名稱  
  
3.執行\hand_mediapipeSP\training_moving.ipynb  
    csv檔訓練成hdf5 , tflite  
  
----------------
重置csv檔
----------------
  
重置手勢:手勢訓練模式按'R'後，按'1'  
重置動作:手勢訓練模式按'R'後，按'2'  
