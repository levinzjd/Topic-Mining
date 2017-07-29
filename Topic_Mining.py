from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


def top_titles_for_latent(W,n_titles,titles):
    max_idx = np.argsort(W,axis=0)[:-n_titles-1:0-1]
    titles_idx = max_idx.T
    for i,idx in enumerate(titles_idx):
        print 'topic: {}, \ntitles:\n{}'.format(i+1,titles[idx])

def top_words_for_latent(H,n_words,vocal):
    max_idx = np.argsort(H,axis=1)[:,:-n_words-1:0-1]
    for i,idx in enumerate(max_idx):
        print 'topic: {}, \ntitles:\n{}'.format(i+1,vocal[idx])


def fit_nmf(obs_matrix, vocabulary):
    '''
    Takes in TF-IDF matrix and vocab list
    Decomposes matrix to W & H
    Returns matrices W & H
    '''
    nmf = NMF(n_components = 5,random_state=42) #5 latent features
    W = nmf.fit_transform(obs_matrix)
    H = nmf.components_
    return W,H


if __name__ == '__main__':

    obs = df['Obs']


    vect = TfidfVectorizer(max_features=1000, stop_words='english')
    obs_matrix = vect.fit_transform(obs).toarray()
    vocabulary = np.array(vect.get_feature_names())

    W,H = fit_nmf(obs_matrix, vocabulary)
    top_words_for_latent(H,10,vocabulary)
    top_titles_for_latent(W,5,df['Title'])
