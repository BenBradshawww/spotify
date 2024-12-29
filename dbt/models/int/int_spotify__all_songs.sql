WITH old_songs AS (
    SELECT 
        NULL AS spotify_track_id,
        spotify_old_songs_artist_name AS spotify_artist_name,
        spotify_old_songs_track_name AS spotify_track_name,
        DATE_TRUNC('second', spotify_old_songs_stopped_playing_at - spotify_old_songs_ms_player * INTERVAL '1 millisecond') AS spotify_track_played_at
    FROM {{ ref('base_spotify__old_songs') }}
),

last_songs AS (
    SELECT
        spotify_last_songs_track_id AS spotify_track_id,
        spotify_last_songs_artist_name AS spotify_artist_name,
        spotify_last_songs_track_name AS spotify_track_name,
        DATE_TRUNC('second', spotify_last_songs_track_played_at) AS spotify_track_played_at
    FROM {{ ref('base_spotify__last_songs')}}
),

all_songs AS (
    SELECT * FROM old_songs
    UNION
    SELECT * FROM last_songs
)

SELECT * FROM all_songs
