from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
import pandas as pd


def top_titles_for_latent(W,n_titles,titles):
    '''
    find the most relevant titles for latent features
    '''

    max_idx = np.argsort(W,axis=0)[:-n_titles-1:0-1]
    titles_idx = max_idx.T
    for i,idx in enumerate(titles_idx):
        print 'topic: {}, \ntitles:\n{}'.format(i+1,titles[idx])

def top_words_for_latent(H,n_words,vocal):
    max_idx = np.argsort(H,axis=1)[:,:-n_words-1:0-1]
    for i,idx in enumerate(max_idx):
        print 'topic: {}, \ntitles:\n{}'.format(i+1,vocal[idx])


def fit_nmf(obs_matrix,n_topic, vocabulary):
    '''
    Takes in TF-IDF matrix and vocab list
    Decomposes matrix to W & H
    Returns matrices W & H
    '''

    nmf = NMF(n_components = n_topic,random_state=42) #5 latent features
    W = nmf.fit_transform(obs_matrix)
    H = nmf.components_
    return W,H

def MF(obs,n_topic):
    '''Matrix factorization'''

    vect = TfidfVectorizer(max_features=1000, stop_words='english')
    obs_matrix = vect.fit_transform(obs).toarray()
    vocabulary = np.array(vect.get_feature_names())
    W,H = fit_nmf(obs_matrix,n_topic, vocabulary)

    return W,H,vocabulary

def plot_state_heatmap(df,filename):
    '''create a state-wise heatmap for bigfoot sightings'''

    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = df['code'],
            z = df['Obs'].astype(float),
            locationmode = 'USA-states',
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                )
            ),
            colorbar = dict(
                title = "Sightings Number"
            )
        ) ]

    layout = dict(
            title = 'Bigfoot sightings Heatmap',
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)',
            ),
        )

    fig = dict( data=data, layout=layout )

    url = py.plot( fig, filename=filename )

if __name__ == '__main__':

    obs = df['Obs']


    vect = TfidfVectorizer(max_features=1000, stop_words='english')
    obs_matrix = vect.fit_transform(obs).toarray()
    vocabulary = np.array(vect.get_feature_names())

    W,H = fit_nmf(obs_matrix, vocabulary)
    top_words_for_latent(H,10,vocabulary)
    top_titles_for_latent(W,5,df['Title'])
