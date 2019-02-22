import CubeStructure as cs
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import metrics
from tensorflow.python.data import Dataset
tf.logging.set_verbosity(tf.logging.ERROR)
def get_features(cube):
    d = {}
    for i in range(24):
        d[str(i)] = [cube.state[i]]
    processed_features = pd.DataFrame(data = d)
    return processed_features

def make_targets(moves_away):
    output_targets = pd.DataFrame()
    output_targets['movesaway'] = [moves_away]
    return output_targets

def construct_feature_columns(input_features):
  """Construct the TensorFlow Feature Columns.

  Args:
    input_features: The names of the numerical input features to use.
  Returns:
    A set of feature columns
  """


  
  return set([tf.feature_column.indicator_column(
      tf.feature_column.categorical_column_with_identity(
          key = my_feature,
          num_buckets = 6))
              for my_feature in input_features])
    

def my_input_fn(features):
    features = {key:np.array(value) for key,value in dict(features).items()}
    
    ds = Dataset.from_tensor_slices(features)
    ds = ds.batch(1)
    features = ds.make_one_shot_iterator().get_next()
 
    return features

def my_training_input_fn(features, targets):
    features = {key:np.array(value) for key,value in dict(features).items()}
    
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(1)

    (features, targets) = ds.make_one_shot_iterator().get_next()
 
    return (features, targets)


def get_cube_score(cube, regressor):
    features = get_features(cube)
    predict_input_fn = lambda: my_input_fn(features)
    predictions = regressor.predict(predict_input_fn)
    predictions = np.array([item['predictions'][0] for item in predictions])
    return predictions[0]

def make_dnn_regressor():
    features = get_features(cs.solvedcube())
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

    dnn_regressor = tf.estimator.DNNRegressor(
        hidden_units = [72, 24],
        feature_columns = construct_feature_columns(features),
        optimizer = my_optimizer)
    return dnn_regressor

def train_regressor(cube, regressor, moves_away):
    features = get_features(cube)
    targets = make_targets(moves_away)

    training_input_fn = lambda: my_training_input_fn(features, targets['movesaway'])
    
    regressor.train(input_fn = training_input_fn)


def weighted_bfs(cube, regressor):
    if cube.solved():
        print("Cube already solved")
        return None
    PQ = [[get_cube_score(cube, regressor), cube, []]]
    visited = [cube]
    SolvedCube = cs.solvedcube()
    while True:
        curPair = PQ.pop(0)
        print(curPair[2], curPair[0])
        curCube = curPair[1]
        curSeq = curPair[2]
        for i in range(6):
            newSeq = curSeq.copy()
            newSeq.append(cs.moveliststr[i])
            newCube = curCube.copy()
            cs.movelist[i](newCube)
            if newCube.solved():
                print(newSeq)
                return newSeq
            if newCube in visited:
                pass
            else:
                PQ.append([get_cube_score(newCube, regressor), newCube.copy(), newSeq])
                PQ.sort(key = lambda x: x[0])
                visited.append(newCube.copy())


def train_on_easy_random_cubes(num_cube, regressor, scramble_length):
    if regressor == None:
            regressor = make_dnn_regressor()
    for counter in range(num_cube):
        
    
        (scramble, random_cube) = cs.randomcube(scramble_length)
        print ("Cube {0}".format(counter + 1))
        print(scramble)
        seq = weighted_bfs(random_cube, regressor)
        l = len(seq)
        train_regressor(random_cube, regressor, l)
        for i in range(l):
            j = cs.moveliststr.index(seq[i])
            cs.movelist[j](random_cube)
            train_regressor(random_cube, regressor, min((l - i - 1)/7 - 1, 1))
        print("Solved Cube Value:")
        print(get_cube_score(cs.solvedcube(), regressor))
    return regressor


OutputRegressor = train_on_easy_random_cubes(100, None, 1)
OutputRegressor = train_on_easy_random_cubes(100, OutputRegressor, 2)
OutputRegressor = train_on_easy_random_cubes(100, OutputRegressor, 3)


