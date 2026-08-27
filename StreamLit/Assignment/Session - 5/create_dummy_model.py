import pickle

class DummyModel:

    def predict(self, features):
        t1 = features[0][0]
        t2 = features[0][1]
        if t1 > t2:
            return ['Team 1']
        else:
            return ['Team 2']
with open('ipl_model.pkl', 'wb') as f:
    pickle.dump(DummyModel(), f)