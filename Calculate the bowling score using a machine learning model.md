
<span style="color:red">**Can we calculate the bowling score based on a sequence of rolls using a machine learning model?**</span>

## Where is the idea from?

When I was asked to make a program for to calculate the score of a bowling game based on a sequence of rolls, I was not too impressed. I'm Data Scientist, that's not what I usually work with. I managed to finished the task (detailed solution can be found in [here](bowling_score_calculator.py)), but felt like I could do more. 

Since I never really played a bowling game before, I never know how to calculate the score of a bowling game, I had to read the score logic very clearly before I start coding for it. Then I had this thought, can I use a machine learning model to calculate the bowling score? If I have a bunch of roll sequences and their corresponding score, can I use a machine learning mode to learn the rule by itself? That way I don't have to struggle to understand every details of the score logic.

This seems a great idea!

I was disappointed not long after I found that there doesn't seem any data of roll sequences I can use.

## Where to start?
I decided to make my own data.
First, I create a [bowling game](bowling_game.py) program that can play 10 turns;
Then, I [created](create_bowling_data.py)  5000 bowling games and calculate their scores and save them to a [csv](bowling_data_5000.csv) file.

Now I have some data, it's time to roll.

## The initial thought:
While I think of it, it's interesting that the process of building a machine learning model is exactly the opposite of programming to calculate the bowling score based on some defined rules. A good machine learning model is supposed to capture the true rules underlying the data. 
Since we all know that the rules for calculating the score of a bowling game have something to do with making decision at some critical point, like a strike or a spare. 

## The assumption:
The assumption for this project is as follows:
- We have some data with roll sequences and their corresponding score.
- We know there are some rules you can use to calculate the score, but you don't want to read the details.
- We can use a machine learning model to help us learn the rules and calculate the score of a bowling game based on a sequence of rolls for us.

## How to make it happen?
A very import part in building a machine learning model is exploratory data analysis (EDA) and data preprocessing. During this step, we will need to figure out how to represent our data, what feature do we need and how to create the features.

### 1. EDA 
First let's read the data and check how does it look like. 


```python
# read data
import pandas as pd
bowling_data = pd.read_csv('bowling_data_5000.csv')
```


```python
# check the first five rows
bowling_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sequence</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>XX4/X8/2/X7/XX07</td>
      <td>193</td>
    </tr>
    <tr>
      <th>1</th>
      <td>X2/XX7/4/3/XXX67</td>
      <td>213</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3/X3/2/2/8/2/XXX88</td>
      <td>198</td>
    </tr>
    <tr>
      <th>3</th>
      <td>X-/5/XX3/6/XXX50</td>
      <td>204</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8/9/7/5/1/X3/X1/1/9</td>
      <td>172</td>
    </tr>
  </tbody>
</table>
</div>




We put the bowling game data in a dataframe. As we can see from the upper table, there two columns, the 'Sequence' column holds the sequence of rolls for each game, and the 'Score' column holds the score for that sequence of rolls. Each row represents one game.  

Although the assumption is we don't know the details of the rules of scoring, we do know that the order of the roll matters and type of roll (strike, spare) matters. So we will take this information into account when we generate our features. 

This reminds of a very good way to deal with sequential data which is LSTM(long short - term memory). LSTM is a type of type of Recurrent Neural Network (RNN) and has been used in lots of tech companies including Google, Apple, to solve problems regarding natural languange text compression and unsegmented connected handwriting recognition, etc [1](https://en.wikipedia.org/wiki/Long_short-term_memory).

### 2. Data Preprocessing
Here I will use keras package in Python to preprocess the data.


```python
# seperate the data into input:X and output:Y
X = bowling_data.Sequence
Y = bowling_data.Score
```


```python
# tokenize the sequence of rolls into single roll and create features 
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence

tok = Tokenizer(char_level=True)
tok.fit_on_texts(X)
sequences = tok.texts_to_sequences(X)
```


```python
# since LSTM require same input dimension and our roll sequences have differnt length
# we will need to pad our rolls
max_len = 21 # that's the most rolls a game can have 
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len, padding='post')
```


```python
# reshape our data to use in the model
seq_matrix_reshape = sequences_matrix.reshape(5000, 21, 1)
Y_reshape = Y.values.reshape(5000,1)
```

### 3. Train the model



```python
from keras.layers import LSTM, Input, Bidirectional, Dense
from keras.models import Sequential
# set up input dimension
data_dim = 1
timesteps = 22
num_classes = 1

# initiate the model
model = Sequential()
model.add(Bidirectional(LSTM(32, return_sequences=True,input_shape=(timesteps, data_dim))))
model.add(Bidirectional(LSTM(32, return_sequences=True))) 
model.add(Bidirectional(LSTM(32)))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')
```

Here I didn't use a test dataset to test the model performance. Because I know that there is a definite rule behind this set of data that I don't need to worry about the overfitting issue. If it fits, it finds the rule.


```python
# start training
# because I don't have a lot of time now, I will just train 10 epochs to have a taste
model.fit(seq_matrix_reshape, Y_reshape,
          batch_size=64, epochs=10,
          validation_data=(seq_matrix_reshape, Y_reshape))
```

    Train on 5000 samples, validate on 5000 samples
    Epoch 1/10
    5000/5000 [==============================] - 13s 3ms/step - loss: 36821.3275 - val_loss: 34432.6505
    Epoch 2/10
    5000/5000 [==============================] - 9s 2ms/step - loss: 33347.9910 - val_loss: 32290.7854
    Epoch 3/10
    5000/5000 [==============================] - 9s 2ms/step - loss: 31355.4527 - val_loss: 30401.9174
    Epoch 4/10
    5000/5000 [==============================] - 9s 2ms/step - loss: 29533.5474 - val_loss: 28641.7739
    Epoch 5/10
    5000/5000 [==============================] - 9s 2ms/step - loss: 27821.8807 - val_loss: 26979.5037
    Epoch 6/10
    5000/5000 [==============================] - 10s 2ms/step - loss: 26202.8973 - val_loss: 25402.5721
    Epoch 7/10
    5000/5000 [==============================] - 10s 2ms/step - loss: 24665.2637 - val_loss: 23904.3037
    Epoch 8/10
    5000/5000 [==============================] - 10s 2ms/step - loss: 23201.8754 - val_loss: 22477.1204
    Epoch 9/10
    5000/5000 [==============================] - 9s 2ms/step - loss: 21809.0589 - val_loss: 21118.8180
    Epoch 10/10
    5000/5000 [==============================] - 9s 2ms/step - loss: 20482.7720 - val_loss: 19826.5016





    <keras.callbacks.History at 0x10f7a4c88>



### 4. Prediction
Now let's see how good the model has learnt the scoring rules.
Since we didn't use too many epochs, we can see that the loss is still very high. The result will be bad, but we might be able to see some trend.


```python
# predict
pred = model.predict(seq_matrix_reshape)
```


```python
# check the result for the first 10 games
pred[0:10]
```




    array([[61.28873],
           [61.28873],
           [61.28873],
           [61.28873],
           [61.28873],
           [61.28873],
           [61.28873],
           [61.28873],
           [61.28873],
           [61.28873]], dtype=float32)



The result looks strange, all the predictions are the same. There are lots of reasons for that, I think I will need some time to figure that out.

## Conclusion
In this stage, the model I tried had failed to calculate the score of a bowling game using the sequence of rolls. However, there are lot of things we can do to improve the performance of the model, like change the batch size, add more epoches and so on. 
With more effort, I believe I will be able to train a good model to calculate the bowling game eventually.
