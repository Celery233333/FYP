# python predict_multi.py -voc_p D:\Celery\1\Y4\FYP\sample\polyphonic-omr\experiment_code\vocab\rnn_pitch.txt -voc_r D:\Celery\1\Y4\FYP\sample\polyphonic-omr\experiment_code\vocab\rnn_rhythm.txt -model D:\Celery\1\Y4\FYP\sample\polyphonic-omr\experiment_code\models\latest_model60.pt -images D:\Celery\1\Y4\FYP\corpus\images -out D:\Celery\1\Y4\FYP\corpus1\output

import argparse
import utils
import cv2
import numpy as np
import torch
import os
import sys
import random

import model

def write_output(seq, output_file):

    """
    Writes sequence to an output file
    """

    with open(output_file, 'w') as f:

        f.write(seq)
        f.close()

        # print('File written:',output_file)

def predict(imgpath, mode):
    
    modelpath = 'models/rnndecoder.pt'

    # Setup GPU stuff
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print('Using',device)

    # Params used in train_multi.py
    max_chord_stack = 10

    # Read the pitch vocabulary and create dictionary
    dict_file = open('vocab/rnn_pitch.txt','r')
    dict_list = dict_file.read().splitlines()
    pitch_int2word = dict()
    pitch_word2int = dict()
    for word in dict_list:
        word_idx = len(pitch_int2word)
        pitch_int2word[word_idx] = word
        pitch_word2int[word] = word_idx
    dict_file.close()

    # Read the length vocabulary and create dictionary
    dict_file = open('vocab/rnn_rhythm.txt','r')
    dict_list = dict_file.read().splitlines()
    length_int2word = dict()
    length_word2int = dict()
    for word in dict_list:
        word_idx = len(length_int2word)
        length_int2word[word_idx] = word
        length_word2int[word] = word_idx
    dict_file.close()

    # Load model params
    params = model.default_model_params()

    # Create model
    nn_model = model.RNNDecoder(params, len(pitch_int2word), len(length_int2word), max_chord_stack)
    nn_model.to(device)

    # Restore model
    state_dict = torch.load(modelpath,map_location='cpu')
    nn_model.load_state_dict(state_dict['model'])

    nn_model.eval()

    # For building batches
    images = []
    lengths = []

    # Length calculation
    width_reduction = 1
    for i in range(params['conv_blocks']):
        width_reduction = width_reduction * params['conv_pooling_size'][i][1]

    # Preprocess image
    image = cv2.imread(imgpath, cv2.IMREAD_UNCHANGED)
    try:
        if image.shape[2] == 4:     # we have an alpha channel
            a1 = ~image[:,:,3]        # extract and invert that alpha
            image = cv2.add(cv2.merge([a1,a1,a1,a1]), image)   # add up values (with clipping)
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)    # strip alpha channel
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        elif image.shape[2] == 3:   # no alpha channel (musicma_abaro)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) 
    except IndexError: # 2d image
        pass
    height = params['img_height']
    if mode == 'tough':
        kernel = np.ones((3,3),np.uint8)  
        image = cv2.dilate(image,kernel,iterations = 1)
        image = cv2.erode(image,kernel,iterations = 1)
        image = cv2.GaussianBlur(image, (5, 5), 0) 
        image = cv2.bilateralFilter(image,5,75,75)
        image = cv2.medianBlur(image, 3)
    image = utils.resize(image,height)

    # # erosion & dilation
    # choice = random.randint(0,2)
    # kernel = np.ones((1,2),np.uint8)  
    # if choice == 1:
    #     image = cv2.dilate(image,kernel,iterations = 1)
    # if choice == 2:
    #     image = cv2.erode(image,kernel,iterations = 1)
    
    # # rotaion between (-3,3)
    # (h, w) = image.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, random.uniform(-3,3), 1.0)
    # image = cv2.warpAffine(image, M, (w, h),borderValue=(255,255,255)) 

    # # distortion
    # K = np.array(
    #     [
    #         [w/3, 0.0, w/2],
    #         [0.0, -w/2, 0.0],
    #         [0.0, 0.0, 1.0],
    #     ]
    # )
    # D = np.array([0, -0.25, 1, 0])
    # map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, (w,h), cv2.CV_16SC2)
    # image = cv2.remap(
    #     image, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT
    # )
        
    # Add to lists
    images.append(utils.normalize(image))
    lengths.append((2*2*2*image.shape[1] // width_reduction))   # Based on conv architecture

    # Check if ready to predict
    if len(images) == 1:

        # Get max width
        image_widths = [img.shape[1] for img in images]
        max_image_width = max(image_widths)

        batch_images = np.zeros(shape=[1,
                                params['img_height'],
                                max_image_width,
                                params['img_channels']], dtype=np.float32)

        for i, img in enumerate(images):
            batch_images[i, 0:img.shape[0], 0:img.shape[1], 0] = img

        batch_images = (torch.from_numpy(batch_images)).permute(0, 3, 1, 2) # batch, channels, height, width
            
        lengths = torch.tensor(lengths).unsqueeze(0)

        with torch.no_grad():

            # Forward pass
            pitch_outs, length_outs = nn_model(batch_images.to(device))
            out_lengths = torch.cat((max_chord_stack*[lengths]), 1)

            # Concat the pitch_outs and length_outs
            pitch_outs = torch.cat((pitch_outs),1)
            length_outs = torch.cat((length_outs),1)

            # Decode predictions
            haha = True
            if haha:
                preds = utils.multi_decode(pitch_outs, out_lengths[0], max_chord_stack)
            else:
                preds = utils.multi_decode(length_outs, out_lengths[0], max_chord_stack)
            decoded_preds = []
            for i, l_pred in enumerate(preds):
                for pred in l_pred:
                    string_seq = ''
                    s = []
                    for p in pred:
                        string_seq += pitch_int2word[p] if haha else length_int2word[p]
                        string_seq += ' '
                        s.append(pitch_int2word[p] if haha else length_int2word[p])
                    decoded_preds.append(s)

            for k in range(1): # BATCH SIZE
                img_idx = k
                string_pred = ''
                k = k * 10
                for i in range(len(decoded_preds[k])):
                    for j in range(max_chord_stack):
                        if i < len(decoded_preds[k+j]) and decoded_preds[k+j][i] != 'noNote':
                            string_pred += decoded_preds[k+j][i] + ' '
                    string_pred += '+' + ' '
                string_pred = string_pred[:-2] # Remove last '+' char and space from prediction
                output_file = os.path.join('temp/prediction' + '.txt')
                write_output(string_pred, output_file) 

                    
            # Reset values
            lengths = []
            images = [] 
    print(string_pred)
    return string_pred