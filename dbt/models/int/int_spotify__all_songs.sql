WITH old_songs AS (
    SELECT 
        spotify_old_songs_id AS spotify_id,
        spotify_old_songs_track_id AS spotify_track_id,
        spotify_old_songs_artist_name AS spotify_artist_name,
        spotify_old_songs_track_name AS spotify_track_name,
        spotify_old_songs_album_name AS spotify_album_name,
        spotify_old_songs_ms_played AS spotify_ms_played,
        spotify_old_songs_reason_start AS spotify_reason_start,
        spotify_old_songs_reason_end AS spotify_reason_end,
        spotify_old_songs_shuffle AS spotify_shuffle,
        spotify_old_songs_skipped AS spotify_skipped,
        spotify_old_songs_offline AS spotify_offline,
        DATE_TRUNC('second', spotify_old_songs_started_playing_at) AS spotify_track_played_at
    FROM {{ ref('base_spotify__old_songs') }}
),

last_songs AS (
    SELECT
        spotify_last_songs_id AS spotify_id,
        spotify_last_songs_track_id AS spotify_track_id,
        spotify_last_songs_artist_name AS spotify_artist_name,
        spotify_last_songs_track_name AS spotify_track_name,
        NULL AS spotify_album_name,
        CAST(NULL AS INTEGER) AS spotify_ms_played,
        CAST(NULL AS VARCHAR) AS spotify_reason_start,
        CAST(NULL AS VARCHAR) AS spotify_reason_end,
        CAST(NULL AS BOOLEAN) AS spotify_shuffle,
        CAST(NULL AS BOOLEAN) AS spotify_skipped,
        CAST(NULL AS BOOLEAN) AS spotify_offline,
        DATE_TRUNC('second', spotify_last_songs_track_played_at) AS spotify_track_played_at
    FROM {{ ref('base_spotify__last_songs')}}
),

all_songs AS (
    SELECT * FROM old_songs
    UNION
    SELECT * FROM last_songs
)

SELECT * FROM all_songs
