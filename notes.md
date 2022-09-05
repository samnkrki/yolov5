# notes

## scripts
- to run a detection script
`
python detect.py --weights runs/train/exp56/weights/last-fp16.tflite --source /home/samin/Documents/datasets/tomato_disease/images/000002.jpg --data data/tomato.yaml
`
- run a train script for tomato disease detection
`
python tomato_train.py --data tomato.yaml --weights yolov5s.pt --batch 20 --epochs 10 --cache disk
`
## things to learn
- how to resize image for input
- make a separate folder for each train file for storing weights and detect
- 'back' label in tomato image

## export
 `
 python export.py --weights runs/train/exp55/weights/last.pt --include tflite --data data/tomato.yaml --img 640 --int8
 `
 
## current script
python train.py --data tomato.yaml --weights yolov5m.pt --cache disk --img 640 --batch-size 5 --epoch 300 --resume
python train.py --data potholes.yaml --weights yolov5m.pt --cache disk --img 640 --batch-size 5 --epoch 50

