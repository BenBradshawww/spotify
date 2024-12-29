WITH source AS (
    SELECT
      *
    FROM {{ source('spotify', 'spotify_old_songs') }}
),

model AS (
    SELECT
        spotify_old_songs_id,
        spotify_old_songs_updated_at,
        spotify_old_songs_stopped_playing_at,
        spotify_old_songs_artist_name,
        spotify_old_songs_track_name,
        spotify_old_songs_ms_player
    FROM source
)

SELECT * FROM model
