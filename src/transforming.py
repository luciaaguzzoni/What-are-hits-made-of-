import pandas as pd

def decade(year):
    if year<1969:
        return '60s'
    elif year<1979:
        return '70s'
    elif year<1989:
        return '80s'
    elif year<1999:
        return '90s'
    elif year<2009:
        return '2000s'
    elif year<=2020:
        return '2010s'
    

def create_year_decade_columns(df):
    #create column with release year of the track album
    pattern_year="(^\d{4})"
    df["track_album_release_year"]= df["track_album_release_date"].str.extract(pattern_year)
    #create column with release decade of the track album
    df["track_album_release_decade"] = pd.to_numeric(df["track_album_release_year"]).apply(decade)
    return df















def most_popular(df,n):
    '''
    input: dataframe of songs from same decade, int n
    output: dataframe with the 'n' most popular songs from that decade
    '''
    best_df= df.sort_values("track_popularity", ascending=False) #sorting by popularity
    best_df = best_df.reset_index(drop=True) #rearranging the index
    best_df = best_df.truncate(before=0,after=n) #keeping firts n sogns
    return best_df





def popularity(df,year):
    '''
    input: dataframe df with songs from decade 'year'
    creates an histogram displayng track_popularity of the songs in dataframe df
    '''
    popularity=sns.histplot(df, x="track_popularity", bins=30)
    plt.xlabel("Popularity")
    if year=='00':
        year==2000
    elif year=='10':
        year==2010
    plt.title(f"Popularity of songs from {year}'s'")
    popularity.figure.savefig(f"../images/popularity{year}.jpg", dpi=1000)
    plt.clf()
    return popularity

def popularity2(df,year):
    '''
    input: dataframe df with songs from decade 'year'
    creates a bar plot displayng number of songs for each track_popularity value, sorted by year
    '''
    popularity= sns.countplot(data=df[df["track_popularity"]>75], y="track_popularity", order=[i for i in range(75,101)], palette="husl")
    plt.xlabel("Popularity")
    if year=='00':
        year==2000
    elif year=='10':
        year==2010
    plt.title(f"Popularity of songs from {year}'s'")
    popularity.figure.savefig(f"../images/popularity{year}_2.jpg", dpi=1000)
    plt.clf()
    return popularity



def most_popular_2(df,p):
    '''
    input: dataframe of songs from same decade, int n
    output: dataframe with songs from that decade with track_popularity >= p
    '''
    best_df = df[df["track_popularity"]>=p] #keeping only the songs with track_popularity >= p
    best_df= best_df.sort_values("track_popularity", ascending=False) #sorting by popularity
    best_df = best_df.reset_index(drop=True) #rearranging the index
    return best_df

def most_popular_3(df,n_min):
    '''
    input: dataframe of songs from same decade, int n
    output: dataframe with at least n_min songs from that decade with highest 'track_popularity'
    '''
    best_df= df.sort_values("track_popularity", ascending=False) #sorting by popularity
    best_df = best_df.reset_index(drop=True) #rearranging the index
    p = best_df.iloc[n_min-1]["track_popularity"]
    best_df = df[df["track_popularity"]>=p] #keeping only the songs with track_popularity >= p
    return best_df

