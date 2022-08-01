# notes

## scripts
- to run a detection script
`
python detect.py --weights runs/train/exp23/weights/best.pt --source /media/samin/MadRabbit/datasets/tomato_disease/mixed/000002.jpg
`
- run a train script for tomato disease detection
`
python tomato_train.py --data tomato.yaml --weights yolov5s.pt --batch 20 --epochs 10
`
## things to learn
- how to resize image for input
- make a separate folder for each train file for storing weights and detect
- 'back' label in tomato image